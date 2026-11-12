import BigWorld, SoundGroups, Windowing
from debug_utils import LOG_ERROR
from frameworks.wulf import ViewSettings, WindowFlags, WindowLayer
from gui.impl.gen import R
from gui.shared.event_dispatcher import selectVehicleInHangar
from gui.shared.gui_items.Vehicle import getNationLessName
from gui.sounds.filters import States, StatesGroup
from gui_lootboxes.gui.bonuses.bonuses_packers import getMainRewardsBonusPacker
from gui_lootboxes.gui.impl.gen.view_models.views.lobby.gui_lootboxes.lootbox_open_by_selection_view_model import LootboxOpenBySelectionViewModel
from gui.impl.pub import ViewImpl, WindowImpl
from gui.impl.gui_decorators import args2params
from gui_lootboxes.gui.impl.gen.view_models.views.lobby.gui_lootboxes.reward_video_model import RewardVideoModel
from gui_lootboxes.gui.impl.lobby.gui_lootboxes.lootbox_video_reward_config import REWARD_VIDEO_CONFIG
from gui_lootboxes.gui.impl.lobby.gui_lootboxes.lootbox_video_reward_view import packVideoRewardConfig
from gui_lootboxes.gui.impl.lobby.gui_lootboxes.sound import LOOT_BOXES_OVERLAY_SOUND_SPACE
from gui_lootboxes.gui.impl.lobby.gui_lootboxes.sounds import BaseVideoRewardsSoundControl
from gui_lootboxes.gui.shared.event_dispatcher import showLootBoxOpenErrorWindow
from helpers import dependency
from gui_lootboxes.gui.lb_gui_constants import SCH_CLIENT_MSG_TYPE
from skeletons.gui.game_control import IGuiLootBoxesController
from skeletons.gui.impl import IGuiLoader
from uilogging.lootboxes import LootboxStorageLogger
from skeletons.gui.shared import IItemsCache
from skeletons.gui.system_messages import ISystemMessages
from gui.SystemMessages import ResultMsg, SM_TYPE
from gui.server_events.bonuses import getNonQuestBonuses
from gui.impl.lobby.common.view_helpers import packBonusModelAndTooltipData
from functools import partial
from shared_utils import first

class _SoundControl(BaseVideoRewardsSoundControl):
    _SOUND_EVENT_TEMPLATE = 'gui_video_ny_lootbox_{}'
    _DEFAULT = 'tank_legendary'

    def __init__(self):
        super(_SoundControl, self).__init__('')

    def start(self):
        self.enableVideoOverlay()
        super(_SoundControl, self).start()

    def stop(self):
        super(_SoundControl, self).stop()
        SoundGroups.g_instance.setState(StatesGroup.VIDEO_OVERLAY, States.VIDEO_OVERLAY_OFF)

    @staticmethod
    def enableVideoOverlay():
        SoundGroups.g_instance.setState(StatesGroup.VIDEO_OVERLAY, States.VIDEO_OVERLAY_ON)


