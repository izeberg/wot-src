from gui.Scaleform.daapi.view.battle.shared.vehicle_mechanics.mechanic_widgets.vehicle_mechanic_widget import VehicleMechanicWidget

class StationaryReloadWidgetMeta(VehicleMechanicWidget):

    def as_setConditionS(self, condition):
        if self._isDAAPIInited():
            return self.flashObject.as_setCondition(condition)