from gui.Scaleform.daapi.view.battle.shared.crosshair.container import CrosshairPanelContainer

class WTCrosshairPanelContainerMeta(CrosshairPanelContainer):

    def as_showPlasmaIndicatorS(self, plasmaValue, oldPlasmaValue, plasmaMultiplicatorText):
        if self._isDAAPIInited():
            return self.flashObject.as_showPlasmaIndicator(plasmaValue, oldPlasmaValue, plasmaMultiplicatorText)

    def as_setPlasmaSavedS(self, plasmaValue):
        if self._isDAAPIInited():
            return self.flashObject.as_setPlasmaSaved(plasmaValue)

    def as_showExplosiveShotIndicatorS(self, isActive):
        if self._isDAAPIInited():
            return self.flashObject.as_showExplosiveShotIndicator(isActive)

    def as_showBarrierS(self, isVisible, bindKey):
        if self._isDAAPIInited():
            return self.flashObject.as_showBarrier(isVisible, bindKey)

    def as_showIncreaseDamageS(self, useAnim=True):
        if self._isDAAPIInited():
            return self.flashObject.as_showIncreaseDamage(useAnim)

    def as_hideIncreaseDamageS(self, useAnim=True):
        if self._isDAAPIInited():
            return self.flashObject.as_hideIncreaseDamage(useAnim)

    def as_updateIncreaseDamageS(self, progress, isFail=False, useAnim=True):
        if self._isDAAPIInited():
            return self.flashObject.as_updateIncreaseDamage(progress, isFail, useAnim)

    def as_showReloadBoostS(self, useAnim=False):
        if self._isDAAPIInited():
            return self.flashObject.as_showReloadBoost(useAnim)

    def as_hideReloadBoostS(self, useAnim=False):
        if self._isDAAPIInited():
            return self.flashObject.as_hideReloadBoost(useAnim)

    def as_updateReloadBoostS(self, progress, isFail=False, useAnim=False):
        if self._isDAAPIInited():
            return self.flashObject.as_updateReloadBoost(progress, isFail, useAnim)

    def as_showS(self, useAnim=False):
        if self._isDAAPIInited():
            return self.flashObject.as_show(useAnim)

    def as_hideS(self, useAnim=False):
        if self._isDAAPIInited():
            return self.flashObject.as_hide(useAnim)