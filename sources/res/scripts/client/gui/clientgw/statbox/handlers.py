from gui.clientgw.base.handlers import RequestHandlers
from gui.clientgw.settings import WebRequestDataType

class StatBoxRequestHandlers(RequestHandlers):

    def get(self):
        handlers = {WebRequestDataType.STATBOX_STATISTICS_INFO: self.__getStatisticLootbox}
        return handlers

    def __getStatisticLootbox(self, ctx, callback):
        reqCtx = self._requester.doRequestEx(ctx, callback, ('statbox', 'get_statistic_lootbox'))
        return reqCtx