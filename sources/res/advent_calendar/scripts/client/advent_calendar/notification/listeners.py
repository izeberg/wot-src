from __future__ import absolute_import
import uuid, BigWorld
from account_helpers.AccountSettings import AdventCalendar
from advent_calendar.gui.feature.constants import MIN_AVAILABLE_DOORS_REQUIRED_FOR_NOTIFICATION
from advent_calendar.gui.impl.gen.view_models.views.lobby.door_view_model import DoorState
from advent_calendar.gui.impl.gen.view_models.views.lobby.notifications.available_doors_view_model import State as AvailableDoorsNotificationState
from advent_calendar.gui.impl.lobby.feature.advent_helper import getDoorState, getAdventCalendarSetting, setAdventCalendarSetting
from advent_calendar.notification.decorators import AdventCalendarDoorsAvailableDecorator
from advent_calendar.skeletons import IAdventCalendarController
from gui.shared import g_eventBus, EVENT_BUS_SCOPE, events
from gui.shared.notifications import NotificationPriorityLevel
from helpers import dependency, time_utils
from notification.listeners import BaseReminderListener
from notification.settings import NOTIFICATION_TYPE, NotificationData
from skeletons.gui.shared import IItemsCache
from skeletons.new_year import INewYearController

class AdventCalendarDoorsAvailableListener(BaseReminderListener):
    __adventController = dependency.descriptor(IAdventCalendarController)
    __itemsCache = dependency.descriptor(IItemsCache)
    __nyController = dependency.descriptor(INewYearController)
    MSG_ID = 0
    POPUP_NOTIFICATION_DELAY = 30
    POPUP_NOTIFICATION_DELAY_WITH_HO = 90

    def __init__(self):
        super(AdventCalendarDoorsAvailableListener, self).__init__(NOTIFICATION_TYPE.ADVENT_CALENDAR_DOORS_AVAILABLE, self.MSG_ID)
        self.__popUpNotificationCallbackID = None
        return

    def start(self, model):
        result = super(AdventCalendarDoorsAvailableListener, self).start(model)
        self.__tryNotify()
        self.__adventController.onDoorOpened += self.__tryNotify
        self.__adventController.onDoorsStateChanged += self.__tryNotify
        self.__adventController.onConfigChanged += self.__tryNotify
        g_eventBus.addListener(events.NyInitialNotificationEvent.INITIAL_NOTIFICATION_SHOWN, self.__onNyInitialNotificationShown, EVENT_BUS_SCOPE.LOBBY)
        return result

    def stop(self):
        super(AdventCalendarDoorsAvailableListener, self).stop()
        g_eventBus.removeListener(events.NyInitialNotificationEvent.INITIAL_NOTIFICATION_SHOWN, self.__onNyInitialNotificationShown, EVENT_BUS_SCOPE.LOBBY)
        self.__adventController.onConfigChanged -= self.__tryNotify
        self.__adventController.onDoorsStateChanged -= self.__tryNotify
        self.__adventController.onDoorOpened -= self.__tryNotify
        self.__cancelPopUpNotificationCallback()

    def _createNotificationData(self, savedData, priorityLevel, **kwargs):
        return NotificationData(entityID=self._getNotificationId(), savedData=savedData, priorityLevel=priorityLevel, entity=None)

    def _createDecorator(self, notificationData):
        return AdventCalendarDoorsAvailableDecorator(self._getNotificationId(), self._model(), notificationData)

    def __tryNotify(self):
        if not self.__adventController.isAvailable():
            return self.__notifyOrRemoveOrDelay(False)
        availableDoorsAmount = len([ dayID for dayID in range(1, self.__adventController.config.doorsCount + 1) if getDoorState(dayID) == DoorState.READY_TO_OPEN
                                   ])
        if not availableDoorsAmount:
            self.__notifyOrRemoveOrDelay(False)
            return
        state, canShowPopUp = self.__getNotificationInfo(availableDoorsAmount)
        gfDataID = str(uuid.uuid4())
        data = {'state': state.value, 'gfDataID': gfDataID}
        priority = NotificationPriorityLevel.LOW
        if canShowPopUp:
            self._removeNotification()
            priority = NotificationPriorityLevel.HIGH
        self.__notifyOrRemoveOrDelay(True, isStateChanged=canShowPopUp, isDelayed=True, priorityLevel=priority, savedData={'linkageData': data})

    def __notifyOrRemoveOrDelay(self, isAdding, isStateChanged=False, isDelayed=False, **ctx):
        if not isAdding:
            self.__cancelPopUpNotificationCallback()
            self._notifyOrRemove(False)
            return
        if not isDelayed:
            self._notifyOrRemove(isAdding, isStateChanged=isStateChanged, **ctx)
            return

        def callback():
            self.__popUpNotificationCallbackID = None
            self._notifyOrRemove(isAdding, isStateChanged=isStateChanged, **ctx)
            return

        self.__cancelPopUpNotificationCallback()
        delay = self.POPUP_NOTIFICATION_DELAY_WITH_HO if self.__adventController.isNYEntryPointStarted else self.POPUP_NOTIFICATION_DELAY
        self.__popUpNotificationCallbackID = BigWorld.callback(delay, callback)

    def __getNotificationInfo(self, availableDoorsAmount):
        currentDay = self.__adventController.getCurrentDayNumber()
        firstEntryNTDay = getAdventCalendarSetting(AdventCalendar.FIRST_ENTRY_NOTIFICATION_SHOWING_DAY)
        if firstEntryNTDay < 0:
            setAdventCalendarSetting(AdventCalendar.FIRST_ENTRY_NOTIFICATION_SHOWING_DAY, currentDay)
            firstEntryNTDay = currentDay
        isPopUpSeenToday = getAdventCalendarSetting(AdventCalendar.LAST_DAY_POPUP_SEEN) == currentDay
        if self.__adventController.isInPostActivePhase():
            isSpecialPostEventDay = self.__isFirstDayPostEvent() or self.__isLastDayPostEvent()
            canShowPopUp = isSpecialPostEventDay and not isPopUpSeenToday
            return (
             AvailableDoorsNotificationState.POST_EVENT, canShowPopUp)
        if firstEntryNTDay == currentDay:
            return (AvailableDoorsNotificationState.FIRST_ENTRY, not isPopUpSeenToday)
        isEnoughAvailableDoors = availableDoorsAmount >= MIN_AVAILABLE_DOORS_REQUIRED_FOR_NOTIFICATION
        return (AvailableDoorsNotificationState.DOORS_AVAILABLE, isEnoughAvailableDoors and not isPopUpSeenToday)

    def __isFirstDayPostEvent(self):
        startDate = self.__adventController.postEventStartDate
        return startDate + time_utils.ONE_DAY > self.__adventController.getCurrentTime > startDate

    def __isLastDayPostEvent(self):
        endDate = self.__adventController.postEventEndDate
        return endDate > self.__adventController.getCurrentTime > endDate - time_utils.ONE_DAY

    def __onNyInitialNotificationShown(self, _):
        self.__tryNotify()

    def __cancelPopUpNotificationCallback(self):
        if self.__popUpNotificationCallbackID is not None:
            BigWorld.cancelCallback(self.__popUpNotificationCallbackID)
            self.__popUpNotificationCallbackID = None
        return