from gui.Scaleform.daapi.view.battle.shared.vehicle_mechanics.mechanic_widgets.vehicle_mechanic_widget import VehicleMechanicWidget

class StanceDanceBaseWidgetMeta(VehicleMechanicWidget):

    def as_setStatusS(self, isChosen, isActive):
        if self._isDAAPIInited():
            return self.flashObject.as_setStatus(isChosen, isActive)

    def as_setProgressS(self, isSwitchingState, progress):
        if self._isDAAPIInited():
            return self.flashObject.as_setProgress(isSwitchingState, progress)