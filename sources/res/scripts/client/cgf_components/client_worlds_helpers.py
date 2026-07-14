from __future__ import absolute_import
import enum, BattleReplay
from constants import IS_UE_EDITOR
from helpers import isPlayerAccount, isPlayerAvatar

class ClientWorld(enum.IntEnum):
    NONE = 0
    BATTLE = 1
    HANGAR = 2
    EDITOR = 4
    AllWorlds = BATTLE | HANGAR | EDITOR


def getClientWorld():
    if IS_UE_EDITOR:
        clientWorld = ClientWorld.EDITOR
    elif isPlayerAccount():
        clientWorld = ClientWorld.HANGAR
    elif isPlayerAvatar() or BattleReplay.isPlaying() or BattleReplay.isServerSideReplay():
        clientWorld = ClientWorld.BATTLE
    else:
        clientWorld = ClientWorld.NONE
    return clientWorld


def clientWorldsPredicate(clientWorlds):

    def predicate(_):
        return bool(getClientWorld() & clientWorlds)

    return predicate