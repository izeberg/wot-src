import Event
from constants import Configs
from helpers import dependency
from helpers.server_settings import EasyTankEquipConfig
from skeletons.gui.game_control import IEasyTankEquipController
from skeletons.gui.lobby_context import ILobbyContext

class EasyTankEquipController(IEasyTankEquipController):
    __lobbyContext = dependency.descriptor(ILobbyContext)

    def __init__(self):
        self.__em = Event.EventManager()
        self.onUpdated = Event.Event(self.__em)
        super(EasyTankEquipController, self).__init__()

    @property
    def config(self):
        if self.__lobbyContext:
            return self.__lobbyContext.getServerSettings().getEasyTankEquip()
        return EasyTankEquipConfig()

    def fini(self):
        self.__em.clear()
        self.__removeListeners()
        super(EasyTankEquipController, self).fini()

    def onDisconnected(self):
        self.__removeListeners()
        super(EasyTankEquipController, self).onDisconnected()

    def onLobbyInited(self, event):
        super(EasyTankEquipController, self).onLobbyInited(event)
        self.__lobbyContext.getServerSettings().onServerSettingsChange += self.__onSettingsChanged

    def onAccountBecomeNonPlayer(self):
        self.__removeListeners()
        super(EasyTankEquipController, self).onAccountBecomeNonPlayer()

    def __removeListeners(self):
        self.__lobbyContext.getServerSettings().onServerSettingsChange -= self.__onSettingsChanged

    def __onSettingsChanged(self, diff):
        if Configs.EASY_TANK_EQUIP_CONFIG.value in diff:
            self.onUpdated()