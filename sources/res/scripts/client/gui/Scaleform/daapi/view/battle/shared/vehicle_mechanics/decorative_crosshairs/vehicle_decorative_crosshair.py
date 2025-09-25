from gui.Scaleform.daapi.view.meta.BaseDecorativeCrosshairMeta import BaseDecorativeCrosshairMeta
from gui.veh_mechanics.battle.updaters.mechanic_passenger_view_updater import IMechanicPassengerView

class VehicleDecorativeCrosshair(BaseDecorativeCrosshairMeta, IMechanicPassengerView):

    def setVisible(self, visible):
        self.as_setVisibleS(visible)