from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class WTAbilityWidgetMeta(BaseDAAPIComponent):

    def as_addMissileWidgetS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_addMissileWidget()