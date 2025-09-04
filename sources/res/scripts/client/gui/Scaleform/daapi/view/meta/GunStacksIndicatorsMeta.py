from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class GunStacksIndicatorsMeta(BaseDAAPIComponent):

    def as_setVisibleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setVisible(value)

    def as_setBonusS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setBonus(value)

    def as_setProgressS(self, idx, percent):
        if self._isDAAPIInited():
            return self.flashObject.as_setProgress(idx, percent)

    def as_setProgressAsPercentS(self, idx, percent):
        if self._isDAAPIInited():
            return self.flashObject.as_setProgressAsPercent(idx, percent)