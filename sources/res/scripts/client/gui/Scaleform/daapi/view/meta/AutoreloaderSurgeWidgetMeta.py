from gui.Scaleform.daapi.view.battle.shared.vehicle_mechanics.mechanic_widgets.vehicle_mechanic_widget import VehicleMechanicWidget

class AutoreloaderSurgeWidgetMeta(VehicleMechanicWidget):

    def as_setStagesProgressS(self, progress):
        if self._isDAAPIInited():
            return self.flashObject.as_setStagesProgress(progress)

    def as_setAvailableS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setAvailable(value)

    def as_setChargeCountS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setChargeCount(value)

    def as_setSectorCountS(self, count):
        if self._isDAAPIInited():
            return self.flashObject.as_setSectorCount(count)

    def as_setBoostedChargeS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setBoostedCharge(value)