from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class PhaseModifierMeta(BaseDAAPIComponent):

    def as_updateHintS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateHint(data)

    def as_setVisibleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setVisible(value)