import typing, BigWorld
from events_core_client.score_system.PlayerInfoScoreComponent import PlayerInfoScoreComponent
if typing.TYPE_CHECKING:
    from typing import Optional

def getTeamInfoScoreComponent():
    player = BigWorld.player()
    if player and player.arena is not None:
        teamInfo = player.arena.teamInfo
        if teamInfo:
            return teamInfo.dynamicComponents.get('teamInfoScoreComponent', None)
    return


class TeamInfoScoreComponent(PlayerInfoScoreComponent):
    pass