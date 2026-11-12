import Windowing
from constants import DOSSIER_TYPE
from frameworks.wulf import ViewFlags, ViewSettings, WindowFlags, WindowLayer
from CurrentVehicle import g_currentVehicle
from debug_utils import LOG_ERROR
from gui.impl.gen import R
from gui.impl.lobby.common.view_wrappers import createBackportTooltipDecorator
from gui.impl.lobby.personal_missions.personal_mission_bonuses_packers import packBonusModelAndTooltipData
from gui.impl.pub import ViewImpl
from gui.impl.pub.lobby_window import LobbyNotificationWindow
from gui.server_events.bonuses import getNonQuestBonuses
from gui.shared.event_dispatcher import showHangar
from helpers import dependency
from items.vehicles import getVehicleClassFromVehicleType
from new_year.gui.impl.new_year.sounds import VideoRewardsSoundControl, NY_LEADERBOARD_TANK_REWARD_SOUND
from new_year.gui.impl.gen.view_models.views.lobby.new_year.ny_video_reward_view_model import NyVideoRewardViewModel
from new_year.helpers.ny_leaderboard_tank_reward import markLeaderboardTankRewardSeen
from new_year.skeletons.new_year import INewYearController, ITamagotchiDataProvider
from skeletons.gui.shared import IItemsCache

