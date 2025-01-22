from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class FragCorrelationBarMeta(BaseDAAPIComponent):

    def as_updateHPS(self, allyHP, diff, allyHPProgress, enemyHP, enemyHPProgress):
        if self._isDAAPIInited():
            return self.flashObject.as_updateHP(allyHP, diff, allyHPProgress, enemyHP, enemyHPProgress)

    def as_updateViewSettingS(self, setting):
        if self._isDAAPIInited():
            return self.flashObject.as_updateViewSetting(setting)