from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class HangarHeaderMeta(BaseDAAPIComponent):

    def onQuestBtnClick(self, questType, questID):
        self._printOverrideError('onQuestBtnClick')

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_setSecondaryEntryPointVisibleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setSecondaryEntryPointVisible(value)

    def as_addEntryPointS(self, alias, registerAlias=None):
        if self._isDAAPIInited():
            return self.flashObject.as_addEntryPoint(alias, registerAlias)

    def as_addSecondaryEntryPointS(self, alias, isRight):
        if self._isDAAPIInited():
            return self.flashObject.as_addSecondaryEntryPoint(alias, isRight)

    def as_setCollectiveGoalEntryPointS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setCollectiveGoalEntryPoint(value)

    def as_setUniversalFlagEntryPointS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setUniversalFlagEntryPoint(value)

    def as_setArmoryYardEntryPointS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setArmoryYardEntryPoint(value)

    def as_setEarlyAccessEntryPointS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setEarlyAccessEntryPoint(value)