from gui.wgcg.base.contexts import CommonWebRequestCtx
from gui.wgcg.settings import WebRequestDataType

class RankedPositionCtx(CommonWebRequestCtx):

    def getRequestType(self):
        return WebRequestDataType.RANKED_LEAGUE_POSITION

    def isAuthorizationRequired(self):
        return True

    def isClanSyncRequired(self):
        return False

    def isCaching(self):
        return False


class RankedYearPositionCtx(CommonWebRequestCtx):

    def getRequestType(self):
        return WebRequestDataType.RANKED_YEAR_POSITION

    def isAuthorizationRequired(self):
        return True

    def isClanSyncRequired(self):
        return False

    def isCaching(self):
        return False