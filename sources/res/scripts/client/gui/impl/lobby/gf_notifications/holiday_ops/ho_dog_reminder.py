from gui.impl.lobby.gf_notifications.holiday_ops.notifications_utils import isAcceptableState
from gui.shared import g_eventBus, events as events_constants
from helpers import dependency
from ho_notification import HONotification
from gui.impl.gen.view_models.views.lobby.new_year.notifications.ny_dog_reminder_model import NyDogReminderModel
from new_year.ny_constants import NYObjects
from skeletons.gui.server_events import IEventsCache
from skeletons.new_year import IFriendServiceController

class HODogReminder(HONotification):
    __friendController = dependency.descriptor(IFriendServiceController)
    __eventsCache = dependency.descriptor(IEventsCache)

    def __init__(self, resId, *args, **kwargs):
        model = NyDogReminderModel()
        super(HODogReminder, self).__init__(resId, model, *args, **kwargs)

    @property
    def viewModel(self):
        return super(HODogReminder, self).getViewModel()

    def _getEvents(self):
        events = super(HODogReminder, self)._getEvents()
        return events + (
         (
          self.viewModel.onClick, self.__onClick),)

    def _canNavigate(self):
        return super(HODogReminder, self)._canNavigate() and self._nyController.isEnabled()

    def _update(self):
        with self.viewModel.transaction() as (model):
            model.setIsPopUp(self._isPopUp)
            model.setIsButtonDisabled(not self._canNavigate() or not isAcceptableState(self.prbEntity))

    def __onClick(self):
        if self._canNavigate():
            g_eventBus.handleEvent(events_constants.HidePopoverEvent(events_constants.HidePopoverEvent.HIDE_POPOVER))
            if self.__friendController.isInFriendHangar:
                self.__friendController.leaveFriendHangar()
            self._navigateToNy(NYObjects.CELEBRITY_D)