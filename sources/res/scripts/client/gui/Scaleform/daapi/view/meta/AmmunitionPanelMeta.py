from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class AmmunitionPanelMeta(BaseDAAPIComponent):

    def showRepairDialog(self):
        self._printOverrideError('showRepairDialog')

    def showCustomization(self):
        self._printOverrideError('showCustomization')

    def toRentContinue(self):
        self._printOverrideError('toRentContinue')

    def showChangeNation(self):
        self._printOverrideError('showChangeNation')

    def showEasyTankEquip(self):
        self._printOverrideError('showEasyTankEquip')

    def as_setMaintenanceWarningStateS(self, stateWarning):
        if self._isDAAPIInited():
            return self.flashObject.as_setMaintenanceWarningState(stateWarning)

    def as_highlightEasyTankEquipS(self, isHighlight):
        if self._isDAAPIInited():
            return self.flashObject.as_highlightEasyTankEquip(isHighlight)

    def as_updateVehicleStatusS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateVehicleStatus(data)

    def as_setCustomizationBtnCounterS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setCustomizationBtnCounter(value)