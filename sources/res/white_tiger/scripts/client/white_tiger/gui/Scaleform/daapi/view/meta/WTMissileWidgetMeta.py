from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class WTMissileWidgetMeta(BaseDAAPIComponent):

    def as_setRangeS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setRange(value)

    def as_setAltitudeS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setAltitude(value)

    def as_setMaxAltitudeS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setMaxAltitude(value)

    def as_showS(self, useAnim=False):
        if self._isDAAPIInited():
            return self.flashObject.as_show(useAnim)

    def as_hideS(self, useAnim=False):
        if self._isDAAPIInited():
            return self.flashObject.as_hide(useAnim)