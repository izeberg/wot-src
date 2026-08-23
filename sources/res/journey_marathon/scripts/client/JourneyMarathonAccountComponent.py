from __future__ import absolute_import
import typing, AccountCommands
from BaseAccountExtensionComponent import BaseAccountExtensionComponent
from PlayerEvents import g_playerEvents as events
from journey_marathon_common.journey_marathon_account_commands import CMD_JOURNEY_MOVE_POINTER, CMD_JOURNEY_OPEN_NODES
if typing.TYPE_CHECKING:
    from typing import List, Optional, Callable

def _getAccountRepository():
    import Account
    return Account.g_accountRepository


class JourneyMarathonAccountComponent(BaseAccountExtensionComponent):

    def __init__(self):
        BaseAccountExtensionComponent.__init__(self)
        self._ignore = True
        events.onAccountBecomeNonPlayer += self.onAccountBecomeNonPlayer
        events.onAccountBecomePlayer += self.onAccountBecomePlayer

    def openJMNodeIds(self, nodeIds, callback=None):
        repository = _getAccountRepository()
        if repository is None or self._ignore:
            if callback is not None:
                callback(AccountCommands.RES_NON_PLAYER, 'NON_PLAYER')
            return
        proxy = (lambda requestID, resultID, errorStr, ext={}: callback(resultID, errorStr, ext)) if callback is not None else None
        repository.commandProxy.perform(CMD_JOURNEY_OPEN_NODES, nodeIds, proxy)
        return

    def moveJmCurrentNode(self, nodeId, callback=None):
        repository = _getAccountRepository()
        if repository is None or self._ignore:
            if callback is not None:
                callback(AccountCommands.RES_NON_PLAYER, 'NON_PLAYER')
            return
        proxy = (lambda requestID, resultID, errorStr, ext={}: callback(resultID, errorStr)) if callback is not None else None
        repository.commandProxy.perform(CMD_JOURNEY_MOVE_POINTER, nodeId, proxy)
        return

    def onAccountBecomePlayer(self):
        self._ignore = False
        events.onAccountBecomePlayer -= self.onAccountBecomePlayer

    def onAccountBecomeNonPlayer(self):
        self._ignore = True
        events.onAccountBecomeNonPlayer -= self.onAccountBecomeNonPlayer