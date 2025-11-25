from gui.wgcg.settings import WebRequestDataType
from gui.shared.utils.requesters import RequestCtx

class IngameTournamentGetDataCtx(RequestCtx):

    def getRequestType(self):
        return WebRequestDataType.INGAME_TOURNAMENT_GET_DATA

    def isAuthorizationRequired(self):
        return False

    def isClanSyncRequired(self):
        return False

    def isCaching(self):
        return False