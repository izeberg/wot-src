from helpers import dependency
from skeletons.gui.lobby_context import ILobbyContext
from web.web_client_api import W2CSchema, w2c

class ReactiveCommunicationConfigWebApiMixin(object):
    __lobbyContext = dependency.descriptor(ILobbyContext)

    @w2c(W2CSchema, 'reactive_communication_config')
    def getHermodSettings(self, cmd):
        return self.__lobbyContext.getServerSettings().getReactiveCommunicationConfig().asDict()