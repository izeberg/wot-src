import typing, BigWorld
from mt_birthday_common.constants import CMD_GET_PLAYERS_FROM_BATTLES
if typing.TYPE_CHECKING:
    from Account import Account

class TanksBirthdayAccountComponent(BigWorld.StaticScriptComponent):

    @property
    def _account(self):
        return self.entity

    def getPlayersFromBattles(self, arenaUniqueIds, callback):
        self._account.commandProxy.perform(CMD_GET_PLAYERS_FROM_BATTLES, arenaUniqueIds, [], callback)