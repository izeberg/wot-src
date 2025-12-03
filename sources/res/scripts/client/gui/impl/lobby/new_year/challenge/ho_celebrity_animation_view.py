from frameworks.wulf import ViewSettings, WindowLayer
from gui.impl.pub import ViewImpl
from gui.impl.gen import R
from gui.impl.pub.lobby_window import LobbyNotificationWindow
from gui.impl.new_year.navigation import NewYearNavigation
from frameworks.wulf import ViewModel
from gui.impl.lobby.new_year.observers import HolidayOpsObjectStateObserver
from gui.shared import EVENT_BUS_SCOPE, g_eventBus
from gui.shared.events import NyCelebrityAnimationEvent, NyGladeVisibilityEvent
from skeletons.gui.app_loader import IAppLoader
from skeletons.gui.shared.utils import IHangarSpace
from helpers import dependency
from gui.Scaleform.lobby_entry import getLobbyStateMachine
_CHANGE_LAYERS_VISIBILITY = (WindowLayer.VIEW, WindowLayer.WINDOW, WindowLayer.MARKER)

class HOCelebrityAnimationView(ViewImpl):
    _hangarSpace = dependency.descriptor(IHangarSpace)
    __appLoader = dependency.instance(IAppLoader)

    def __init__(self, justReceived, previewType):
        settings = ViewSettings(R.views.mono.holiday_ops.celebrity_animation_view())
        settings.model = ViewModel()
        self.__objectObserver = HolidayOpsObjectStateObserver()
        self.__justReceived = justReceived
        self.__previewType = previewType
        super(HOCelebrityAnimationView, self).__init__(settings)

    def _getListeners(self):
        listeners = super(HOCelebrityAnimationView, self)._getListeners()
        return listeners + (
         (
          NyCelebrityAnimationEvent.CLOSE_ANIMATION_VIEW, self.__handleCloseView, EVENT_BUS_SCOPE.DEFAULT),)

    def _initialize(self):
        super(HOCelebrityAnimationView, self)._initialize()
        self._hangarSpace.setSelectionEnabled(False)
        self.__changeLayersVisibility(True, _CHANGE_LAYERS_VISIBILITY)
        lsm = getLobbyStateMachine()
        lsm.connect(self.__objectObserver)
        self.__objectObserver.onObjectStateChanged += self.__onNavigation

    def _onLoaded(self, *args, **kwargs):
        super(HOCelebrityAnimationView, self)._onLoaded(args, kwargs)
        g_eventBus.handleEvent(NyGladeVisibilityEvent(eventType=NyGladeVisibilityEvent.START_FADE_IN), scope=EVENT_BUS_SCOPE.DEFAULT)
        if not NewYearNavigation.getCurrentObject():
            self.destroyWindow()

    def _finalize(self):
        self._hangarSpace.setSelectionEnabled(True)
        g_eventBus.handleEvent(NyGladeVisibilityEvent(eventType=NyGladeVisibilityEvent.START_FADE_OUT), scope=EVENT_BUS_SCOPE.DEFAULT)
        g_eventBus.handleEvent(NyCelebrityAnimationEvent(eventType=NyCelebrityAnimationEvent.ANIMATION_VIEW_CLOSED, ctx={'justReceived': self.__justReceived, 'previewType': self.__previewType}), scope=EVENT_BUS_SCOPE.DEFAULT)
        self.__changeLayersVisibility(False, _CHANGE_LAYERS_VISIBILITY)
        self.__objectObserver.onObjectStateChanged -= self.__onNavigation
        lsm = getLobbyStateMachine()
        lsm.disconnect(self.__objectObserver)
        self.__objectObserver.clear()
        self.__objectObserver = None
        super(HOCelebrityAnimationView, self)._finalize()
        return

    def __handleCloseView(self, _):
        self.destroyWindow()

    def __onNavigation(self, _):
        self.destroyWindow()

    def __changeLayersVisibility(self, isHide, layers):
        lobby = self.__appLoader.getDefLobbyApp()
        if lobby:
            if isHide:
                lobby.containerManager.hideContainers(layers, time=0.3)
            else:
                lobby.containerManager.showContainers(layers, time=0.3)
            self.__appLoader.getApp().graphicsOptimizationManager.switchOptimizationEnabled(not isHide)


class HOCelebrityAnimationWindow(LobbyNotificationWindow):
    __slots__ = ()

    def __init__(self, justReceived=None, previewType=None, parent=None):
        super(HOCelebrityAnimationWindow, self).__init__(content=HOCelebrityAnimationView(justReceived, previewType), parent=parent, layer=WindowLayer.FULLSCREEN_WINDOW)