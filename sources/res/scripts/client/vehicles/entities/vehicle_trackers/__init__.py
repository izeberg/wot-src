from __future__ import absolute_import
from constants import UNKNOWN_VEHICLE_ID
from vehicles.entities.vehicle_trackers.events import VehicleEntityTracker
from vehicles.entities.vehicle_trackers.interfaces import IVehicleEntityTracker, IVehicleEntityTrackerListener, IVehicleEntityTrackerListenerLogic
__all__ = ('IVehicleEntityTracker', 'IVehicleEntityTrackerListener', 'IVehicleEntityTrackerListenerLogic',
           'createVehicleEntityTracker')

def createVehicleEntityTracker(vehicleID=UNKNOWN_VEHICLE_ID):
    return VehicleEntityTracker(vehicleID)