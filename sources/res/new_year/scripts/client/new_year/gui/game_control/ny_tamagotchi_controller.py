from helpers.events_handler import EventsHandler
from new_year.helpers.server_settings import getNewYearGeneralConfig
from new_year.tamagotchi.simulator import TamagotchiSimulator
from new_year.tamagotchi.sys_msg.sys_msg_handler import TamagotchiSysMsgHandler
from new_year_common.items.components.ny_constants import ENT_TAMAGOCHI
from new_year.skeletons.new_year import INewYearTamagotchiController, ITamagotchiWebRequester, ITamagotchiDataProvider, INewYearController
from skeletons.gui.shared import IItemsCache
from helpers import dependency

class NewYearTamagotchiController(INewYearTamagotchiController, EventsHandler):
    __slots__ = ('__simulator', '__sysMsgHandler')
    _itemsCache = dependency.descriptor(IItemsCache)
    _webRequester = dependency.descriptor(ITamagotchiWebRequester)
    _dataProvider = dependency.descriptor(ITamagotchiDataProvider)
    _nyController = dependency.descriptor(INewYearController)

    def __init__(self):
        super(NewYearTamagotchiController, self).__init__()
        self.__simulator = TamagotchiSimulator()
        self.__sysMsgHandler = TamagotchiSysMsgHandler()

    @property
    def isEntObtained(self):
        return bool(self._itemsCache.items.stats.entitlements.get(ENT_TAMAGOCHI, False))

    @property
    def isPetVisible(self):
        return getNewYearGeneralConfig().getPetVisible()

    @property
    def __isPetVisible(self):
        return self.isEntObtained and self.isPetVisible

    def onConnected(self):
        self.__simulator.init()
        self.__sysMsgHandler.init()
        self._subscribe()

    def onDisconnected(self):
        self._unsubscribe()
        self._dataProvider.reset()
        self.__simulator.fini()
        self.__sysMsgHandler.fini()

    def onAccountBecomePlayer(self):
        if not self._dataProvider.raccoonState:
            self._itemsCache.onSyncCompleted += self.__onItemsSyncCompleted
        else:
            self.__simulator.setEnabled(self._dataProvider.raccoonState)

    def onAvatarBecomePlayer(self):
        self.__simulator.setEnabled(False)

    def _getEvents(self):
        return (
         (
          self._itemsCache.onSyncCompleted, self.__onItemsSyncCompleted),
         (
          self._nyController.onPetVisibilityUpdated, self.__setRaccoonState),
         (
          self._dataProvider._onPlayerInfoUpdated, self.__setRaccoonState))

    def __onItemsSyncCompleted(self, *_):
        if self.__isPetVisible:
            self._itemsCache.onSyncCompleted -= self.__onItemsSyncCompleted
            self._webRequester.requestPlayerInfo()

    def __setRaccoonState(self, state):
        self._dataProvider.raccoonState = state and self.__isPetVisible and self._dataProvider.isValidConfig
        self.__simulator.setEnabled(self._dataProvider.raccoonState)