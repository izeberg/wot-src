from helpers import dependency, time_utils
from gui.impl.lobby.gf_notifications import NotificationBase
from gui.Scaleform.daapi.view.lobby.customization.states import CustomizationState
from gui.Scaleform.lobby_entry import getLobbyStateMachine
from one_time_gift.gui.impl.gen.view_models.views.lobby.reward_available_notification_view_model import RewardAvailableNotificationViewModel
from one_time_gift.skeletons.gui.game_control import IOneTimeGiftController

def _isCustomizationState():
    lsm = getLobbyStateMachine()
    customizationState = lsm.getStateByCls(CustomizationState)
    return customizationState and customizationState.isEntered()


class RewardAvailableNotificationView(NotificationBase):
    __oneTimeGiftController = dependency.descriptor(IOneTimeGiftController)

    def __init__(self, resId, *args, **kwargs):
        model = RewardAvailableNotificationViewModel()
        super(RewardAvailableNotificationView, self).__init__(resId, model, *args, **kwargs)

    @property
    def viewModel(self):
        return super(RewardAvailableNotificationView, self).getViewModel()

    def _getEvents(self):
        return super(RewardAvailableNotificationView, self)._getEvents() + (
         (
          self.viewModel.onClose, self.__onClose),
         (
          self.viewModel.onClaimReward, self.__onClaimReward),
         (
          self.__oneTimeGiftController.onSettingsChanged, self._update),
         (
          self.__oneTimeGiftController.onEntryPointUpdated, self._update))

    def _update(self):
        with self.viewModel.transaction() as (vm):
            vm.setIsPopUp(self._isPopUp)
            currentTime = time_utils.getServerUTCTime()
            if currentTime >= self.__oneTimeGiftController.getRemindTime():
                vm.setTimeLeft(self.__oneTimeGiftController.getEndTime() - currentTime)
            self.viewModel.setIsDisabled(not self.__oneTimeGiftController.isEntryPointActive or _isCustomizationState())

    def __onClose(self):
        self.destroyWindow()

    def __onClaimReward(self):
        self.__oneTimeGiftController.onEntryPointClicked()