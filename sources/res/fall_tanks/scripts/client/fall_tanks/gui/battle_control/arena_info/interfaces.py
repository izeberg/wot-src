from __future__ import absolute_import
import typing
from gui.battle_control.arena_info.interfaces import IArenaVehiclesController
if typing.TYPE_CHECKING:
    from Event import Event

class IFallTanksVehicleInfo(object):

    @property
    def isFinished(self):
        raise NotImplementedError

    @property
    def isPlayerVehicle(self):
        raise NotImplementedError

    @property
    def isPlayerVehicleInRace(self):
        raise NotImplementedError

    @property
    def checkpoint(self):
        raise NotImplementedError

    @property
    def finishTime(self):
        raise NotImplementedError

    @property
    def frags(self):
        raise NotImplementedError

    @property
    def racePosition(self):
        raise NotImplementedError


class IFallTanksBattleController(IArenaVehiclesController):
    onFallTanksAttachedInfoUpdate = None

    def getFallTanksAttachedVehicleInfo(self):
        raise NotImplementedError

    def getFallTanksPlayerVehicleInfo(self):
        raise NotImplementedError