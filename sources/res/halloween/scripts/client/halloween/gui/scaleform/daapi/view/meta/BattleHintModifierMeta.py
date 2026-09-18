from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class BattleHintModifierMeta(BaseDAAPIComponent):

    def as_updateHintS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateHint(data)