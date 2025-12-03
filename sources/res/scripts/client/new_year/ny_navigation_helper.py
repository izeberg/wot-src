from adisp import adisp_process, isAsync
from gui.impl.new_year.navigation import NewYearNavigation
from gui.lootbox_system.base.common import Views, ViewID
from gui.shared import g_eventBus, EVENT_BUS_SCOPE
from gui.shared.event_dispatcher import showHolidayOpsMainView
from gui.shared.events import LobbySimpleEvent
from helpers import dependency
from skeletons.gui.shared.utils import IHangarSpace

def switchNewYearView(objectName, executeBeforeSwitch=None, **kwargs):
    ctx = {'objectName': objectName, 
       'executeBeforeSwitch': executeBeforeSwitch, 
       'kwargs': kwargs}
    g_eventBus.handleEvent(LobbySimpleEvent(LobbySimpleEvent.SWITCH_NEW_YEAR_VIEW, ctx), EVENT_BUS_SCOPE.LOBBY)


def showLootBox(lootBoxType):
    Views.load(ViewID.MAIN, eventName=lootBoxType)


class NewYearNavigationHelper(object):
    hangarSpace = dependency.descriptor(IHangarSpace)

    def onLobbyInited(self):
        g_eventBus.addListener(LobbySimpleEvent.SWITCH_NEW_YEAR_VIEW, self.__onSwitchEvent, EVENT_BUS_SCOPE.LOBBY)

    def clear(self):
        g_eventBus.removeListener(LobbySimpleEvent.SWITCH_NEW_YEAR_VIEW, self.__onSwitchEvent, EVENT_BUS_SCOPE.LOBBY)
        NewYearNavigation.clear()

    @staticmethod
    @adisp_process
    def __onSwitchEvent(event):
        ctx = event.ctx
        objectName = ctx.get('objectName')
        executeBeforeSwitch = ctx.get('executeBeforeSwitch')
        kwargs = ctx.get('kwargs', {})
        if objectName:
            if executeBeforeSwitch:
                if isAsync(executeBeforeSwitch):
                    execRes = yield executeBeforeSwitch()
                else:
                    execRes = executeBeforeSwitch()
                if not execRes:
                    return
            showHolidayOpsMainView(objectName=objectName, **kwargs)