from gui.Scaleform.daapi.view.battle.shared.vehicle_mechanics.panels_common import VehicleMechanicsPanel

class DecorativeCrosshairPanelMeta(VehicleMechanicsPanel):

    def as_addDecorCrosshairS(self, type):
        if self._isDAAPIInited():
            return self.flashObject.as_addDecorCrosshair(type)

    def as_setVisibleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setVisible(value)

    def as_updateLayoutS(self, x, y):
        if self._isDAAPIInited():
            return self.flashObject.as_updateLayout(x, y)

    def as_updateCrosshairTypeS(self, type):
        if self._isDAAPIInited():
            return self.flashObject.as_updateCrosshairType(type)