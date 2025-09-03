from gui.Scaleform.daapi.view.battle.shared.vehicle_mechanics.decorative_crosshairs.vehicle_decorative_crosshair import VehicleDecorativeCrosshair

class FuryDecorativeCrosshairMeta(VehicleDecorativeCrosshair):

    def as_setGunStackProgressS(self, count, progress):
        if self._isDAAPIInited():
            return self.flashObject.as_setGunStackProgress(count, progress)