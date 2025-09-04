from gui.Scaleform.daapi.view.battle.shared.vehicle_mechanics.mechanic_widgets.vehicle_mechanic_widget import VehicleMechanicWidget

class ChargeShotWidgetMeta(VehicleMechanicWidget):

    def as_setUpdateProgressS(self, stack, progressValue):
        if self._isDAAPIInited():
            return self.flashObject.as_setUpdateProgress(stack, progressValue)

    def as_setShootBlockS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setShootBlock(value)

    def as_setDamageS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setDamage(value)

    def as_showShootBlockAnimationS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_showShootBlockAnimation()