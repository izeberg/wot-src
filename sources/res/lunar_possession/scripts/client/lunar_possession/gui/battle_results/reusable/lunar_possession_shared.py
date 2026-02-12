from constants import DEATH_REASON_ALIVE
from gui.battle_results.reusable.shared import VehicleSummarizeInfo, VehicleDetailedInfo

class LunarPossessionVehicleDetailedInfo(VehicleDetailedInfo):
    __slots__ = ('_spiritPoints', )

    def __init__(self, vehicleID, vehicle, player, deathReason=DEATH_REASON_ALIVE):
        super(LunarPossessionVehicleDetailedInfo, self).__init__(vehicleID, vehicle, player, deathReason)
        self._spiritPoints = 0

    @property
    def spiritPoints(self):
        return self._spiritPoints

    @classmethod
    def _setSharedRecords(cls, info, records):
        super(LunarPossessionVehicleDetailedInfo, cls)._setSharedRecords(info, records)
        info._spiritPoints = records.get('lunarSpiritScore', 0)


class LunarPossessionVehicleSummarizeInfo(VehicleSummarizeInfo):

    @property
    def spiritPoints(self):
        value = self._accumulate('spiritPoints')
        return value