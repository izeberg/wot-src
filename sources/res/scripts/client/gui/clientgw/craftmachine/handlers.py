from gui.clientgw.base.handlers import RequestHandlers
from gui.clientgw.settings import WebRequestDataType

class CraftmachineRequestHandlers(RequestHandlers):

    def get(self):
        handlers = {WebRequestDataType.CRAFTMACHINE_MODULES_INFO: self.__modulesInfo}
        return handlers

    def __modulesInfo(self, ctx, callback):
        reqCtx = self._requester.doRequestEx(ctx, callback, ('craftmachine', 'craftmachine_modules_info'))
        return reqCtx