import typing, BigWorld
from events_core_client.score_system.PlayerInfoScoreComponent import PlayerInfoScoreComponent
if typing.TYPE_CHECKING:
    from typing import Optional

def getArenaInfoScoreComponent():
    player = BigWorld.player()
    if player and player.arena is not None:
        arenaInfo = player.arena.arenaInfo
        if arenaInfo:
            return arenaInfo.dynamicComponents.get('arenaInfoScoreComponent', None)
    return


class ArenaInfoScoreComponent(PlayerInfoScoreComponent):
    pass