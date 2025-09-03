from gui.Scaleform.daapi.view.battle.shared.vehicle_mechanics.components_common import VehicleMechanicDAAPIComponent

class BaseDecorativeCrosshairMeta(VehicleMechanicDAAPIComponent):

    def as_setStateS(self, state, isInstantly=False):
        if self._isDAAPIInited():
            return self.flashObject.as_setState(state, isInstantly)

    def as_setVisibleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setVisible(value)