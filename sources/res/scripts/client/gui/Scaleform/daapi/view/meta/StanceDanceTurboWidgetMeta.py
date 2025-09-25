from gui.Scaleform.daapi.view.battle.shared.vehicle_mechanics.mechanic_widgets.vehicle_mechanic_widget import VehicleMechanicWidget

class StanceDanceTurboWidgetMeta(VehicleMechanicWidget):

    def as_setProgressS(self, isSwitchingState, progress):
        if self._isDAAPIInited():
            return self.flashObject.as_setProgress(isSwitchingState, progress)

    def as_setSpeedS(self, currentSpeed, isActive):
        if self._isDAAPIInited():
            return self.flashObject.as_setSpeed(currentSpeed, isActive)

    def as_setParamsS(self, maxSpeed, maxActiveSpeed, maxTurboSpeed, gainSpeed):
        if self._isDAAPIInited():
            return self.flashObject.as_setParams(maxSpeed, maxActiveSpeed, maxTurboSpeed, gainSpeed)

    def as_switchTimerS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_switchTimer(value)

    def as_keysVisibleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_keysVisible(value)