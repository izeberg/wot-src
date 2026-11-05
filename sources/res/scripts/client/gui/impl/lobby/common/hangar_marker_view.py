from __future__ import absolute_import
from Event import Event
from frameworks.wulf import WindowLayer, WindowStatus
from frameworks_common.state_machine import BaseStateObserver
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.framework.entities.sf_window import SFWindow
from gui.Scaleform.genConsts.PREBATTLE_ALIASES import PREBATTLE_ALIASES
from gui.Scaleform.lobby_entry import getLobbyStateMachine
from gui.impl.pub import ViewImpl
from gui.lobby_state_machine.states import LobbyStateFlags
from gui.prb_control.dispatcher import g_prbLoader
from gui.prb_control.entities.maps_training.pre_queue.entity import MapsTrainingEntity
from helpers import dependency
from skeletons.gui.impl import IGuiLoader

class HangarMarkerStatesObserver(BaseStateObserver):

    def __init__(self):
        super(HangarMarkerStatesObserver, self).__init__()
        self._state = None
        self.onMarkerState = Event()
        return

    def isObservingState(self, state):
        return state.getFlags() & LobbyStateFlags.HANGAR

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


class HangarMarkerView(ViewImpl):
    __guiLoader = dependency.descriptor(IGuiLoader)
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
    __UPDATING_WINDOW_STATUSES = (WindowStatus.LOADING, WindowStatus.LOADED, WindowStatus.DESTROYING)

    def __init__(self, settings):
        self._statesObserver = self._createStatesObserver()
        super(HangarMarkerView, self).__init__(settings)

    @property
    def viewModel(self):
        return self.getViewModel()

    def _createStatesObserver(self):
        return HangarMarkerStatesObserver()

    def _getEvents(self):
        return super(HangarMarkerView, self)._getEvents() + (
         (
          self.__guiLoader.windowsManager.onWindowStatusChanged, self.__onWindowStatusChanged),
         (
          self._statesObserver.onMarkerState, self._updateMarkerVisibility))

    def _onLoading(self, *args, **kwargs):
        super(HangarMarkerView, self)._onLoading(*args, **kwargs)
        lsm = getLobbyStateMachine()
        if lsm is not None:
            lsm.connect(self._statesObserver)
        self._updateMarkerVisibility()
        self._updateMarker()
        return

    def _finalize(self):
        super(HangarMarkerView, self)._finalize()
        lsm = getLobbyStateMachine()
        if lsm is not None:
            lsm.disconnect(self._statesObserver)
        self._statesObserver.clear()
        self._statesObserver = None
        return

    def _canShowMarkers(self):
        if self._statesObserver.currentState is None:
            return False
        else:
            windowsManager = self.__guiLoader.windowsManager
            dispatcher = g_prbLoader.getDispatcher()
            blockedByGameMode = issubclass(type(dispatcher.getEntity()), (MapsTrainingEntity,))
            blockedByWindow = len(windowsManager.findWindows(lambda w: w.layer in self.__LAYERS_WITHOUT_MARKERS and w.windowStatus in self.__ACTIVE_WINDOW_STATUSES)) > 0
            blockedByAlias = len(windowsManager.findWindows(lambda w: w.layer == WindowLayer.SUB_VIEW and w.windowStatus in self.__ACTIVE_WINDOW_STATUSES and isinstance(w, SFWindow) and w.loadParams.viewKey.alias in self.__ALIASES_WITHOUT_MARKERS)) > 0
            return not (blockedByWindow or blockedByAlias or blockedByGameMode)

    def _setMarkerVisible(self, isVisible):
        if self.viewModel.getIsVisible() == isVisible:
            return
        with self.viewModel.transaction() as (model):
            model.setIsVisible(isVisible)
            if isVisible:
                self._updateMarker()

    def _updateMarker(self, *args, **kwargs):
        pass

    def _updateMarkerVisibility(self, *args, **kwargs):
        self._setMarkerVisible(self._canShowMarkers())

    def __onWindowStatusChanged(self, uniqueID, newStatus):
        if newStatus in self.__UPDATING_WINDOW_STATUSES:
            self._updateMarkerVisibility()