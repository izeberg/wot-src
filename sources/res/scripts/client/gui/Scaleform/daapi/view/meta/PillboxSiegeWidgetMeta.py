from gui.Scaleform.daapi.view.battle.shared.vehicle_mechanics.mechanic_widgets.vehicle_mechanic_widget import VehicleMechanicWidget

class PillboxSiegeWidgetMeta(VehicleMechanicWidget):

    def as_setProgressS(self, progress, timeLeft):
        if self._isDAAPIInited():
            return self.flashObject.as_setProgress(progress, timeLeft)

    def as_setConditionS(self, condition, isUpdatable):
        if self._isDAAPIInited():
            return self.flashObject.as_setCondition(condition, isUpdatable)

    def as_setDeviceStatesS(self, deviceStates):
        if self._isDAAPIInited():
            return self.flashObject.as_setDeviceStates(deviceStates)

    def as_setCommandS(self, command, affectOn, duration):
        if self._isDAAPIInited():
            return self.flashObject.as_setCommand(command, affectOn, duration)