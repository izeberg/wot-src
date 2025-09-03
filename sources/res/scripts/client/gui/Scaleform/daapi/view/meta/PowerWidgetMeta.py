from gui.Scaleform.daapi.view.battle.shared.vehicle_mechanics.mechanic_widgets.vehicle_mechanic_widget import VehicleMechanicWidget

class PowerWidgetMeta(VehicleMechanicWidget):

    def as_setProgressS(self, progress):
        if self._isDAAPIInited():
            return self.flashObject.as_setProgress(progress)