import logging, typing
from historical_battles_common import account_commands
import AccountCommands, BigWorld
if typing.TYPE_CHECKING:
    from typing import Optional, Callable
    from Account import Account
_logger = logging.getLogger(__name__)

class HBAccountBattleResultCache(BigWorld.StaticScriptComponent):

    @property
    def account(self):
        return self.entity

    def applyBooster(self, arenaUniqueID, boosterTokenID, callback=None):

        def cmdCallback(requestId, resultId, errorStr):
            if resultId != AccountCommands.RES_SUCCESS:
                _logger.error(errorStr)
                return
            if callback:
                callback()

        self.account._doCmdIntStr(account_commands.CMD_HB_APPLY_BOOSTER, arenaUniqueID, boosterTokenID, cmdCallback)

    def requestBattleResults(self, arenaUniqueID, callback):

        def cmdCallback(requestId, resultId, errorStr, ext=None):
            if resultId != AccountCommands.RES_SUCCESS:
                _logger.error(errorStr)
                return
            if ext:
                earnedCoins, appliedBooster = ext
                callback(earnedCoins, appliedBooster)

        self.account._doCmdInt(account_commands.CMD_HB_REQUEST_BATTLE_RESULTS, arenaUniqueID, cmdCallback)
        return