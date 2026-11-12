import typing
from frameworks.wulf import ViewSettings, WindowLayer, ViewStatus
from gui.impl.backport import BackportTooltipWindow, TooltipData
from gui.impl.gen.resources import R
from gui.impl.lobby.tooltips.additional_rewards_tooltip import AdditionalRewardsTooltip
from gui.impl.pub import ViewImpl
from gui.impl.pub.lobby_window import LobbyNotificationWindow
from gui.server_events.bonuses import VehiclesBonus, getAllNonQuestBonuses
from gui.shared.event_dispatcher import selectVehicleInHangar
from helpers import dependency
from messenger.proto.events import g_messengerEvents
from new_year.gui.impl.gen.view_models.views.lobby.new_year.ny_pet_raid_reward_view_model import NyPetRaidRewardViewModel
from new_year.gui.impl.new_year.new_year_bonus_packer import getPetRaidBonusPacker, packBonusModelAndTooltipData
from new_year.gui.shared.event_dispatcher import showLootBoxEntry
from new_year.gui.shared.ny_machine_helper import isMachineEnabled
from new_year.ny_constants import NewYearLootBoxes, ViewAliases
from new_year.skeletons.new_year import INewYearController, ITamagotchiDataProvider
from shared_utils import findFirst
from skeletons.gui.impl import INewYearNavigation
from new_year.gui.impl.new_year.sounds import OVERLAY_HANGAR_SOUND_SPACE
from new_year.gui.shared.formatters import formatPurchaseItems
from new_year.tamagotchi.sys_msg.sys_msg_handler import TamagotchiSysMsgHandler
if typing.TYPE_CHECKING:
    from typing import Dict, List
    from gui.server_events.bonuses import SimpleBonus

