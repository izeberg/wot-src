from __future__ import absolute_import
import BigWorld
from helpers import isPlayerAvatar

def getScoreComponent():
    player = BigWorld.player()
    if not (player and isPlayerAvatar() and player.arena and player.arena.arenaInfo):
        return None
    else:
        return player.arena.arenaInfo.dynamicComponents.get('FortRushScoreComponent')