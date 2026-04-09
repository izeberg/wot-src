from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class HBEnemiesPanelMeta(BaseDAAPIComponent):

    def as_getEnemyInfoDPS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getEnemyInfoDP()

    def as_setEnemyHpS(self, vehID, hpMax, hpCurrent):
        if self._isDAAPIInited():
            return self.flashObject.as_setEnemyHp(vehID, hpMax, hpCurrent)

    def as_setChatCommandS(self, vehID, chatCommand, chatCommandFlags):
        if self._isDAAPIInited():
            return self.flashObject.as_setChatCommand(vehID, chatCommand, chatCommandFlags)

    def as_setChatCommandsVisibilityS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setChatCommandsVisibility(value)