from __future__ import absolute_import
from advent_calendar.gui.impl.gen.view_models.views.lobby.door_view_model import DoorState
from advent_calendar.gui.impl.gen.view_models.views.lobby.marker_view_model import MarkerViewModel
from advent_calendar.gui.impl.lobby.feature.advent_helper import getDoorState
from advent_calendar.skeletons.game_controller import IAdventCalendarController
from frameworks.wulf import ViewSettings
from frameworks.wulf import WindowLayer, WindowStatus
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.framework.entities.sf_window import SFWindow
from gui.Scaleform.genConsts.PREBATTLE_ALIASES import PREBATTLE_ALIASES
from gui.impl.gen import R
from gui.impl.pub import ViewImpl
from gui.prb_control.dispatcher import g_prbLoader
from gui.prb_control.entities.maps_training.pre_queue.entity import MapsTrainingEntity
from helpers import dependency, time_utils
from skeletons.account_helpers.settings_core import ISettingsCore
from skeletons.gui.impl import IGuiLoader

class ACHangarMarkerView(ViewImpl):
    __guiLoader = dependency.descriptor(IGuiLoader)
    _settingsCore = dependency.descriptor(ISettingsCore)
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
     VIEW_ALIAS.LOBBY_CUSTOMIZATION,
     VIEW_ALIAS.STYLE_PREVIEW,
     VIEW_ALIAS.VEHICLE_PREVIEW,
     VIEW_ALIAS.HERO_VEHICLE_PREVIEW}
    __ACTIVE_WINDOW_STATUSES = (
     WindowStatus.LOADING, WindowStatus.LOADED)

    def _onLoading(self, *args, **kwargs):
        super(ACHangarMarkerView, self)._onLoading(*args, **kwargs)
        self._updateMarkerVisibility()
        self.__guiLoader.windowsManager.onWindowStatusChanged += self.__onWindowStatusChanged

    def _finalize(self):
        super(ACHangarMarkerView, self)._finalize()
        self.__guiLoader.windowsManager.onWindowStatusChanged -= self.__onWindowStatusChanged

    def _setMarkerVisible(self, value):
        pass

    def _canShowMarkers(self):
        windowsManager = self.__guiLoader.windowsManager
        dispatcher = g_prbLoader.getDispatcher()
        blockedByGameMode = issubclass(type(dispatcher.getEntity()), (MapsTrainingEntity,))
        blockedByWindow = len(windowsManager.findWindows(lambda w: w.layer in self.__LAYERS_WITHOUT_MARKERS and w.windowStatus in self.__ACTIVE_WINDOW_STATUSES)) > 0
        blockedByAlias = len(windowsManager.findWindows(lambda w: w.layer == WindowLayer.SUB_VIEW and w.windowStatus in self.__ACTIVE_WINDOW_STATUSES and isinstance(w, SFWindow) and w.loadParams.viewKey.alias in self.__ALIASES_WITHOUT_MARKERS)) > 0
        return not blockedByWindow and not blockedByAlias and not blockedByGameMode

    def _updateMarkerVisibility(self, *args, **kwargs):
        self._setMarkerVisible(self._canShowMarkers())

    def __onWindowStatusChanged(self, uniqueID, newStatus):
        if newStatus in (WindowStatus.LOADING, WindowStatus.LOADED, WindowStatus.DESTROYING):
            self._updateMarkerVisibility()


class MarkerView(ACHangarMarkerView):
    __adventController = dependency.descriptor(IAdventCalendarController)

    def __init__(self, *args, **kwargs):
        settings = ViewSettings(R.views.advent_calendar.mono.lobby.markers.entry_point_marker(), model=MarkerViewModel(), args=args, kwargs=kwargs)
        super(MarkerView, self).__init__(settings)

    @property
    def viewModel(self):
        return self.getViewModel()

    def _onLoading(self, *args, **kwargs):
        super(MarkerView, self)._onLoading(*args, **kwargs)
        self.__updateMarker()

    def _getEvents(self):
        events = super(MarkerView, self)._getEvents()
        return events + (
         (
          self.__adventController.onDoorOpened, self.__updateMarker),
         (
          self.__adventController.onConfigChanged, self.__updateMarker),
         (
          self.__adventController.onDoorsStateChanged, self.__updateMarker))

    def _setMarkerVisible(self, isVisible):
        with self.viewModel.transaction() as (model):
            if model.getIsVisible() != isVisible:
                model.setIsVisible(isVisible)
                if isVisible:
                    self.__updateMarker()

    def __updateMarker(self, *args, **kwargs):
        doorsToOpenAmount = self.__getAvailableDoorsToOpenAmount()
        with self.viewModel.transaction() as (model):
            model.setIsVisible(doorsToOpenAmount and self.__adventController.isAvailable() and self._canShowMarkers())
            model.setIsAnimationEnabled(True)
            model.setAvailableDoorsAmount(doorsToOpenAmount)
            model.setIsPostEvent(self.__adventController.isInPostActivePhase() or self.__isFirstEventDay())

    def __getAvailableDoorsToOpenAmount(self):
        return len([ doorId for doorId in range(0, self.__adventController.config.doorsCount + 1) if getDoorState(doorId + 1) == DoorState.READY_TO_OPEN
                   ])

    def __isFirstEventDay(self):
        return 0 < time_utils.getServerUTCTime() - self.__adventController.config.startDate < time_utils.ONE_DAY