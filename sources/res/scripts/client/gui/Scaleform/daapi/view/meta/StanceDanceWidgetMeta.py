from gui.Scaleform.daapi.view.battle.shared.vehicle_mechanics.mechanic_widgets.vehicle_mechanic_widget import VehicleMechanicWidget

class StanceDanceWidgetMeta(VehicleMechanicWidget):

    def as_setStatusS(self, isFightState, isTurboState, isActiveFightState, isActiveTurboState):
        if self._isDAAPIInited():
            return self.flashObject.as_setStatus(isFightState, isTurboState, isActiveFightState, isActiveTurboState)

    def as_setProgressS(self, isSwitchingState, progressFight, progressTurbo):
        if self._isDAAPIInited():
            return self.flashObject.as_setProgress(isSwitchingState, progressFight, progressTurbo)