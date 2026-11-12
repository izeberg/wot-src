from gui.shared import EVENT_BUS_SCOPE, events, g_eventBus
from helpers import dependency
from skeletons.gui.impl import IGuiLoader
from frameworks.wulf import ViewStatus
HEADER_IS_VISIBLE = 'headerIsVisible'
MESSENGER_BAR_VISIBLE = 'messengerBarVisible'
IGNORE_TOP_OFFSET = 'ignoreTopOffset'
IS_ACTIVE = 'isActive'
VIEW_ID = 'viewId'

class LobbyViewPartsVisibilityHelper(object):
    __gui = dependency.descriptor(IGuiLoader)
    __slots__ = ('__activeViewCtx', '__lobbyView')

    def __init__(self, lobbyView):
        super(LobbyViewPartsVisibilityHelper, self).__init__()
        self.__activeViewCtx = None
        self.__lobbyView = lobbyView
        g_eventBus.addListener(events.LobbyInterfaceEvent.TOGGLE_VISIBILITY, self.__onToggleVisibility, scope=EVENT_BUS_SCOPE.LOBBY)
        self.__gui.windowsManager.onViewStatusChanged += self.__onViewStatusChanged
        return

    def dispose(self):
        self.__lobbyView = None
        g_eventBus.removeListener(events.LobbyInterfaceEvent.TOGGLE_VISIBILITY, self.__onToggleVisibility, scope=EVENT_BUS_SCOPE.LOBBY)
        self.__gui.windowsManager.onViewStatusChanged -= self.__onViewStatusChanged
        return

    def __onViewStatusChanged(self, uniqueId, newStatus):
        if self.__activeViewCtx and self.__activeViewCtx['viewId'] == uniqueId and newStatus == ViewStatus.DESTROYING:
            self.__activeViewCtx = None
        return

    def __onToggleVisibility(self, event):
        eventCtx = event.ctx
        isActive = eventCtx[IS_ACTIVE]
        viewId = eventCtx[VIEW_ID]
        if isActive:
            self.__activeViewCtx = eventCtx
        elif self.__activeViewCtx:
            eventCtx = self.__activeViewCtx
        headerIsVisible = eventCtx[HEADER_IS_VISIBLE]
        messengerBarVisible = eventCtx[MESSENGER_BAR_VISIBLE]
        ignoreTopOffset = eventCtx[IGNORE_TOP_OFFSET]
        self.__lobbyView.as_setInterfaceVisibleS({'headerIsVisible': headerIsVisible, 
           'messengerBarVisible': messengerBarVisible, 
           'ignoreTopOffset': ignoreTopOffset})


def handleLobbyPartsVisibilityEvent(headerIsVisible=True, messengerBarVisible=True, ignoreTopOffset=False, isActive=False, viewId=0):
    eventCtx = {HEADER_IS_VISIBLE: headerIsVisible, 
       MESSENGER_BAR_VISIBLE: messengerBarVisible, 
       IGNORE_TOP_OFFSET: ignoreTopOffset, 
       IS_ACTIVE: isActive, 
       VIEW_ID: viewId}
    g_eventBus.handleEvent(events.LobbyInterfaceEvent(events.LobbyInterfaceEvent.TOGGLE_VISIBILITY, ctx=eventCtx), EVENT_BUS_SCOPE.LOBBY)