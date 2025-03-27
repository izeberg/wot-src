from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class FrontlineDamagePanelMeta(BaseDAAPIComponent):

    def as_setGeneralBonusS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setGeneralBonus(value)