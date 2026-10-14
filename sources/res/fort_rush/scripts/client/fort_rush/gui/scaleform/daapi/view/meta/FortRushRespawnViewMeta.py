from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class FortRushRespawnViewMeta(BaseDAAPIComponent):

    def onRespawnPointClick(self, id):
        self._printOverrideError('onRespawnPointClick')

    def onBattleButtonClicked(self, value):
        self._printOverrideError('onBattleButtonClicked')

    def as_setTimerS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setTimer(value)