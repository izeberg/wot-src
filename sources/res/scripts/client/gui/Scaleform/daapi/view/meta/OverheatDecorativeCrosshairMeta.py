from gui.Scaleform.daapi.view.battle.shared.vehicle_mechanics.decorative_crosshairs.vehicle_decorative_crosshair import VehicleDecorativeCrosshair

class OverheatDecorativeCrosshairMeta(VehicleDecorativeCrosshair):

    def as_setStacksProgresS(self, progress, level):
        if self._isDAAPIInited():
            return self.flashObject.as_setStacksProgres(progress, level)

    def as_setHeatProgresS(self, progress):
        if self._isDAAPIInited():
            return self.flashObject.as_setHeatProgres(progress)

    def as_updateStateS(self, state):
        if self._isDAAPIInited():
            return self.flashObject.as_updateState(state)

    def as_setInitDataS(self, speedLimit, maxLevel, heatingTime, coolingTime, isSpeedChanged):
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(speedLimit, maxLevel, heatingTime, coolingTime, isSpeedChanged)

    def as_setDamageDataS(self, baseDamage, maxDamage):
        if self._isDAAPIInited():
            return self.flashObject.as_setDamageData(baseDamage, maxDamage)