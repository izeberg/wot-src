from __future__ import absolute_import
from frameworks.wulf import ViewSettings
from advent_calendar.gui.impl.gen.view_models.views.lobby.door_view_model import DoorState
from advent_calendar.gui.impl.gen.view_models.views.lobby.marker_view_model import MarkerViewModel
from advent_calendar.gui.impl.lobby.feature.advent_helper import getDoorState
from advent_calendar.skeletons.game_controller import IAdventCalendarController
from gui.impl.gen import R
from gui.impl.lobby.common.hangar_marker_view import HangarMarkerView
from helpers import dependency

class MarkerView(HangarMarkerView):
    _adventController = dependency.descriptor(IAdventCalendarController)

    def __init__(self, *args, **kwargs):
        settings = ViewSettings(R.views.advent_calendar.mono.lobby.markers.entry_point_marker(), model=MarkerViewModel(), args=args, kwargs=kwargs)
        super(MarkerView, self).__init__(settings)

    @property
    def viewModel(self):
        return self.getViewModel()

    def _getEvents(self):
        return super(MarkerView, self)._getEvents() + (
         (
          self._adventController.onDoorOpened, self._updateMarker),
         (
          self._adventController.onConfigChanged, self._updateMarker),
         (
          self._adventController.onDoorsStateChanged, self._updateMarker))

    def _isVisible(self, doorsToOpenAmount):
        return bool(doorsToOpenAmount) and self._adventController.isAvailable() and self._canShowMarkers()

    def _isAnimationEnabled(self):
        return self._adventController.isInActivePhase()

    def _updateMarker(self, *args, **kwargs):
        doorsToOpenAmount = self._getAvailableDoorsToOpenAmount()
        with self.viewModel.transaction() as (model):
            model.setIsVisible(self._isVisible(doorsToOpenAmount))
            model.setIsAnimationEnabled(self._isAnimationEnabled())
            model.setAvailableDoorsAmount(doorsToOpenAmount)
            model.setIsPostEvent(self._adventController.isInPostActivePhase() or self._adventController.isFirstEventDay())

    def _getAvailableDoorsToOpenAmount(self):
        return len([ doorId for doorId in range(0, self._adventController.config.doorsCount + 1) if getDoorState(doorId + 1) == DoorState.READY_TO_OPEN
                   ])