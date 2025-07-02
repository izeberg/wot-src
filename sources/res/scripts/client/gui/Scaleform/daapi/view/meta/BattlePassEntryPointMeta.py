from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor

class BattlePassEntryPointMeta(InjectComponentAdaptor):

    def setIsSmall(self, value):
        self._printOverrideError('setIsSmall')

    def as_isChapterChosenS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_isChapterChosen(value)