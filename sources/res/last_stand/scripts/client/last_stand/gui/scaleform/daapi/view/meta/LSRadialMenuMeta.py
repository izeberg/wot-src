from gui.Scaleform.daapi.view.battle.shared.radial_menu import RadialMenu

class LSRadialMenuMeta(RadialMenu):

    def as_setObeliskEnabledS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setObeliskEnabled(value)