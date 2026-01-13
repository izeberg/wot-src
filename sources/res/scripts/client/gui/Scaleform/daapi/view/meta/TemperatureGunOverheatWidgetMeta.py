from gui.Scaleform.daapi.view.battle.shared.vehicle_mechanics.mechanic_widgets.vehicle_mechanic_widget import VehicleMechanicWidget

class TemperatureGunOverheatWidgetMeta(VehicleMechanicWidget):

    def as_setupThresholdsS(self, warning, overheat):
        if self._isDAAPIInited():
            return self.flashObject.as_setupThresholds(warning, overheat)

    def as_setTemperatureS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setTemperature(value)