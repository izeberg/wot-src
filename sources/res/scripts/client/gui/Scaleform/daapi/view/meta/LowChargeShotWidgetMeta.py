from gui.Scaleform.daapi.view.battle.shared.vehicle_mechanics.mechanic_widgets.vehicle_mechanic_widget import VehicleMechanicWidget

class LowChargeShotWidgetMeta(VehicleMechanicWidget):

    def as_setInitialTimeS(self, baseTime, lowChargeTime, almostFinishedTime, lowChargeCap, shellChangeTime):
        if self._isDAAPIInited():
            return self.flashObject.as_setInitialTime(baseTime, lowChargeTime, almostFinishedTime, lowChargeCap, shellChangeTime)

    def as_setTimeLeftS(self, timeLeft, state, isReplay):
        if self._isDAAPIInited():
            return self.flashObject.as_setTimeLeft(timeLeft, state, isReplay)