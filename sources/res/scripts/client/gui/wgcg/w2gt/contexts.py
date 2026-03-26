from gui.wgcg.base.contexts import CommonWebRequestCtx
from gui.wgcg.settings import WebRequestDataType

class W2gtCtx(CommonWebRequestCtx):

    def __init__(self, clientVersion, eTag, geometryName, gameplayType, vehRole, vehLevel, team, waitingID=''):
        self.__eTag = eTag
        vehicleRole = self.normalizeVehicleRole(vehRole)
        self.__params = {'client_version': clientVersion, 
           'map_name': geometryName, 
           'gameplay_type': gameplayType, 
           'vehicle_role': vehicleRole, 
           'level': vehLevel, 
           'team': team}
        super(W2gtCtx, self).__init__(waitingID=waitingID)

    @staticmethod
    def normalizeVehicleRole(vehRole):
        if vehRole.startswith('role_'):
            return vehRole.split('_', 1)[(-1)]
        return vehRole

    def getRequestType(self):
        return WebRequestDataType.W2GT_DATA

    def isAuthorizationRequired(self):
        return True

    def isClanSyncRequired(self):
        return False

    def isCaching(self):
        return False

    def getParams(self):
        return self.__params

    def getHeaders(self):
        if self.__eTag:
            return {'If-None-Match': self.__eTag}
        return {}