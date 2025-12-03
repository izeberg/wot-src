from Event import Event
from frameworks.state_machine import BaseStateObserver
from frameworks.wulf import WindowLayer, WindowStatus, ViewFlags
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.genConsts.PREBATTLE_ALIASES import PREBATTLE_ALIASES
from gui.Scaleform.framework.entities.sf_window import SFWindow
from gui.Scaleform.lobby_entry import getLobbyStateMachine
from gui.impl.lobby.hangar.states import HangarState, DefaultHangarState
from gui.impl.lobby.new_year.observers import HolidayOpsObjectStateObserver
from gui.impl.lobby.new_year.states import GladeState, FriendsState, RewardsState, FriendGladeState
from gui.impl.pub import ViewImpl
from gui.prb_control.dispatcher import g_prbLoader
from gui.prb_control.entities.maps_training.pre_queue.entity import MapsTrainingEntity
from helpers import dependency
from skeletons.account_helpers.settings_core import ISettingsCore
from skeletons.gui.impl import IGuiLoader
from skeletons.new_year import INewYearController
_ALLOWED_STATES = {
 GladeState.STATE_ID,
 FriendsState.STATE_ID,
 RewardsState.STATE_ID,
 FriendGladeState.STATE_ID,
 HangarState.STATE_ID,
 DefaultHangarState.STATE_ID}

class HangarMarkerStatesObserver(BaseStateObserver):

    def __init__(self):
        super(HangarMarkerStatesObserver, self).__init__()
        self._state = None
        self.onMarkerState = Event()
        return

    def isObservingState(self, state):
        allowed = state.getStateID() in _ALLOWED_STATES
        return allowed

    def onEnterState(self, state, event):
        self._state = state
        self.onMarkerState()

    def onExitState(self, state, event):
        self._state = None
        self.onMarkerState()
        return

    @property
    def currentState(self):
        return self._state


class HOHangarMarkerView(ViewImpl):
    __guiLoader = dependency.descriptor(IGuiLoader)
    _settingsCore = dependency.descriptor(ISettingsCore)
    _nyController = dependency.descriptor(INewYearController)
    __LAYERS_WITHOUT_MARKERS = {
     WindowLayer.FULLSCREEN_WINDOW,
     WindowLayer.OVERLAY,
     WindowLayer.TOP_SUB_VIEW}
    __ALIASES_WITHOUT_MARKERS = {
     PREBATTLE_ALIASES.TRAINING_LIST_VIEW_PY,
     PREBATTLE_ALIASES.TRAINING_ROOM_VIEW_PY,
     PREBATTLE_ALIASES.EPICBATTLE_LIST_VIEW_PY,
     PREBATTLE_ALIASES.EPIC_TRAINING_ROOM_VIEW_PY,
     VIEW_ALIAS.BATTLE_QUEUE,
     VIEW_ALIAS.BATTLE_STRONGHOLDS_QUEUE,
     VIEW_ALIAS.LOBBY_CUSTOMIZATION,
     VIEW_ALIAS.STYLE_PREVIEW,
     VIEW_ALIAS.VEHICLE_PREVIEW,
     VIEW_ALIAS.HERO_VEHICLE_PREVIEW}
    __ACTIVE_WINDOW_STATUSES = (
     WindowStatus.LOADING, WindowStatus.LOADED)

    def __init__(self, settings):
        settings.flags = ViewFlags.VIEW
        self._objectObserver = HolidayOpsObjectStateObserver()
        self._statesObserver = HangarMarkerStatesObserver()
        super(HOHangarMarkerView, self).__init__(settings)

    def _onLoading(self, *args, **kwargs):
        super(HOHangarMarkerView, self)._onLoading(*args, **kwargs)
        self._updateMarkerVisibility()
        self.__guiLoader.windowsManager.onWindowStatusChanged += self.__onWindowStatusChanged
        self._nyController.onStateChanged += self._updateMarkerVisibility
        lsm = getLobbyStateMachine()
        lsm.connect(self._objectObserver)
        lsm.connect(self._statesObserver)
        self._objectObserver.onObjectStateChanged += self._updateMarkerVisibility
        self._statesObserver.onMarkerState += self._updateMarkerVisibility

    def _finalize(self):
        super(HOHangarMarkerView, self)._finalize()
        self.__guiLoader.windowsManager.onWindowStatusChanged -= self.__onWindowStatusChanged
        self._nyController.onStateChanged -= self._updateMarkerVisibility
        self._objectObserver.onObjectStateChanged -= self._updateMarkerVisibility
        lsm = getLobbyStateMachine()
        lsm.disconnect(self._objectObserver)
        lsm.disconnect(self._statesObserver)
        self._objectObserver.clear()
        self._statesObserver.clear()
        self._objectObserver = None
        self._statesObserver = None
        return

    def _setMarkerVisible(self, value):
        pass

    def _canShowMarkers(self):
        if not self._nyController.isEnabled():
            return False
        windowsManager = self.__guiLoader.windowsManager
        dispatcher = g_prbLoader.getDispatcher()
        blockedByGameMode = issubclass(type(dispatcher.getEntity()), (MapsTrainingEntity,))
        blockedByWindow = len(windowsManager.findWindows(lambda w: w.layer in self.__LAYERS_WITHOUT_MARKERS and w.windowStatus in self.__ACTIVE_WINDOW_STATUSES)) > 0
        blockedByAlias = len(windowsManager.findWindows(lambda w: w.layer == WindowLayer.SUB_VIEW and w.windowStatus in self.__ACTIVE_WINDOW_STATUSES and isinstance(w, SFWindow) and w.loadParams.viewKey.alias in self.__ALIASES_WITHOUT_MARKERS)) > 0
        if self._statesObserver.currentState:
            return not blockedByWindow and not blockedByAlias and not blockedByGameMode
        return False

    def _updateMarkerVisibility(self, *args, **kwargs):
        self._setMarkerVisible(self._canShowMarkers())

    def __onWindowStatusChanged(self, uniqueID, newStatus):
        if newStatus in (WindowStatus.LOADING, WindowStatus.LOADED, WindowStatus.DESTROYING):
            self._updateMarkerVisibility()