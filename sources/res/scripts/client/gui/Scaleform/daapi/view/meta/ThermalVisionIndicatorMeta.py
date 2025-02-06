from gui.Scaleform.daapi.view.battle.shared.indicator_items.base import BaseIndicator

class ThermalVisionIndicatorMeta(BaseIndicator):

    def as_setEnemyIndicatorS(self, isVisible):
        if self._isDAAPIInited():
            return self.flashObject.as_setEnemyIndicator(isVisible)