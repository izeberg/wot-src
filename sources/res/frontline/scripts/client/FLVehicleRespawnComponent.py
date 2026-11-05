from __future__ import absolute_import
from VehicleRespawnComponent import VehicleRespawnComponent
from helpers.EffectsList import RespawnDestroyEffect

class FLVehicleRespawnComponent(VehicleRespawnComponent):

    def _explodeVehicleBeforeRespawn(self):
        RespawnDestroyEffect.play(self.entity.id)
        self.entity.stopGUIVisual()