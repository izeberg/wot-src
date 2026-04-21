from gui.Scaleform.daapi.view.battle.shared.vehicle_mechanics.mechanic_widgets.vehicle_mechanic_widget import VehicleMechanicWidget

class PropellantGunWidgetMeta(VehicleMechanicWidget):

    def as_setChargeValuesS(self, chargeProgress, chargeDamage):
        if self._isDAAPIInited():
            return self.flashObject.as_setChargeValues(chargeProgress, chargeDamage)

    def as_setupThresholdS(self, chargeThreshold):
        if self._isDAAPIInited():
            return self.flashObject.as_setupThreshold(chargeThreshold)

    def as_showHotKeysS(self, isShow=True):
        if self._isDAAPIInited():
            return self.flashObject.as_showHotKeys(isShow)

    def as_activateHotKeyS(self, command):
        if self._isDAAPIInited():
            return self.flashObject.as_activateHotKey(command)