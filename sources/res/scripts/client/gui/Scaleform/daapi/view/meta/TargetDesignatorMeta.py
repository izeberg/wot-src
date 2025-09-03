from gui.Scaleform.daapi.view.battle.shared.vehicle_mechanics.mechanic_widgets.vehicle_mechanic_widget import VehicleMechanicWidget

class TargetDesignatorMeta(VehicleMechanicWidget):

    def as_setPreparingProgressS(self, progress):
        if self._isDAAPIInited():
            return self.flashObject.as_setPreparingProgress(progress)