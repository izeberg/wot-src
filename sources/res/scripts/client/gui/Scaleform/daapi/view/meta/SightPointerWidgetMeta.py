from gui.Scaleform.daapi.view.battle.shared.vehicle_mechanics.mechanic_widgets.vehicle_mechanic_widget import VehicleMechanicWidget

class SightPointerWidgetMeta(VehicleMechanicWidget):

    def as_setProgressS(self, progress, timeLeft):
        if self._isDAAPIInited():
            return self.flashObject.as_setProgress(progress, timeLeft)

    def as_setTankIconStateS(self, state):
        if self._isDAAPIInited():
            return self.flashObject.as_setTankIconState(state)

    def as_triggerHighlightLampS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_triggerHighlightLamp()