from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class PostBattleCommendationMeta(BaseDAAPIComponent):

    def selectedChoice(self, choice):
        self._printOverrideError('selectedChoice')

    def as_setInitDataS(self, choices, selectedChoice):
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(choices, selectedChoice)