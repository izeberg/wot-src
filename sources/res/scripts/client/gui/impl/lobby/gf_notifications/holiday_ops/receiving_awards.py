from CurrentVehicle import g_currentVehicle
from gui.impl.gen.resources import R
from gui.impl.gen.view_models.views.lobby.new_year.notifications.receiving_rewards_model import ReceivingRewardsModel
from gui.impl.gen.view_models.views.lobby.new_year.views.atmosphere_level_up_model import ButtonActionType
from gui.impl.lobby.gf_notifications.holiday_ops.award_notification_base import AwardNotificationBase, splitHugeBonuses, customSplitBonuses, fromRawBonusesToBonuses
from gui.impl.lobby.gf_notifications.holiday_ops.notifications_utils import isAcceptableState
from gui.impl.lobby.new_year.action_helper import getButtonAction, ACTION_TO_STATES
from gui.impl.lobby.new_year.tooltips.ny_gift_machine_token_tooltip import NyGiftMachineTokenTooltip
from gui.impl.lobby.new_year.tooltips.ny_guest_tooltip import NyGuestTooltip
from gui.impl.lobby.new_year.tooltips.ny_marketplace_token_tooltip import NyMarketplaceTokenTooltip
from gui.impl.lobby.tooltips.additional_rewards_tooltip import AdditionalRewardsTooltip
from gui.impl.new_year.new_year_bonus_packer import getChallengeBonusPacker, getHOLevelUpBonusSortOrder
from gui.impl.new_year.new_year_helper import backportTooltipDecorator
from gui.shared import g_eventBus, events, EVENT_BUS_SCOPE
from helpers import dependency, isPlayerAccount
from shared_utils import findFirst, first
from skeletons.gui.server_events import IEventsCache
from skeletons.gui.shared import IItemsCache
_FIRST_LVL = 1

class HOReceivingAwards(AwardNotificationBase):
    __itemsCache = dependency.descriptor(IItemsCache)
    eventsCache = dependency.descriptor(IEventsCache)

    def __init__(self, resId, *args, **kwargs):
        model = ReceivingRewardsModel()
        super(HOReceivingAwards, self).__init__(resId, model, *args, **kwargs)
        self.__rewards = []
        self.__currentLevel = 0
        self.__buttonAction = ButtonActionType.UNDEFINED

    @property
    def viewModel(self):
        return super(HOReceivingAwards, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        data = self._getPayload()
        self.__rewards = fromRawBonusesToBonuses(data.get('bonuses', []))
        self.__currentLevel = data.get('completedLevel', 0)
        battleCount = self.__itemsCache.items.getAccountDossier().getTotalStats().getBattlesCount()
        if self.__currentLevel == _FIRST_LVL and self._isPopUp:
            g_eventBus.handleEvent(events.NyInitialNotificationEvent(eventType=events.NyInitialNotificationEvent.INITIAL_NOTIFICATION_SHOWN), scope=EVENT_BUS_SCOPE.LOBBY)
            if battleCount > 0:
                self.__processVehicleChange()
        super(HOReceivingAwards, self)._onLoading(self)

    def _canNavigate(self):
        return super(HOReceivingAwards, self)._canNavigate() and self._nyController.isEnabled()

    def _update(self):
        self.__setRewards()

    def _getEvents(self):
        return super(HOReceivingAwards, self)._getEvents() + (
         (
          self.viewModel.onClick, self._onClick),)

    def createToolTipContent(self, event, ctID):
        if ctID == R.views.lobby.tooltips.AdditionalRewardsTooltip():
            showCount = int(event.getArgument('showedCount'))
            bonuses = customSplitBonuses(self.__rewards)
            _, secondaryBonuses = splitHugeBonuses(bonuses)
            bonuses = sorted(secondaryBonuses, key=getHOLevelUpBonusSortOrder)[showCount:]
            bonusPackers = getChallengeBonusPacker()
            packedBonuses = []
            for bonus in bonuses:
                if bonus.isShowInGUI():
                    bonusList = bonusPackers.pack(bonus)
                    for item in bonusList:
                        packedBonuses.append(item)

            return AdditionalRewardsTooltip(packedBonuses)
        if ctID == R.views.mono.holiday_ops.tooltips.ho_marketplace_token_tooltip():
            return NyMarketplaceTokenTooltip()
        if ctID == R.views.mono.holiday_ops.tooltips.ho_guest_tooltip():
            guestType = str(event.getArgument('guestType'))
            return NyGuestTooltip(guestType)
        if ctID == R.views.mono.holiday_ops.tooltips.ho_gift_machine_token_tooltip():
            return NyGiftMachineTokenTooltip()
        return super(HOReceivingAwards, self).createToolTipContent(event, ctID)

    @backportTooltipDecorator()
    def createToolTip(self, event):
        return super(HOReceivingAwards, self).createToolTip(event)

    def __processVehicleChange(self):
        if not isPlayerAccount():
            return
        else:
            vehicleBonus = findFirst(lambda bonus: bonus.getName() == 'vehicles', self.__rewards)
            if vehicleBonus is not None:
                vehicle, _ = first(vehicleBonus.getVehicles(), (None, None))
                if vehicle is not None:
                    g_currentVehicle.selectVehicle(vehicle.invID)
            return

    def __setRewards(self):
        bonuses = customSplitBonuses(self.__rewards)
        hugeBonuses, otherBonuses = splitHugeBonuses(bonuses)
        self.__buttonAction = self.__getRewardsAwards(self.__currentLevel, bonuses)
        with self.getViewModel().transaction() as (model):
            self._tooltips.clear()
            self._fillRewardsList(rewardsList=model.hugeRewards.getItems(), bonuses=hugeBonuses, sortMethod=getHOLevelUpBonusSortOrder, packer=getChallengeBonusPacker())
            self._fillRewardsList(rewardsList=model.rewards.getItems(), bonuses=otherBonuses, sortMethod=getHOLevelUpBonusSortOrder, packer=getChallengeBonusPacker())
            model.setIsPopUp(self._isPopUp)
            model.setLevel(self.__currentLevel)
            model.setIsButtonDisabled(not self._canNavigate() or self.__buttonAction != ButtonActionType.TOREWARDS and not isAcceptableState(self.prbEntity))
            model.setButtonAction(self.__buttonAction)

    def __getRewardsAwards(self, level, bonuses):
        action = getButtonAction(level, bonuses)
        if action != ButtonActionType.UNDEFINED:
            return action
        return ButtonActionType.TOREWARDS

    def _onClick(self):
        state, instantly = ACTION_TO_STATES.get(self.__buttonAction)
        if state and self._canNavigate():
            g_eventBus.handleEvent(events.HidePopoverEvent(events.HidePopoverEvent.HIDE_POPOVER))

            def navigationAction():
                state.goTo(instantly=instantly)

            if self.currentHangarAcceptable:
                navigationAction()
            else:
                self._gfNotificationController.selectRandomBattle(navigationAction)