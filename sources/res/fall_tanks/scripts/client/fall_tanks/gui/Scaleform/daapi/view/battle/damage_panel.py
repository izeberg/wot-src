from __future__ import absolute_import
from gui.Scaleform.daapi.view.battle.shared.damage_panel import DamagePanel
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE

class FallTanksDamagePanel(DamagePanel):

    def _onVehicleStateUpdated(self, state, value):
        if state not in {VEHICLE_VIEW_STATE.DESTROYED, VEHICLE_VIEW_STATE.HEALTH}:
            super(FallTanksDamagePanel, self)._onVehicleStateUpdated(state, value)