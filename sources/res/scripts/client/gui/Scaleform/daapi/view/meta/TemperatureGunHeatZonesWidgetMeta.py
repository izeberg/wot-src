from gui.Scaleform.daapi.view.battle.shared.vehicle_mechanics.mechanic_widgets.vehicle_mechanic_widget import VehicleMechanicWidget

class TemperatureGunHeatZonesWidgetMeta(VehicleMechanicWidget):

    def as_setHeatZonesValuesS(self, low, medium=1):
        if self._isDAAPIInited():
            return self.flashObject.as_setHeatZonesValues(low, medium)

    def as_setTemperatureS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setTemperature(value)