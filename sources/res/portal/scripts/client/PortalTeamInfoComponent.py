import logging, Event
from script_component.DynamicScriptComponent import DynamicScriptComponent
_logger = logging.getLogger(__name__)

class PortalTeamInfoComponent(DynamicScriptComponent):
    onAllyInfoUpdated = Event.Event()

    def setNested_alliesInfo(self, changePath, oldValue):
        index = changePath[0]
        info = self.alliesInfo[index]
        vehicleID = info.vehicleID
        self.onAllyInfoUpdated(vehicleID)

    def getRespawnTime(self, vehicleID):
        allyInfo = self.__getAllyInfo(vehicleID)
        if allyInfo:
            return allyInfo.respawnTime
        return 0.0

    def getVehicleLevel(self, vehicleID):
        allyInfo = self.__getAllyInfo(vehicleID)
        if allyInfo:
            return allyInfo.vehicleLevel
        return 0

    def __getAllyInfo(self, vehicleID):
        allyInfo = next((info for info in self.alliesInfo if info.vehicleID == vehicleID), None)
        if not allyInfo:
            _logger.error('There is no info for vehicle %d', vehicleID)
        return allyInfo