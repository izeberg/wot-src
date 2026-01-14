from __future__ import absolute_import
import typing
from vehicles.mechanics.mechanic_trackers.tracker_events import VehicleMechanicsTracker
from vehicles.mechanics.mechanic_trackers.tracker_interfaces import IVehicleMechanicsTracker, IVehicleMechanicsTrackerListener, IVehicleMechanicsTrackerListenerLogic
if typing.TYPE_CHECKING:
    from vehicles.mechanics.mechanic_constants import VehicleMechanic
__all__ = ('IVehicleMechanicsTracker', 'IVehicleMechanicsTrackerListener', 'IVehicleMechanicsTrackerListenerLogic',
           'createVehicleMechanicsTracker')

def createVehicleMechanicsTracker(trackedMechanics):
    return VehicleMechanicsTracker(trackedMechanics)