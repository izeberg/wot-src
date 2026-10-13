import logging, typing
if typing.TYPE_CHECKING:
    from web.web_client_api import CommandHandler
_logger = logging.getLogger(__name__)

class WebHandlersContainer(object):
    _webHandlers = {}

    @classmethod
    def addWebHandler(cls, name, handler):
        cls._webHandlers[name] = handler

    @classmethod
    def removeWebHandler(cls, name):
        if name in cls._webHandlers:
            del cls._webHandlers[name]

    @classmethod
    def getWebHandler(cls, name):
        if name is None:
            return
        else:
            if name not in cls._webHandlers:
                _logger.warning("Cannot get web client handler by name '%s'", name)
                return
            return cls._webHandlers[name]