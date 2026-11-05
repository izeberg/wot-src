from __future__ import absolute_import
from account_helpers.AccountSettings import AdventCalendar
from advent_calendar.gui.impl.gen.view_models.views.lobby.notifications.available_doors_view_model import AvailableDoorsViewModel, State
from advent_calendar.gui.impl.lobby.feature.advent_helper import setAdventCalendarSetting
from advent_calendar.gui.shared.event_dispatcher import showAdventCalendarMainWindow
from advent_calendar.skeletons import IAdventCalendarController
from gui.impl import backport
from gui.impl.gen import R
from gui.impl.lobby.gf_notifications.notification_base import NotificationBase
from helpers import dependency

class AvailableDoorsView(NotificationBase):
    _adventController = dependency.descriptor(IAdventCalendarController)
    _DESCRIPTION_RESOURCE = ''
    _BACKGROUND_RESOURCE = ''

    def __init__(self, resId, *args, **kwargs):
        super(AvailableDoorsView, self).__init__(resId, AvailableDoorsViewModel(), *args, **kwargs)

    @property
    def viewModel(self):
        return self.getViewModel()

    @property
    def rewardImagePath(self):
        return backport.image(R.images.advent_calendar.gui.maps.icons.notifications.reward())

    def _getEvents(self):
        events = super(AvailableDoorsView, self)._getEvents()
        return events + (
         (
          self.viewModel.onClick, self._onClick),)

    def _update(self):
        state = State(self.linkageData.state)
        if self._isPopUp:
            currentDay = self._adventController.getCurrentDayNumber()
            setAdventCalendarSetting(AdventCalendar.LAST_DAY_POPUP_SEEN, currentDay)
        with self.viewModel.transaction() as (tx):
            tx.setState(state)
            tx.setEventEndDate(self._adventController.postEventEndDate)
            tx.setIsPopUp(self._isPopUp)
            tx.setIsButtonDisabled(not self._canNavigate())
            tx.setDescriptionPlugin(self._DESCRIPTION_RESOURCE)
            tx.setBackgroundPlugin(self._BACKGROUND_RESOURCE)
            tx.setRewardImagePath(self.rewardImagePath)

    def _onClick(self):
        if self._canNavigate() and self._adventController.isAvailable():
            showAdventCalendarMainWindow()