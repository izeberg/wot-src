from __future__ import absolute_import
import typing, CGF
from constants import IS_EDITOR, IS_CGF_DUMP
if IS_EDITOR or IS_CGF_DUMP:

    class Vehicle(object):
        pass


else:
    from Vehicle import Vehicle

def getVehicleEntityByVehicleGameObject(vehicleGameObject):
    return vehicleGameObject.findWrite(Vehicle)


def tryActivateGameObject(gameObject):
    if not gameObject:
        return
    gameObject.activate()


def tryDeactivateGameObject(gameObject):
    if not gameObject:
        return
    gameObject.deactivate()