class NyVideoRewardView(ViewImpl):
    __slots__ = ('__seasonID', '__vehicleCD', '__rewards', '__vehicle', '__tooltipData',
                 '__soundControl', '__isVideoStarted')
    __itemsCache = dependency.descriptor(IItemsCache)
    __nyController = dependency.descriptor(INewYearController)
    __dataProvider = dependency.descriptor(ITamagotchiDataProvider)

    def __init__(self, layoutID, seasonID, vehicleCD, rewards):
        settings = ViewSettings(layoutID)
        settings.flags = ViewFlags.VIEW
        settings.model = NyVideoRewardViewModel()
        super(NyVideoRewardView, self).__init__(settings)
        self.__seasonID = seasonID
        self.__vehicleCD = vehicleCD
        self.__rewards = rewards or {}
        self.__vehicle = self.__itemsCache.items.getItemByCD(vehicleCD) if vehicleCD else None
        self.__tooltipData = {}
        self.__soundControl = VideoRewardsSoundControl(NY_LEADERBOARD_TANK_REWARD_SOUND)
        self.__isVideoStarted = False
        return

    @property
    def viewModel(self):
        return super(NyVideoRewardView, self).getViewModel()

    @createBackportTooltipDecorator()
    def createToolTip(self, event):
        return super(NyVideoRewardView, self).createToolTip(event)

    def getTooltipData(self, event):
        index = event.getArgument('tooltipId')
        return self.__tooltipData.get(index)

    def _finalize(self):
        Windowing.removeWindowAccessibilityHandler(self.__onWindowAccessibilityChanged)
        if self.__isVideoStarted:
            self.__soundControl.stop()
        self.__nyController.leaderboardTankReward.notifyPresentedFinished()
        super(NyVideoRewardView, self)._finalize()

    def _getEvents(self):
        return (
         (
          self.viewModel.onClose, self.__onClose),
         (
          self.viewModel.onError, self.__onError),
         (
          self.viewModel.onShowVehicle, self.__onShowVehicle),
         (
          self.viewModel.onVideoStarted, self.__onVideoStarted))

    def _onLoading(self, *args, **kwargs):
        super(NyVideoRewardView, self)._onLoading(*args, **kwargs)
        if self.__vehicle is None:
            LOG_ERROR('[NyVideoRewardView] vehicle not found: ', self.__vehicleCD, nice=True)
            markLeaderboardTankRewardSeen(self.__seasonID)
            self.destroyWindow()
            return
        else:
            with self.viewModel.transaction() as (vm):
                vm.setVehicleName(self.__vehicle.userName)
                vm.setVehicleLvl(self.__vehicle.level)
                vm.setVehicleType(getVehicleClassFromVehicleType(self.__vehicle.descriptor.type))
                vm.setIsElite(self.__vehicle.isElite or self.__vehicle.isPremium)
                vm.setVehicleCD(self.__vehicle.intCD)
                vm.setIsWindowAccessible(Windowing.isWindowAccessible())
                vm.setIsFocused(self.isFocused)
                vm.setStage(self.__seasonID)
                if self.__seasonID == 0:
                    vm.setPosition(self.__getPosition())
                badgeBonuses, badgeTop = self.__getBadgeData()
                vm.setBadgeTop(badgeTop)
                packBonusModelAndTooltipData(badgeBonuses, vm.getRewards(), self.__tooltipData)
                vm.setHasExtraRewards(bool(badgeBonuses))
            Windowing.addWindowAccessibilitynHandler(self.__onWindowAccessibilityChanged)
            return

    def __getBadgeData(self):
        playerBadges = self.__rewards.get('playerBadges') or ()
        remapBadges = {}
        badgeTop = 0
        for badgeRecord in playerBadges:
            badgeId = badgeRecord.get('id')
            if badgeId is None:
                continue
            remapBadges[('playerBadges', badgeId)] = {'unique': badgeRecord.get('unique'), 'value': badgeRecord.get('count')}
            badgeTop = badgeTop or badgeRecord.get('top') or 0

        if remapBadges:
            return (getNonQuestBonuses('dossier', {DOSSIER_TYPE.ACCOUNT: remapBadges}), badgeTop)
        else:
            dossier = self.__rewards.get('dossier')
            if not dossier:
                return ([], 0)
            return (getNonQuestBonuses('dossier', dossier), 0)

    def __getPosition(self):
        if not self.__dataProvider.hasCumulativeLeaderboard:
            return 0
        else:
            cumulative = self.__dataProvider.cumulativeLeaderboard
            if cumulative is not None:
                return cumulative.user.position
            return 0

    def __onClose(self):
        self.destroyWindow()

    def __onError(self, args):
        errorFilePath = str(args.get('errorFilePath', ''))
        LOG_ERROR('[NyVideoRewardView] video error: ', errorFilePath, nice=True)
        markLeaderboardTankRewardSeen(self.__seasonID)
        self.destroyWindow()

    def __onShowVehicle(self):
        vehicle = self.__itemsCache.items.getItemByCD(self.__vehicleCD)
        if vehicle is not None and vehicle.isInInventory:
            showHangar()
            g_currentVehicle.selectVehicle(vehicle.invID)
        self.destroyWindow()
        return

    def __onVideoStarted(self):
        markLeaderboardTankRewardSeen(self.__seasonID)
        self.__startVideoSound()
        if not self.__isPlaybackAccessible():
            self.__soundControl.pause()

    def __onWindowAccessibilityChanged(self, isWindowAccessible):
        self.viewModel.setIsWindowAccessible(isWindowAccessible)
        self.__syncPlaybackState()

    def _onFocus(self, focused):
        super(NyVideoRewardView, self)._onFocus(focused)
        self.viewModel.setIsFocused(focused)
        self.__syncPlaybackState()

    def __syncPlaybackState(self):
        if self.__isPlaybackAccessible():
            if self.__isVideoStarted:
                self.__soundControl.unpause()
            else:
                self.__startVideoSound()
        elif self.__isVideoStarted:
            self.__soundControl.pause()

    def __startVideoSound(self):
        if self.__isVideoStarted:
            return
        self.__isVideoStarted = True
        self.__soundControl.start()

    def __isPlaybackAccessible(self):
        return Windowing.isWindowAccessible() and self.isFocused


class NyVideoRewardViewWindow(LobbyNotificationWindow):
    __slots__ = ()

    def __init__(self, seasonID, vehicleCD, rewards, parent=None):
        super(NyVideoRewardViewWindow, self).__init__(wndFlags=WindowFlags.WINDOW | WindowFlags.WINDOW_FULLSCREEN, content=NyVideoRewardView(R.views.new_year.lobby.new_year.NyVideoRewardView(), seasonID=seasonID, vehicleCD=vehicleCD, rewards=rewards), parent=parent, layer=WindowLayer.OVERLAY)