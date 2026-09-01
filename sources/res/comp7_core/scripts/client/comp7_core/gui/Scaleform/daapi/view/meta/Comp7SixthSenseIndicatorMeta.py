from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class Comp7SixthSenseIndicatorMeta(BaseDAAPIComponent):

    def as_showS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_show()

    def as_hideS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hide()

    def as_setStateS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setState(value)