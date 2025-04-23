from gui.sounds.ambients import BattleResultsEnv

class FunRandomBattleResultsEnv(BattleResultsEnv):

    def _getLastWinStatus(self):
        super(FunRandomBattleResultsEnv, self)._getLastWinStatus()
        return