from gui.wgcg.base.contexts import CommonWebRequestCtx
from gui.wgcg.settings import WebRequestDataType

class GoldWagonFetchInfoCtx(CommonWebRequestCtx):

    def getRequestType(self):
        return WebRequestDataType.GOLD_WAGON_INFO

    def isAuthorizationRequired(self):
        return False

    def isClanSyncRequired(self):
        return False

    def isCaching(self):
        return False