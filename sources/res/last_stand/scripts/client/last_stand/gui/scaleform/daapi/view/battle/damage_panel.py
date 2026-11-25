from __future__ import absolute_import
from gui.battle_control.arena_info.settings import INVALIDATE_OP
from gui.Scaleform.daapi.view.battle.shared.damage_panel import DamagePanel

class LSDamagePanel(DamagePanel):

    def updateVehiclesInfo(self, updated, arenaDP):
        updated = [ item for item in updated if item[0] & INVALIDATE_OP.VEHICLE_INFO ]
        if updated:
            super(LSDamagePanel, self).updateVehiclesInfo(updated, arenaDP)