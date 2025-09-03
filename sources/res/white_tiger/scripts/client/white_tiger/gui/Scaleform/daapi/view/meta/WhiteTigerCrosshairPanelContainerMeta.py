from gui.Scaleform.daapi.view.battle.shared.crosshair import CrosshairPanelContainer

class WhiteTigerCrosshairPanelContainerMeta(CrosshairPanelContainer):

    def as_showPlasmaIndicatorS(self, plasmaValue, isPlasmaChanged, plasmaMultiplicatorText):
        if self._isDAAPIInited():
            return self.flashObject.as_showPlasmaIndicator(plasmaValue, isPlasmaChanged, plasmaMultiplicatorText)

    def as_showExplosiveShotIndicatorS(self, isActive):
        if self._isDAAPIInited():
            return self.flashObject.as_showExplosiveShotIndicator(isActive)