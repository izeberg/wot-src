import logging, Event
from script_component.DynamicScriptComponent import DynamicScriptComponent
_logger = logging.getLogger(__name__)

class HBTeamInfoComponent(DynamicScriptComponent):
    onAllyInfoUpdated = Event.Event()

    def set_alliesInfo(self, _):
        self.onAllyInfoUpdated()

    def getDivisionLevel(self, vehicleID):
        allyInfo = self.__getAllyInfo(vehicleID)
        if allyInfo:
            return allyInfo.divisionLevel
        return 1

    def getAliveVehicleCount(self, vehicleID):
        allyInfo = self.__getAllyInfo(vehicleID)
        if allyInfo:
            return allyInfo.vehicleCount
        return 0

    def getRespawnTime(self, vehicleID):
        allyInfo = self.__getAllyInfo(vehicleID)
        if allyInfo:
            return allyInfo.respawnTime
        return 0.0

    def __getAllyInfo(self, vehicleID):
        allyInfo = next((info for info in self.alliesInfo if info.vehicleID == vehicleID), None)
        if not allyInfo:
            _logger.error('There is no info for vehicle %d', vehicleID)
        return allyInfo