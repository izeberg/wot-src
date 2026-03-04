from __future__ import absolute_import
from CurrentVehicle import g_currentVehicle

def isVehicleUnavailable():
    return g_currentVehicle.item.isInBattle or g_currentVehicle.item.isInPrebattle