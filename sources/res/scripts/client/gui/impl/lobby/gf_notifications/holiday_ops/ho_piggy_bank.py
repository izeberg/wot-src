from gui.impl.gen.view_models.views.lobby.new_year.notifications.ny_piggy_bank_multiple_rewards_model import NyPiggyBankMultipleRewardsModel
from gui.impl.gen.view_models.views.lobby.new_year.notifications.ny_piggy_bank_single_reward_model import NyPiggyBankSingleRewardModel
from gui.impl.lobby.gf_notifications.holiday_ops.award_notification_base import bonusesSortOrder, splitHugeBonuses, AwardNotificationBase, fromRawBonusesToBonuses
from gui.impl.new_year.new_year_bonus_packer import getPiggyBankBonusPacker
from gui.impl.lobby.new_year.states import FriendsState
from gui.impl.new_year.new_year_helper import backportTooltipDecorator
from gui.shared.gui_items import GUI_ITEM_TYPE
from helpers import dependency
from skeletons.gui.server_events import IEventsCache
from skeletons.gui.shared import IItemsCache
from skeletons.new_year import IFriendServiceController

class HOPiggyBankSingleReward(AwardNotificationBase):
    __itemsCache = dependency.descriptor(IItemsCache)
    __eventsCache = dependency.descriptor(IEventsCache)
    __friendsService = dependency.descriptor(IFriendServiceController)

    def __init__(self, resId, *args, **kwargs):
        model = kwargs.pop('model', NyPiggyBankSingleRewardModel())
        super(HOPiggyBankSingleReward, self).__init__(resId, model, *args, **kwargs)
        self._rewards = []

    @property
    def viewModel(self):
        return super(HOPiggyBankSingleReward, self).getViewModel()

    @backportTooltipDecorator()
    def createToolTip(self, event):
        return super(HOPiggyBankSingleReward, self).createToolTip(event)

    def _canNavigate(self):
        bonuses = self._rewards
        if self._hasBonusStyle(bonuses):
            return super(HOPiggyBankSingleReward, self)._canNavigate() and self._canShowStyle()
        return super(HOPiggyBankSingleReward, self)._canNavigate() and self.__friendsService.isServiceEnabled and self._nyController.isEnabled()

    def _getEvents(self):
        events = super(HOPiggyBankSingleReward, self)._getEvents()
        return events + (
         (
          self.viewModel.onStylePreview, self.__onStylePreview),
         (
          self.viewModel.onGoToFriends, self.__onGoToFriends))

    def _onLoading(self, *args, **kwargs):
        rawBonuses = self._getPayload()['bonuses']
        for rawBonus in rawBonuses:
            self._rewards += fromRawBonusesToBonuses(rawBonus)

        super(HOPiggyBankSingleReward, self)._onLoading(self)

    def _update(self):
        bonuses = self._rewards
        with self.getViewModel().transaction() as (model):
            self._tooltips.clear()
            self._fillRewardsList(rewardsList=model.rewards.getItems(), bonuses=bonuses, sortMethod=bonusesSortOrder, packer=getPiggyBankBonusPacker())
            model.setIsPopUp(self._isPopUp)
            model.setIsButtonDisabled(not self._canNavigate())
            model.setIsStyle(self._hasBonusStyle(bonuses))

    @staticmethod
    def _hasBonusStyle(bonuses):
        for bonus in bonuses:
            if bonus.getName() != 'customizations':
                continue
            for bonusData in bonus.getList():
                if bonusData.get('itemTypeID') == GUI_ITEM_TYPE.STYLE:
                    return True

        return False

    def __onStylePreview(self, intCD):
        styleItem = self.__itemsCache.items.getItemByCD(int(intCD.get('intCD')))
        if styleItem is None:
            return
        else:
            self._showStylePreview(styleItem)
            return

    def __onGoToFriends(self):
        if self._canNavigate():
            if self.__friendsService.isInFriendHangar:
                self.__friendsService.preLeaveFriendHangar()
            FriendsState.goTo(instantly=True)


class HOPiggyBankMultipleRewards(HOPiggyBankSingleReward):

    def __init__(self, resId, *args, **kwargs):
        model = NyPiggyBankMultipleRewardsModel()
        super(HOPiggyBankMultipleRewards, self).__init__(resId, model=model, *args, **kwargs)

    @property
    def viewModel(self):
        return super(HOPiggyBankMultipleRewards, self).getViewModel()

    def _update(self):
        hugeBonuses, otherBonuses = splitHugeBonuses(self._rewards)
        with self.getViewModel().transaction() as (model):
            self._tooltips.clear()
            self._fillRewardsList(rewardsList=model.rewards.getItems(), bonuses=hugeBonuses, sortMethod=bonusesSortOrder, packer=getPiggyBankBonusPacker())
            self._fillRewardsList(rewardsList=model.additionalRewards.getItems(), bonuses=otherBonuses, sortMethod=bonusesSortOrder, packer=getPiggyBankBonusPacker())
            model.setIsPopUp(self._isPopUp)
            model.setIsButtonDisabled(not self._canNavigate())
            model.setIsStyle(self._hasBonusStyle(self._rewards))