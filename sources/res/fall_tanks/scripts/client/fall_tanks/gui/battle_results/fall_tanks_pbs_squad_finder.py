from __future__ import absolute_import
from collections import defaultdict
from gui.battle_control.arena_info.squad_finder import ISquadFinder
from gui.battle_control.arena_info.settings import SQUAD_RANGE_TO_SHOW

class FallTanksPostbattleSquadFinder(ISquadFinder):
    __slots__ = ('__squadIndices', '__prbStats')

    def __init__(self, _):
        super(FallTanksPostbattleSquadFinder, self).__init__()
        self.__prbStats = defaultdict(set)
        self.__squadIndices = {}

    def clear(self):
        self.__squadIndices.clear()
        self.__prbStats.clear()

    def addVehicleInfo(self, team, prebattleID, vehicleID):
        if not prebattleID:
            return
        self.__prbStats[prebattleID].add(vehicleID)

    def getNumberOfSquads(self):
        if self.__squadIndices:
            return max(self.__squadIndices.values())
        return 0

    def getNumberOfSquadmen(self, team, prebattleID):
        return 0

    def findSquads(self):
        squadRange = self._getSquadRange()
        for prebattleID, vehiclesIDs in self.__prbStats.items():
            if not vehiclesIDs or len(vehiclesIDs) not in squadRange:
                continue
            if prebattleID not in self.__squadIndices:
                if self.__squadIndices:
                    self.__squadIndices[prebattleID] = max(self.__squadIndices.values()) + 1
                else:
                    self.__squadIndices[prebattleID] = 1
            for vehicleID in vehiclesIDs:
                yield (
                 vehicleID, self.__squadIndices[prebattleID])

    @classmethod
    def _getSquadRange(cls):
        return SQUAD_RANGE_TO_SHOW