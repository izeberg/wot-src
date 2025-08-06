import typing, AccountCommands
if typing.TYPE_CHECKING:
    from typing import Callable, Optional

class WotAnniversary(object):

    def __init__(self, commandsProxy):
        self.__commandsProxy = commandsProxy

    def openEnvelope(self, callback=None):
        if callback is not None:
            proxy = lambda requestID, resultID, errorStr, ext=None: callback(resultID, errorStr, ext)
        else:
            proxy = None
        self.__commandsProxy.perform(AccountCommands.CMD_WOT_ANNIVERSARY_OPEN_ENVELOPE, proxy)
        return