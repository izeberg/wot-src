from gui.battle_control.arena_info.interfaces import IArenaLoadController

class IComp7VOIPController(IArenaLoadController):
    __slots__ = ()

    @property
    def isVoipSupported(self):
        raise NotImplementedError

    @property
    def isVoipEnabled(self):
        raise NotImplementedError

    @property
    def isTeamChannelAvailable(self):
        raise NotImplementedError

    @property
    def isJoined(self):
        raise NotImplementedError

    @property
    def isTeamVoipEnabled(self):
        raise NotImplementedError

    def toggleChannelConnection(self):
        raise NotImplementedError