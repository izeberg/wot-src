from constants import Configs
from helpers import dependency
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.shared import IItemsCache
from web.client_web_api.api import C2WHandler, c2w
from web.common import formatCustomizationResourceState

class CustomizationResourceEventHandler(C2WHandler):
    __lobbyContext = dependency.descriptor(ILobbyContext)
    __itemsCache = dependency.descriptor(IItemsCache)

    def init(self):
        super(CustomizationResourceEventHandler, self).init()
        self.__lobbyContext.getServerSettings().onServerSettingsChange += self.__onServerSettingsChange
        self.__itemsCache.onSyncCompleted += self.__onItemsSyncCompleted

    def fini(self):
        self.__lobbyContext.getServerSettings().onServerSettingsChange -= self.__onServerSettingsChange
        self.__itemsCache.onSyncCompleted -= self.__onItemsSyncCompleted
        super(CustomizationResourceEventHandler, self).fini()

    def __onServerSettingsChange(self, diff):
        if Configs.CUSTOMIZATION_RESOURCE_CONFIG.value in diff:
            self.__sendState()

    def __onItemsSyncCompleted(self, *_):
        self.__sendState()

    @c2w(name='customization_resource_state_update')
    def __sendState(self):
        return formatCustomizationResourceState()