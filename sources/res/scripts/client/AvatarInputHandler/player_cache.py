import PlayerEvents, BigWorld
from avatar_helpers.player_cache import IPlayerCacheController

class PlayerCacheController(IPlayerCacheController):

    def __init__(self):
        self.player = BigWorld.player()
        PlayerEvents.g_playerEvents.onAvatarBecomePlayer += self._onPlayerChanged
        PlayerEvents.g_playerEvents.onAvatarBecomeNonPlayer += self._onPlayerChanged
        PlayerEvents.g_playerEvents.onAvatarReady += self._onPlayerChanged

    def _onPlayerChanged(self):
        self.player = BigWorld.player()
        return self.player

    def destroy(self):
        self.player = None
        PlayerEvents.g_playerEvents.onAvatarBecomePlayer -= self._onPlayerChanged
        PlayerEvents.g_playerEvents.onAvatarBecomeNonPlayer -= self._onPlayerChanged
        PlayerEvents.g_playerEvents.onAvatarReady -= self._onPlayerChanged
        return