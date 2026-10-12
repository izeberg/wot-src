from __future__ import absolute_import
VEHICLE_RESPAWN_COMPONENT = 'VehicleRespawnComponent'

def getVehicleRespawnComponent(vehicle):
    return vehicle.dynamicComponents.get(VEHICLE_RESPAWN_COMPONENT)