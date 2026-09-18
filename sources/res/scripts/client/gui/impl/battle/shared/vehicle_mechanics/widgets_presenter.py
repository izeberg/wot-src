from __future__ import absolute_import
import typing
from future.utils import viewitems, viewvalues
from events_handler import eventHandler
from gui.battle_control.controllers.vehicle_passenger import hasVehiclePassengerCtrl, VehiclePassengerInfoWatcher
from gui.impl.pub.view_component import ViewComponent
from gui.veh_mechanics.battle.updaters.mechanics.tracked_mechanics_updater import IVehicleTrackedMechanicsView, VehicleTrackedMechanicsUpdater
from gui.veh_mechanics.battle.updaters.updaters_common import ViewUpdatersCollection
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
if typing.TYPE_CHECKING:
    from frameworks.wulf import ViewModel
    from items.vehicle_mechanics_types import VehicleMechanicKey
_WIDGET_ALIASES_BY_MECHANIC = {}

class VehicleMechanicsWidgetsPresenter(ViewComponent, VehiclePassengerInfoWatcher, IVehicleTrackedMechanicsView):
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self):
        super(VehicleMechanicsWidgetsPresenter, self).__init__()
        self.__updatersCollection = ViewUpdatersCollection()

    @eventHandler
    def onTrackedMechanicsUpdate(self, mechanics):
        trackedMechanics = set(mechanics)
        for mechanic, resIds in viewitems(_WIDGET_ALIASES_BY_MECHANIC):
            isTracked = mechanic in trackedMechanics
            for resId in resIds:
                child = self._getChild(resId)
                if child is None:
                    if isTracked:
                        self._constructChild(resId)
                else:
                    child.setEnabled(isTracked)

        return

    @property
    def viewModel(self):
        return super(VehicleMechanicsWidgetsPresenter, self).getViewModel()

    def _getChildComponents(self):
        return ()

    def _getEvents(self):
        vehicleCtrl = self.__sessionProvider.shared.vehicleState
        if vehicleCtrl is None:
            return ()
        else:
            return (
             (
              vehicleCtrl.onPostMortemSwitched, self.__onSwitchToPostmortem),)

    def _onLoaded(self, *args, **kwargs):
        super(VehicleMechanicsWidgetsPresenter, self)._onLoaded(*args, **kwargs)
        self.__updatersCollection.initialize([VehicleTrackedMechanicsUpdater(self)])
        self.startVehiclePassengerLateListening(self.__onVehicleControlling)

    def _finalize(self):
        self.stopVehiclePassengerListening(self.__onVehicleControlling)
        self.__updatersCollection.finalize()
        super(VehicleMechanicsWidgetsPresenter, self)._finalize()

    @hasVehiclePassengerCtrl()
    def __onVehicleControlling(self, _, passengerCtrl=None):
        pass

    def __onSwitchToPostmortem(self, _, __):
        for resIds in viewvalues(_WIDGET_ALIASES_BY_MECHANIC):
            for resId in resIds:
                child = self.getChildByPosId(resId)
                if child is not None:
                    child.setEnabled(False)

        return