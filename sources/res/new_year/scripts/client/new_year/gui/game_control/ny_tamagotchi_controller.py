from BigWorld import callback, cancelCallback
from Event import EventManager, Event
from PlayerEvents import g_playerEvents
from helpers import dependency
from helpers.events_handler import EventsHandler
from helpers.time_utils import getServerUTCTime
from new_year.helpers.server_settings import getNewYearGeneralConfig
from new_year.ny_constants import SyncDataKeys
from new_year.tamagotchi.config_notifier import TamagotchiConfigNotifier
from new_year.tamagotchi.simulator import TamagotchiSimulator
from new_year.tamagotchi.sys_msg.sys_msg_handler import TamagotchiSysMsgHandler
from new_year_common.items.components.ny_constants import ENT_TAMAGOCHI, RaidState
from new_year.skeletons.new_year import INewYearController, INewYearTamagotchiController, ITamagotchiDataProvider, ITamagotchiWebRequester
from skeletons.festivity_factory import IFestivityFactory
from skeletons.gui.shared import IItemsCache

class NewYearTamagotchiController(INewYearTamagotchiController, EventsHandler):
    __slots__ = ('__simulator', '__sysMsgHandler', '__configNotifier', '__raidRequester',
                 '__raidData', '__receiptLimits', '__disclosedReceipts', '__raidStatistics',
                 '__boostAmount', '__raidCallback', '__em')
    _itemsCache = dependency.descriptor(IItemsCache)
    _webRequester = dependency.descriptor(ITamagotchiWebRequester)
    _dataProvider = dependency.descriptor(ITamagotchiDataProvider)
    _nyController = dependency.descriptor(INewYearController)

    def __init__(self):
        super(NewYearTamagotchiController, self).__init__()
        self.__simulator = TamagotchiSimulator()
        self.__sysMsgHandler = TamagotchiSysMsgHandler()
        self.__configNotifier = TamagotchiConfigNotifier()
        self.__raidRequester = None
        self.__raidData = {}
        self.__receiptLimits = {}
        self.__disclosedReceipts = {}
        self.__raidStatistics = {}
        self.__boostAmount = 0
        self.__raidCallback = None
        self.__em = EventManager()
        self.onRaidDataUpdated = Event(self.__em)
        return

    def init(self):
        self.__raidRequester = dependency.instance(IFestivityFactory).getRaidRequester()

    def fini(self):
        self.__cancelRaidCallback()

    def onLobbyInited(self, event):
        g_playerEvents.onClientUpdated += self.__onClientUpdated
        self.__initRaidData()

    @property
    def isEntObtained(self):
        return bool(self._itemsCache.items.stats.entitlements.get(ENT_TAMAGOCHI, False))

    @property
    def isPetVisible(self):
        return getNewYearGeneralConfig().getPetVisible()

    @property
    def __isPetVisible(self):
        return self.isEntObtained and self.isPetVisible

    def getRaidData(self):
        return self.__raidData

    def getRaidState(self):
        return self.__raidData.get('state', RaidState.NOT_ACTIVE)

    def getRaidMetaData(self):
        return {'receiptLimits': self.__receiptLimits, 
           'disclosedReceipts': self.__disclosedReceipts, 
           'raidStatistics': self.__raidStatistics}

    def getRaidBoostAmount(self):
        return self.__boostAmount

    def onConnected(self):
        self.__simulator.init()
        self.__sysMsgHandler.init()
        self._subscribe()

    def onDisconnected(self):
        g_playerEvents.onClientUpdated -= self.__onClientUpdated
        self._unsubscribe()
        self._dataProvider.reset()
        self.__configNotifier.reset()
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
          self._nyController.onPetVisibilityUpdated, self.__onPetVisibilityUpdated),
         (
          self._dataProvider.onPlayerInfoUpdated, self.__onPlayerInfoUpdated))

    def __onItemsSyncCompleted(self, *_):
        if self.__isPetVisible:
            self._itemsCache.onSyncCompleted -= self.__onItemsSyncCompleted
            self._webRequester.requestPlayerInfo()

    def syncPlayerInfo(self):
        if self.__isPetVisible:
            self._webRequester.requestPlayerInfo(self.__simulator.update)

    def __setRaccoonState(self, state):
        self._dataProvider.raccoonState = state and self.__isPetVisible and self._dataProvider.isValidConfig
        self.__simulator.setEnabled(self._dataProvider.raccoonState)

    def __onPetVisibilityUpdated(self, isEnabled):
        self.__setRaccoonState(isEnabled)
        if not isEnabled:
            self._dataProvider.resetData()
            self._itemsCache.onSyncCompleted -= self.__onItemsSyncCompleted
            return
        self._itemsCache.onSyncCompleted += self.__onItemsSyncCompleted
        self.__onItemsSyncCompleted()

    def __onPlayerInfoUpdated(self, state):
        self.__setRaccoonState(state)
        self.__configNotifier.startNotify()

    def __updateRaidState(self, shouldResetCallback=True):
        if shouldResetCallback:
            self.__cancelRaidCallback()
        startTime = self.__raidData.get('startTime', 0)
        duration = self.__raidData.get('duration')
        if not startTime or duration is None:
            self.__raidData['state'] = RaidState.NOT_ACTIVE
            return
        else:
            finishTime = startTime + duration
            remainingTime = finishTime - getServerUTCTime()
            if remainingTime < 0:
                self.__raidData['state'] = RaidState.FINISHED
                if shouldResetCallback:
                    self.__onRaidFinished()
            else:
                self.__raidData['state'] = RaidState.ACTIVE
                if shouldResetCallback:
                    self.__raidCallback = callback(remainingTime, self.__onRaidFinished)
            return

    def __cancelRaidCallback(self):
        if self.__raidCallback is not None:
            cancelCallback(self.__raidCallback)
            self.__raidCallback = None
        return

    def __onRaidFinished(self):
        self.__cancelRaidCallback()
        self.__raidData['state'] = RaidState.FINISHED
        TamagotchiSysMsgHandler.sendRaidFinished()
        self.onRaidDataUpdated()

    def __initRaidData(self, *_):
        if self.__raidRequester is None:
            return
        else:
            self.__raidData = dict(self.__raidRequester.getCurrentRaid())
            self.__receiptLimits = dict(self.__raidRequester.getReceiptLimits())
            self.__raidStatistics = dict(self.__raidRequester.getStatistics())
            self.__disclosedReceipts = dict(self.__raidRequester.getDisclosedReceipts())
            self.__boostAmount = self.__raidRequester.getBoostAmount()
            self.__updateRaidState()
            return

    def __onClientUpdated(self, diff, _):
        raidCache = diff.get('cache', {}).get(SyncDataKeys.NY_TAMAGOTCHI_RAID, {})
        raidData = raidCache.get('currentRaid')
        disclosedReceipts = raidCache.get('disclosedReceipts')
        receiptLimits = raidCache.get('receiptLimits')
        raidStatistics = raidCache.get('statistics')
        boostAmount = raidCache.get('boostAmount')
        isRaidChanged = False
        if raidData is not None:
            prevStartTime = self.__raidData.get('startTime', 0)
            prevDuration = self.__raidData.get('duration', 0)
            self.__raidData = dict(raidData)
            shouldResetCallback = prevStartTime != self.__raidData.get('startTime', 0) or prevDuration != self.__raidData.get('duration', 0)
            self.__updateRaidState(shouldResetCallback)
            isRaidChanged = True
        if disclosedReceipts is not None:
            for receiptType, receipts in disclosedReceipts.iteritems():
                self.__disclosedReceipts.setdefault(receiptType, {}).update(receipts)

            isRaidChanged = True
        if receiptLimits is not None:
            self.__receiptLimits.update(receiptLimits)
            isRaidChanged = True
        if raidStatistics is not None:
            self.__raidStatistics.update(raidStatistics)
            isRaidChanged = True
        if boostAmount is not None:
            self.__boostAmount = boostAmount
            isRaidChanged = True
        if isRaidChanged:
            self.onRaidDataUpdated()
        return