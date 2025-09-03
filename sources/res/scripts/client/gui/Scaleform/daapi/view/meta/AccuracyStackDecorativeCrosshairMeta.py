from gui.Scaleform.daapi.view.battle.shared.vehicle_mechanics.decorative_crosshairs.vehicle_decorative_crosshair import VehicleDecorativeCrosshair

class AccuracyStackDecorativeCrosshairMeta(VehicleDecorativeCrosshair):

    def as_setInitDataS(self, maxStackCount, speedLimit):
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(maxStackCount, speedLimit)

    def as_setStacksProgresS(self, count, progress):
        if self._isDAAPIInited():
            return self.flashObject.as_setStacksProgres(count, progress)

    def as_setGainingActiveS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setGainingActive(value)

    def as_setSpeedLimitActiveS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setSpeedLimitActive(value)