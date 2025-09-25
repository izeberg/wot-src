from gui.Scaleform.daapi.view.battle.shared.vehicle_mechanics.components_common import VehicleMechanicDAAPIComponent

class BaseVehicleMechanicsWidgetMeta(VehicleMechanicDAAPIComponent):

    def as_setStateS(self, state, isInstantly=False):
        if self._isDAAPIInited():
            return self.flashObject.as_setState(state, isInstantly)

    def as_setHotKeysS(self, keyCodes):
        if self._isDAAPIInited():
            return self.flashObject.as_setHotKeys(keyCodes)

    def as_setVisibleS(self, visible):
        if self._isDAAPIInited():
            return self.flashObject.as_setVisible(visible)

    def as_setCrosshairTypeS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setCrosshairType(value)

    def as_setTimeS(self, time):
        if self._isDAAPIInited():
            return self.flashObject.as_setTime(time)