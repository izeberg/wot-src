from gui.Scaleform.daapi.view.battle.shared.vehicle_mechanics.mechanic_widgets.vehicle_mechanic_widget import VehicleMechanicWidget

class RocketAcceleratorIndicatorMeta(VehicleMechanicWidget):

    def as_setCountS(self, count):
        if self._isDAAPIInited():
            return self.flashObject.as_setCount(count)

    def as_setProgressS(self, progress):
        if self._isDAAPIInited():
            return self.flashObject.as_setProgress(progress)

    def as_updateLayoutS(self, x, y):
        if self._isDAAPIInited():
            return self.flashObject.as_updateLayout(x, y)