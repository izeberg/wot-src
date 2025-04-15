from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class DelayedSixthSenseMeta(BaseDAAPIComponent):

    def as_showS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_show()

    def as_hideS(self, force):
        if self._isDAAPIInited():
            return self.flashObject.as_hide(force)

    def as_updateS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_update(value)