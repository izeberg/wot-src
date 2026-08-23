from __future__ import absolute_import
from gui.shared.events import HasCtxEvent

class WhiteTigerEvent(HasCtxEvent):
    SHOW_SPAWN_POINTS = 'game/showSpawnPoints'
    HIDE_SPAWN_POINTS = 'game/hideSpawnPoints'