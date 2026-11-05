from __future__ import absolute_import
import uuid, BigWorld
from skeletons.gui.shared import IItemsCache
from gui.shared.utils.scheduled_notifications import SimpleNotifier
from account_helpers.AccountSettings import AdventCalendar
from advent_calendar.gui.feature.constants import ADVENT_CALENDAR_DOORS_AVAILABLE_NOTIFICATION_NAME, MIN_AVAILABLE_DOORS_REQUIRED_FOR_NOTIFICATION
from advent_calendar.gui.impl.gen.view_models.views.lobby.door_view_model import DoorState
from advent_calendar.gui.impl.gen.view_models.views.lobby.notifications.available_doors_view_model import State as AvailableDoorsNotificationState
from advent_calendar.gui.impl.lobby.feature.advent_helper import getAdventCalendarSetting, getDoorState, setAdventCalendarSetting
from advent_calendar.notification.decorators import DoorsAvailableDecorator
from advent_calendar.skeletons import IAdventCalendarController
from gui.shared.notifications import NotificationPriorityLevel
from helpers import dependency, time_utils
from notification.listeners import BaseReminderListener
from notification.settings import NOTIFICATION_TYPE, NotificationData

class DoorsAvailableListener(BaseReminderListener):
    _adventController = dependency.descriptor(IAdventCalendarController)
    _itemsCache = dependency.descriptor(IItemsCache)
    MSG_ID = 0
    _POPUP_NOTIFICATION_DELAY = 30

    def __init__(self):
        super(DoorsAvailableListener, self).__init__(NOTIFICATION_TYPE.ADVENT_CALENDAR_DOORS_AVAILABLE, self.MSG_ID)
        self._popUpNotificationCallbackID = None
        self._finalDayNotifier = None
        return

    def start(self, model):
        result = super(DoorsAvailableListener, self).start(model)
        self._tryNotify()
        self._adventController.onDoorOpened += self._tryNotify
        self._adventController.onDoorsStateChanged += self._tryNotify
        self._adventController.onConfigChanged += self._tryNotify
        return result

    def stop(self):
        super(DoorsAvailableListener, self).stop()
        self._adventController.onConfigChanged -= self._tryNotify
        self._adventController.onDoorsStateChanged -= self._tryNotify
        self._adventController.onDoorOpened -= self._tryNotify
        self._cancelPopUpNotificationCallback()
        self._stopFinalDayNotifier()

    def _createNotificationData(self, savedData, priorityLevel, **kwargs):
        return NotificationData(entityID=self._getNotificationId(), savedData=savedData, priorityLevel=priorityLevel, entity=None)

    def _createDecorator(self, data):
        return DoorsAvailableDecorator(self._getNotificationId(), self._model(), data, self._getNotificationName())

    def _tryNotify(self):
        if not self._adventController.isAvailable():
            self._notifyOrRemoveOrDelay(False)
            return
        availableDoorsAmount = len([ dayID for dayID in range(1, self._adventController.config.doorsCount + 1) if getDoorState(dayID) == DoorState.READY_TO_OPEN
                                   ])
        if not availableDoorsAmount:
            self._notifyOrRemoveOrDelay(False)
            return
        if self._adventController.isInPostActivePhase() and not self._isLastDayPostEvent():
            self._startFinalDayNotifier()
        state, canShowPopUp = self._getNotificationInfo(availableDoorsAmount)
        gfDataID = str(uuid.uuid4())
        data = {'state': state.value, 'gfDataID': gfDataID}
        priority = NotificationPriorityLevel.LOW
        if canShowPopUp:
            self._removeNotification()
            priority = NotificationPriorityLevel.HIGH
        self._notifyOrRemoveOrDelay(True, isStateChanged=canShowPopUp, isDelayed=True, priorityLevel=priority, savedData={'linkageData': data})

    def _notifyOrRemoveOrDelay(self, isAdding, isStateChanged=False, isDelayed=False, **ctx):
        if not isAdding:
            self._cancelPopUpNotificationCallback()
            self._stopFinalDayNotifier()
            self._notifyOrRemove(False)
            return
        if not isDelayed:
            self._notifyOrRemove(isAdding, isStateChanged=isStateChanged, **ctx)
            return

        def callback():
            self._popUpNotificationCallbackID = None
            self._notifyOrRemove(isAdding, isStateChanged=isStateChanged, **ctx)
            return

        self._cancelPopUpNotificationCallback()
        delay = self._getDelay()
        self._popUpNotificationCallbackID = BigWorld.callback(delay, callback)

    def _getNotificationInfo(self, availableDoorsAmount):
        canShowPopUp = False
        state = AvailableDoorsNotificationState.DOORS_AVAILABLE
        currentDay = self._adventController.getCurrentDayNumber()
        if self._adventController.isInPostActivePhase():
            state = AvailableDoorsNotificationState.POST_EVENT
            isFirstEntry = False
        else:
            firstEntryNTDay = getAdventCalendarSetting(AdventCalendar.FIRST_ENTRY_NOTIFICATION_SHOWING_DAY)
            if firstEntryNTDay < 0:
                setAdventCalendarSetting(AdventCalendar.FIRST_ENTRY_NOTIFICATION_SHOWING_DAY, currentDay)
                firstEntryNTDay = currentDay
            isFirstEntry = firstEntryNTDay == currentDay
            if isFirstEntry:
                state = AvailableDoorsNotificationState.FIRST_ENTRY
        isEnoughAvailableDoors = availableDoorsAmount >= MIN_AVAILABLE_DOORS_REQUIRED_FOR_NOTIFICATION
        if self._isFirstDayPostEvent() or self._isLastDayPostEvent() or isEnoughAvailableDoors or isFirstEntry:
            canShowPopUp = getAdventCalendarSetting(AdventCalendar.LAST_DAY_POPUP_SEEN) < currentDay
        return (state, canShowPopUp)

    def _isFirstDayPostEvent(self):
        startDate = self._adventController.postEventStartDate
        return startDate + time_utils.ONE_DAY > self._adventController.getCurrentTime > startDate

    def _getFinalDayDelta(self):
        return max(self._adventController.postEventEndDate - time_utils.ONE_DAY - self._adventController.getCurrentTime, 0)

    def _isLastDayPostEvent(self):
        endDate = self._adventController.postEventEndDate
        return endDate > self._adventController.getCurrentTime >= endDate - time_utils.ONE_DAY

    def _cancelPopUpNotificationCallback(self):
        if self._popUpNotificationCallbackID is not None:
            BigWorld.cancelCallback(self._popUpNotificationCallbackID)
            self._popUpNotificationCallbackID = None
        return

    def _startFinalDayNotifier(self):
        self._stopFinalDayNotifier()
        self._finalDayNotifier = SimpleNotifier(self._getFinalDayDelta, self._tryNotify)
        self._finalDayNotifier.startNotification()

    def _stopFinalDayNotifier(self):
        if self._finalDayNotifier:
            self._finalDayNotifier.stopNotification()
            self._finalDayNotifier.clear()
        self._finalDayNotifier = None
        return

    def _getDelay(self):
        return self._POPUP_NOTIFICATION_DELAY

    def _getNotificationName(self):
        return ADVENT_CALENDAR_DOORS_AVAILABLE_NOTIFICATION_NAME