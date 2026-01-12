from __future__ import absolute_import
from gui.Scaleform.daapi.view.meta.BaseDecorativeCrosshairMeta import BaseDecorativeCrosshairMeta
from gui.veh_mechanics.battle.updaters.mechanics.mechanic_passenger_updater import IMechanicPassengerView

class VehicleDecorativeCrosshair(BaseDecorativeCrosshairMeta, IMechanicPassengerView):

    def setVisibleForPassenger(self, visibleForPassenger):
        self.as_setVisibleS(visibleForPassenger)