import typing
from skeletons.gui.game_control import IGameController
if typing.TYPE_CHECKING:
    from typing import Dict, Optional
    from Event import Event
    from grinch.gui.prebattle_hints.random_prb_hints import PrbRandomHintManager

class IGrinchController(IGameController):
    onPrimeTimeStatusUpdated = None
    onSeasonStatusUpdated = None

    @property
    def prbHintManager(self):
        return

    def isEnabled(self):
        raise NotImplementedError

    def isAvailable(self):
        raise NotImplementedError

    def isEventPrbActive(self):
        raise NotImplementedError

    def isFrozen(self):
        raise NotImplementedError

    def getConfig(self):
        raise NotImplementedError

    def selectMode(self):
        raise NotImplementedError

    def selectRandomMode(self):
        raise NotImplementedError

    def getSquadConfig(self):
        raise NotImplementedError