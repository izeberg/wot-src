from __future__ import absolute_import
import CGF
from cgf_modules import game_events

def postVehicleShotEvent(entityGo, gunGO, gunIndex, shellType):
    CGF.postEvent(entityGo.spaceID, game_events.VehicleShotEvent(entityGo=entityGo, gunGo=gunGO, gunIndex=gunIndex, shellType=shellType))