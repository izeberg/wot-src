from gui.Scaleform.daapi.view.battle.shared.vehicle_mechanics.mechanic_widgets.vehicle_mechanic_widget import VehicleMechanicWidget

class ChargeableBurstWidgetMeta(VehicleMechanicWidget):

    def as_setupS(self, penetrationCount, burstShootCount):
        if self._isDAAPIInited():
            return self.flashObject.as_setup(penetrationCount, burstShootCount)

    def as_setModeS(self, isBurstMode, isInstantly):
        if self._isDAAPIInited():
            return self.flashObject.as_setMode(isBurstMode, isInstantly)

    def as_setChargesS(self, charges, burstShotCount, isInstantly):
        if self._isDAAPIInited():
            return self.flashObject.as_setCharges(charges, burstShotCount, isInstantly)

    def as_setShellsQuantityLeftS(self, count):
        if self._isDAAPIInited():
            return self.flashObject.as_setShellsQuantityLeft(count)

    def as_updateBurstReloadingStateS(self, isReloading):
        if self._isDAAPIInited():
            return self.flashObject.as_updateBurstReloadingState(isReloading)