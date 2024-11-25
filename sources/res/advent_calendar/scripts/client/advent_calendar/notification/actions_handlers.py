from advent_calendar.gui.shared.event_dispatcher import showAdventCalendarMainWindow
from notification.actions_handlers import NavigationDisabledActionHandler
from notification.settings import NOTIFICATION_TYPE

class AdventCalendarActionHandler(NavigationDisabledActionHandler):

    def doAction(self, model, entityID, action):
        showAdventCalendarMainWindow()

    @classmethod
    def getNotType(cls):
        return NOTIFICATION_TYPE.ADVENT_CALENDAR_DOORS_AVAILABLE

    @classmethod
    def getActions(cls):
        return ('showAdventCalendar', )