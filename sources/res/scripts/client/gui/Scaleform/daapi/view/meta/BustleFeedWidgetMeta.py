from gui.Scaleform.daapi.view.battle.shared.vehicle_mechanics.mechanic_widgets.vehicle_mechanic_widget import VehicleMechanicWidget

class BustleFeedWidgetMeta(VehicleMechanicWidget):

    def as_setProgressS(self, progress, time):
        if self._isDAAPIInited():
            return self.flashObject.as_setProgress(progress, time)

    def as_setLockS(self, isLocked):
        if self._isDAAPIInited():
            return self.flashObject.as_setLock(isLocked)

    def as_setAvailabilityS(self, isDisable):
        if self._isDAAPIInited():
            return self.flashObject.as_setAvailability(isDisable)

    def as_setCommandS(self, command):
        if self._isDAAPIInited():
            return self.flashObject.as_setCommand(command)