class LootboxOpenBySelectionView(ViewImpl):
    __slots__ = ('__boxID', '__count', '__soundControl', '__rewards', '__bonusName',
                 '__uiLogger', '__isSkipped')
    __itemsCache = dependency.descriptor(IItemsCache)
    __systemMessages = dependency.descriptor(ISystemMessages)
    __guiLoader = dependency.descriptor(IGuiLoader)
    __guiLootBoxes = dependency.descriptor(IGuiLootBoxesController)
    _COMMON_SOUND_SPACE = LOOT_BOXES_OVERLAY_SOUND_SPACE

    def __init__(self, layoutID, boxID):
        settings = ViewSettings(layoutID)
        settings.model = LootboxOpenBySelectionViewModel()
        lootbox = self.__itemsCache.items.tokens.getLootBoxByID(boxID)
        settings.model.setLootBoxIconName(lootbox.getIconName())
        self.__boxID = boxID
        self.__count = min(lootbox.getSelectionCardsCount(), lootbox.getSelectionBonusLeft())
        self.__soundControl = _SoundControl()
        self.__rewards = None
        self.__bonusName = ''
        self.__isSkipped = False
        self.__uiLogger = LootboxStorageLogger()
        super(LootboxOpenBySelectionView, self).__init__(settings)
        return

    @property
    def viewModel(self):
        return super(LootboxOpenBySelectionView, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        super(LootboxOpenBySelectionView, self)._onLoading(*args, **kwargs)
        if self.__count < 1:
            LOG_ERROR('Failed to open Selection view for negative card count')
            self.__exitWithError()
            return
        cards = self.viewModel.getCards()
        cards.clear()
        for index in range(self.__count):
            cards.addNumber(index)

        cards.invalidate()
        if self.__count == 1:
            self.__openSelected(0)
        Windowing.addWindowAccessibilitynHandler(self.__onWindowAccessibilityChanged)

    def _finalize(self):
        super(LootboxOpenBySelectionView, self)._finalize()
        Windowing.removeWindowAccessibilityHandler(self.__onWindowAccessibilityChanged)
        self.__soundControl.stop()

    def _getEvents(self):
        return (
         (
          self.viewModel.onCardSelect, self.__onCardSelect),
         (
          self.viewModel.onSkip, self.__onSkip),
         (
          self.viewModel.onClose, self.__onClose),
         (
          self.viewModel.onVideoStarted, self.__onVideoStarted),
         (
          self.viewModel.onVideoEnded, self.__onVideoEnded),
         (
          self.viewModel.onPreview, self.__onPreview))

    def __openSelected(self, cardId):
        if self.__rewards is not None:
            LOG_ERROR('Attempt to select card twice. reward already obtained')
            self.__exitWithError()
            return
        else:
            self.viewModel.setIsLoading(True)
            BigWorld.player().tokens.openBoxesBySelection(self.__boxID, cardId, partial(self.__onResultReceived, cardId))
            return

    @args2params(int)
    def __onCardSelect(self, cardId):
        self.__openSelected(cardId)

    def __onSkip(self, args):
        self.__uiLogger.logSkipAnimation(self.__boxID, int(args.get('skipWay')), 'after_card_selection')
        self.__isSkipped = True
        self.__soundControl.stop()

    def __onClose(self):
        self.destroyWindow()

    @args2params(bool)
    def __onVideoStarted(self, isEffectVideo):
        if self.__isSkipped:
            return
        if isEffectVideo:
            self.__soundControl.enableVideoOverlay()
            return
        self.__soundControl.setBonusName(self.__bonusName)
        self.__soundControl.start()

    @args2params(bool)
    def __onVideoEnded(self, isEffectVideo):
        if isEffectVideo:
            return
        self.__soundControl.stop()

    def __onResultReceived(self, cardId, resultID, errorStr, ext):
        if self.viewModel is None:
            return False
        else:
            self.viewModel.setIsLoading(False)
            if errorStr:
                LOG_ERROR('Failed to open lootbox', resultID, errorStr)
                self.__exitWithError()
                return
            result = ResultMsg(True, '', SM_TYPE.LootBoxRewards, None, {}, ext)
            self.__guiLootBoxes.onOpenLootboxesComplete(result)
            self.__uiLogger.logCardSelect(self.__boxID, cardId)
            self.__rewards = first(ext['bonus'])
            self.__showNotification(ext)
            self.__fillRewards(ext)
            return

    def __onWindowAccessibilityChanged(self, isWindowAccessible):
        self.__soundControl.handleWindowFocus(isWindowAccessible)
        self.viewModel.setIsWindowAccessible(isWindowAccessible)

    def __fillRewards(self, ext):
        rewards = []
        for bonusesDict in ext['rewards']:
            for bonusType, bonusValue in bonusesDict.items():
                rewards.extend(getNonQuestBonuses(bonusType, bonusValue))

        rewardModels = self.viewModel.getRewards()
        rewardModels.clear()
        packBonusModelAndTooltipData(rewards, rewardModels, None, getMainRewardsBonusPacker())
        rewardModels.invalidate()
        self.__fillRewardVideo(ext)
        return

    def __fillRewardVideo(self, ext):
        rewardVideos = self.viewModel.getRewardVideos()
        rewardVideos.clear()
        name = 'vehicles'
        for vehicleReward in self.__rewards[name]:
            for venIntCD, _ in vehicleReward.iteritems():
                vehicle = self.__itemsCache.items.getItemByCD(venIntCD)
                key = self.__itemsCache.items.tokens.getLootBoxByID(self.__boxID).getType()
                videoRes = getNationLessName(vehicle.name).replace('-', '_')
                videoRewardConfig = REWARD_VIDEO_CONFIG[key][name]['videos']
                for videoConfig in packVideoRewardConfig(key, videoRes, videoRewardConfig):
                    model = RewardVideoModel()
                    model.setVideoResName(videoConfig['videoResName'])
                    model.setDuration(videoConfig['duration'])
                    model.setShowFooterTiming(videoConfig['showFooterTiming'])
                    rewardVideos.addViewModel(model)

                self.__bonusName = getNationLessName(vehicle.name)

        rewardVideos.invalidate()

    @args2params(int)
    def __onPreview(self, intCD):
        self.__closeStorageView()
        selectVehicleInHangar(intCD)

    def __closeStorageView(self):
        view = self.__guiLoader.windowsManager.getViewByLayoutID(R.views.gui_lootboxes.lobby.gui_lootboxes.StorageView())
        if view:
            view.destroyWindow()

    def __showNotification(self, ext):
        message = {'rewards': self.__rewards, 
           'failedKeys': {}, 'usedKeys': {}, 'openedLootBoxes': ext['extData']['openedLootBoxes']}
        self.__systemMessages.proto.serviceChannel.pushClientMessage(message, SCH_CLIENT_MSG_TYPE.LB_OPENED)

    def __exitWithError(self):
        view = self.__guiLoader.windowsManager.getViewByLayoutID(R.views.gui_lootboxes.lobby.gui_lootboxes.StorageView())
        if not view:
            LOG_ERROR('Failed to find parent view for error Window')
            return
        self.destroyWindow()
        showLootBoxOpenErrorWindow(view.getParentWindow())


class LootboxOpenBySelectionViewWindow(WindowImpl):
    __slots__ = ()

    def __init__(self, boxID, parent=None):
        super(LootboxOpenBySelectionViewWindow, self).__init__(WindowFlags.WINDOW | WindowFlags.WINDOW_FULLSCREEN, content=LootboxOpenBySelectionView(self.getViewId(), boxID), parent=parent, layer=WindowLayer.OVERLAY)

    @staticmethod
    def getViewId():
        return R.views.gui_lootboxes.lobby.gui_lootboxes.LootboxOpenBySelectionView()