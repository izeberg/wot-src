from helpers import dependency
from gui.impl.lobby.seniority_awards.seniority_reward_award_view import SeniorityRewardAwardView
from one_time_gift.skeletons.gui.game_control import IOneTimeGiftController

class OTGSeniorityRewardAwardView(SeniorityRewardAwardView):
    __otgCtrl = dependency.descriptor(IOneTimeGiftController)

    def _onLoading(self, data, *args, **kwargs):
        super(OTGSeniorityRewardAwardView, self)._onLoading(data, *args, **kwargs)
        self.viewModel.setIsOTGRewardsAvailable(self.__isOTGRewardAvailable())

    @property
    def _needBlockShopTransition(self):
        return super(OTGSeniorityRewardAwardView, self)._needBlockShopTransition or self.__isOTGRewardAvailable()

    def _onSettingsChange(self):
        with self.viewModel.transaction() as (vm):
            vm.setShopOnOpenState(self.__getShopOnOpenState())
            vm.setIsOTGRewardsAvailable(self.__isOTGRewardAvailable())

    def _getEvents(self):
        return super(OTGSeniorityRewardAwardView, self)._getEvents() + (
         (
          self.__otgCtrl.onSettingsChanged, self._onSettingsChange),
         (
          self.__otgCtrl.onEntryPointUpdated, self._onSettingsChange),
         (
          self.__otgCtrl.onPlayerOTGStatusChanged, self._onSettingsChange))

    def __isOTGRewardAvailable(self):
        return self.__otgCtrl.isEntryPointEnabled and self.__otgCtrl.isEntryPointActive