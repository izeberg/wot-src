from gui.Scaleform.daapi.view.battle.shared.vehicle_mechanics.mechanic_widgets.vehicle_mechanic_widget import VehicleMechanicWidget

class StanceDanceFightWidgetMeta(VehicleMechanicWidget):

    def as_setProgressS(self, isSwitchingState, progress):
        if self._isDAAPIInited():
            return self.flashObject.as_setProgress(isSwitchingState, progress)

    def as_energyBoostS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_energyBoost()

    def as_switchTimerS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_switchTimer(value)

    def as_keysVisibleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_keysVisible(value)

    def as_pauseReplayS(self, isPaused):
        if self._isDAAPIInited():
            return self.flashObject.as_pauseReplay(isPaused)