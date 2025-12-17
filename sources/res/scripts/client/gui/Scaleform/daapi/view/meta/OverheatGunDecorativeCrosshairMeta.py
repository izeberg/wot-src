from gui.Scaleform.daapi.view.battle.shared.vehicle_mechanics.decorative_crosshairs.vehicle_decorative_crosshair import VehicleDecorativeCrosshair

class OverheatGunDecorativeCrosshairMeta(VehicleDecorativeCrosshair):

    def as_setProgressS(self, progress):
        if self._isDAAPIInited():
            return self.flashObject.as_setProgress(progress)

    def as_setSectionS(self, section):
        if self._isDAAPIInited():
            return self.flashObject.as_setSection(section)