from __future__ import absolute_import
from items.vehicles import VehicleDescr

def getVehicleLevel(vType):
    descriptor = VehicleDescr(compactDescr=vType.strCompactDescr)
    return max(descriptor.chassis.level, descriptor.turret.level, descriptor.gun.level, descriptor.radio.level, descriptor.engine.level)