class NyPetRaidRewardView(ViewImpl):
    __slots__ = ('__rewards', '__tooltips', '__rewardsSource')
    __nyController = dependency.descriptor(INewYearController)
    __newYearNavigation = dependency.descriptor(INewYearNavigation)
    __dataProvider = dependency.descriptor(ITamagotchiDataProvider)
    _COMMON_SOUND_SPACE = OVERLAY_HANGAR_SOUND_SPACE

    def __init__(self, rewards):
        settings = ViewSettings(R.views.new_year.lobby.new_year.NyPetRaidRewardView())
        settings.model = NyPetRaidRewardViewModel()
        super(NyPetRaidRewardView, self).__init__(settings)
        self.__tooltips = {}
        normalizedRewards = rewards.copy()
        if 'vehicles' in normalizedRewards:
            normalizedRewards['vehicles'] = [
             normalizedRewards['vehicles']]
        self.__rewards = getAllNonQuestBonuses(normalizedRewards)
        self.__rewardsSource = rewards

    @property
    def viewModel(self):
        return super(NyPetRaidRewardView, self).getViewModel()

    def createToolTipContent(self, event, contentID):
        lootboxesViews = R.views.dyn('gui_lootboxes')
        if lootboxesViews.isValid() and contentID == lootboxesViews.lobby.gui_lootboxes.tooltips.LootboxTooltip():
            tooltipData = self.__tooltips.get(event.getArgument('tooltipId'))
            if tooltipData is not None:
                return tooltipData.tooltip(*tooltipData.specialArgs)
            return
        if lootboxesViews.isValid() and contentID == lootboxesViews.lobby.gui_lootboxes.tooltips.CompensationTooltip():
            tooltipData = self.__tooltips.get(event.getArgument('tooltipId'))
            if tooltipData is not None:
                from gui_lootboxes.gui.impl.lobby.gui_lootboxes.tooltips.compensation_tooltip import LootBoxesCompensationTooltip
                return LootBoxesCompensationTooltip(*tooltipData.specialArgs)
            return
        if self.viewStatus == ViewStatus.LOADED and contentID == R.views.lobby.tooltips.AdditionalRewardsTooltip():
            showCount = int(event.getArgument('showedCount'))
            packer = getPetRaidBonusPacker()
            rewards = []
            for bonus in self.__rewards:
                if bonus.isShowInGUI():
                    rewards.extend(packer.pack(bonus))

            return AdditionalRewardsTooltip(rewards[showCount:])
        else:
            return super(NyPetRaidRewardView, self).createToolTipContent(event, contentID)

    def createToolTip(self, event):
        if event.contentID == R.views.common.tooltip_window.backport_tooltip_content.BackportTooltipContent():
            tooltipData = self.__tooltips.get(event.getArgument('tooltipId'))
            if tooltipData is None:
                return
            window = BackportTooltipWindow(tooltipData, self.getParentWindow())
            window.load()
            return window
        else:
            return super(NyPetRaidRewardView, self).createToolTip(event)

    def _initialize(self, *args, **kwargs):
        super(NyPetRaidRewardView, self)._initialize(*args, **kwargs)
        g_messengerEvents.onLockPopUpMessages(lockHigh=True)
        self.__updateRewards()

    def _finalize(self):
        self.__showRaidRewardsOpenedNotification()
        g_messengerEvents.onUnlockPopUpMessages()
        super(NyPetRaidRewardView, self)._finalize()
        self.__rewards = None
        return

    def __showRaidRewardsOpenedNotification(self):
        if not self.__rewards:
            return
        rewardsText = formatPurchaseItems(self.__rewardsSource, getPetRaidBonusPacker())
        TamagotchiSysMsgHandler.sendRaidRewardsOpened(rewardsText)

    def _getEvents(self):
        return (
         (
          self.viewModel.onClose, self.__onCloseAction),
         (
          self.viewModel.onGoToLootbox, self.__onGoToLootbox),
         (
          self.viewModel.onGoToMachine, self.__onGoToMachine),
         (
          self.viewModel.onGotoPet, self.__onGoToPet),
         (
          self.viewModel.onShowInHangar, self.__onShowInHangar),
         (
          self.__nyController.onStateChanged, self.__onEventStateChanged),
         (
          self.__dataProvider.onRaccoonStateUpdated, self.__onRaccoonStateUpdated))

    def __updateRewards(self):
        with self.viewModel.transaction() as (model):
            rewardsList = model.rewards.getItems()
            self.__tooltips.clear()
            rewardsList.clear()
            packBonusModelAndTooltipData(self.__rewards, rewardsList, getPetRaidBonusPacker(), self.__tooltips)
            model.setIsPetAvailable(self.__dataProvider.raccoonState)
            model.setIsMachineAvailable(isMachineEnabled())
            model.setHasVehicle(self.__getVehicle() is not None)
            rewardsList.invalidate()
        return

    def __getVehicle(self):
        vehicleBonus = findFirst(lambda bonus: bonus.getName() == VehiclesBonus.VEHICLES_BONUS, self.__rewards)
        if vehicleBonus is None:
            return
        else:
            vehicle, _ = vehicleBonus.getVehicles()[0]
            return vehicle

    def __onCloseAction(self):
        self.destroyWindow()

    def __onEventStateChanged(self):
        if not self.__nyController.isEnabled():
            self.destroyWindow()
            return
        self.viewModel.setIsMachineAvailable(isMachineEnabled())

    def __onGoToMachine(self):
        self.__newYearNavigation.showViewAfterPrbSwitch(ViewAliases.SURPRISE_MACHINE_VIEW)
        self.destroyWindow()

    def __onGoToLootbox(self):
        showLootBoxEntry(lootBoxType=NewYearLootBoxes.NY_CUR_YEAR_SMALL)
        self.destroyWindow()

    def __onGoToPet(self):
        self.__newYearNavigation.showViewAfterPrbSwitch(ViewAliases.PET_VIEW, isLoadedFromHangar=False)
        self.destroyWindow()

    def __onShowInHangar(self):
        vehicle = self.__getVehicle()
        selectVehicleInHangar(vehicle.intCD)
        self.destroyWindow()

    def __onRaccoonStateUpdated(self, isUnlocked):
        self.viewModel.setIsPetAvailable(isUnlocked)


class NyPetRaidRewardViewWindow(LobbyNotificationWindow):
    __slots__ = ()

    def __init__(self, rewards, parent=None):
        super(NyPetRaidRewardViewWindow, self).__init__(content=NyPetRaidRewardView(rewards), layer=WindowLayer.TOP_WINDOW, parent=parent)