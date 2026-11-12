import logging
from Event import Event, EventManager, EventsSubscriber
from constants import Configs
from gui.shared.utils.scheduled_notifications import SimpleNotifier
from helpers import dependency
from helpers.server_settings import CustomizationResourceConfig, serverSettingsChangeListener
from helpers.time_utils import ONE_DAY, getDateTimeInLocal, getServerUTCTime, getTimestampFromLocal
from skeletons.gui.game_control import ICustomizationResourceController
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.shared import IItemsCache
_logger = logging.getLogger(__name__)
EVENT_TYPE_NAME = 'CustomizationResource'
_ENDING_TIME_OFFSET = ONE_DAY * 1
CUSTOMIZATION_RESOURCE_EVENT_STATE = {'Active': 'Active', 
   'Paused': 'Paused', 
   'Disabled': 'Disabled'}

class CustomizationResourceController(ICustomizationResourceController):
    __lobbyContext = dependency.descriptor(ILobbyContext)
    __itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self):
        super(CustomizationResourceController, self).__init__()
        self.__eventsManager = EventManager()
        self.__eventsSubscriber = EventsSubscriber()
        self.__notifier = SimpleNotifier(self.__getTimeLeft, self.__onEventStateChanged)
        self.onEventSettingsUpdated = Event(self.__eventsManager)
        self.__endDate = 0
        self.__startDate = 0

    @property
    def config(self):
        if self.__lobbyContext:
            return self.__lobbyContext.getServerSettings().customizationResourceConfig
        _logger.error('[customizationResourceConfig]: attempt to access customizationResourceConfig config before it is created')
        return CustomizationResourceConfig.defaults()

    def getStartTime(self):
        return self.__startDate

    def getExpiryTime(self):
        return self.__endDate

    def getCurrencyCode(self):
        return self.config.currencyCode

    def getCurrencyBalance(self):
        return self.__itemsCache.items.stats.dynamicCurrencies.get(self.getCurrencyCode(), 0)

    def isExchangeEnabled(self):
        return self.config.customizationExchange

    def isEnabled(self):
        currentTime = getServerUTCTime()
        return self.config.isEnabled and self.__startDate <= currentTime < self.__endDate

    def isFinished(self):
        return getServerUTCTime() >= self.__endDate

    def isStarted(self):
        return getServerUTCTime() >= self.__startDate

    def isEnding(self):
        currentTime = getServerUTCTime()
        return self.isEnabled() and currentTime >= self.__endDate - _ENDING_TIME_OFFSET

    def onLobbyInited(self, event):
        self.__eventsSubscriber.subscribeToEvent(self.__lobbyContext.getServerSettings().onServerSettingsChange, self.__onServerSettingsChange)
        self.__updateEventSettings()
        self.__notifier.startNotification()

    def onAccountBecomeNonPlayer(self):
        self.__stop()

    def onDisconnected(self):
        self.__stop()

    def fini(self):
        self.__stop()
        self.__notifier.clear()
        self.__eventsManager.clear()

    def getLocalEndDate(self):
        return getTimestampFromLocal(getDateTimeInLocal(self.getExpiryTime()).timetuple())

    def getLocalStartDate(self):
        return getTimestampFromLocal(getDateTimeInLocal(self.getStartTime()).timetuple())

    @serverSettingsChangeListener(Configs.CUSTOMIZATION_RESOURCE_CONFIG.value)
    def __onServerSettingsChange(self, _):
        self.__updateEventSettings()
        self.__notifier.startNotification()
        self.onEventSettingsUpdated()

    def __updateEventSettings(self):
        config = self.config
        self.__startDate = config.startDate
        self.__endDate = config.endDate
        if self.__startDate > self.__endDate:
            _logger.error('Wrong Customization Resource time date range')

    def __getTimeLeft(self):
        if not self.config.isEnabled:
            return 0
        currentTime = getServerUTCTime()
        if currentTime < self.__startDate:
            return self.__startDate - currentTime
        if currentTime < self.__endDate:
            return self.__endDate - currentTime
        return 0

    def __onEventStateChanged(self):
        self.onEventSettingsUpdated()

    def __stop(self):
        self.__eventsSubscriber.unsubscribeFromAllEvents()
        self.__notifier.stopNotification()