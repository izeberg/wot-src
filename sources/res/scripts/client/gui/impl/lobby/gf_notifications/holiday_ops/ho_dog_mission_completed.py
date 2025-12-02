from gui.impl.lobby.gf_notifications.holiday_ops.notifications_utils import isAcceptableState
from gui.shared import g_eventBus, events as events_constants
from helpers import dependency
from ho_notification import HONotification
from gui.impl.gen.view_models.views.lobby.new_year.notifications.ny_dog_mission_completed_model import NyDogMissionCompletedModel
from new_year.ny_constants import NYObjects
from skeletons.new_year import IFriendServiceController

class HODogMissionCompleted(HONotification):
    __friendController = dependency.descriptor(IFriendServiceController)

    def __init__(self, resId, *args, **kwargs):
        model = NyDogMissionCompletedModel()
        super(HODogMissionCompleted, self).__init__(resId, model, *args, **kwargs)

    @property
    def viewModel(self):
        return super(HODogMissionCompleted, self).getViewModel()

    def _getEvents(self):
        events = super(HODogMissionCompleted, self)._getEvents()
        return events + (
         (
          self.viewModel.onClick, self.__onClick),)

    def _canNavigate(self):
        return super(HODogMissionCompleted, self)._canNavigate() and self._nyController.isEnabled()

    def _update(self):
        data = self._getPayload()
        with self.viewModel.transaction() as (model):
            model.setIsPopUp(self._isPopUp)
            model.setMissionsCompleted(data['missionsCompleted'])
            model.setMissionsTotal(data['missionsTotal'])
            model.setBundleLevel(data['dogLevel'])
            model.setIsButtonDisabled(not self._canNavigate() or not isAcceptableState(self.prbEntity))

    def __onClick(self):
        if self._canNavigate():
            g_eventBus.handleEvent(events_constants.HidePopoverEvent(events_constants.HidePopoverEvent.HIDE_POPOVER))
            if self.__friendController.isInFriendHangar:
                self.__friendController.leaveFriendHangar()
            self._navigateToNy(NYObjects.CELEBRITY_D)