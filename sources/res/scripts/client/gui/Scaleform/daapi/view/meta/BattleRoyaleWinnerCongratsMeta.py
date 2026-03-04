from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class BattleRoyaleWinnerCongratsMeta(BaseDAAPIComponent):

    def playWinSound(self):
        self._printOverrideError('playWinSound')

    def as_setStpCoinsS(self, initial, factor=1, bonus=1):
        if self._isDAAPIInited():
            return self.flashObject.as_setStpCoins(initial, factor, bonus)