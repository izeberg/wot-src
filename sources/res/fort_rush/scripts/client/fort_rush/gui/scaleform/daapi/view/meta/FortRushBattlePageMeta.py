from gui.Scaleform.daapi.view.battle.classic.page import ClassicPage

class FortRushBattlePageMeta(ClassicPage):

    def as_setRespawnModeS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setRespawnMode(value)