import Event
from gui.ClientUpdateManager import g_clientUpdateManager
from gui.impl.gen.view_models.views.lobby.user_missions.constants.event_banner_state import EventBannerState
from gui.shared.utils.scheduled_notifications import Notifiable, PeriodicNotifier
from helpers import dependency, time_utils
from ny_common.settings import NY_CONFIG_NAME, NYGeneralConsts
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.server_events import IEventsCache
from new_year.ny_helper import getNYGeneralConfig
from skeletons.new_year import INewYearController

class HOSurpriseBannerHelper(Notifiable):
    __eventsCache = dependency.descriptor(IEventsCache)
    __nyController = dependency.descriptor(INewYearController)
    __lobbyContext = dependency.descriptor(ILobbyContext)

    def __init__(self):
        super(HOSurpriseBannerHelper, self).__init__()
        self.onTimeStatusUpdated = Event.Event()
        self.__surpriseToken = None
        return

    def onLobbyInited(self):
        self.__addEventHandlers()
        self.__surpriseToken = getNYGeneralConfig().getSurpriseToken()
        self.__update()
        self.addNotificator(PeriodicNotifier(self.__getTimer, self.__timerUpdate))
        self.startNotification()

    def __timerUpdate(self):
        self.onTimeStatusUpdated()

    def __getTimer(self):
        surpriseTokenQuest = self.__getSurpriseTokenQuest()
        if surpriseTokenQuest is not None:
            tokenIsAvailable = surpriseTokenQuest.isAvailable().isValid
            endDate = surpriseTokenQuest.getFinishTime() if tokenIsAvailable else surpriseTokenQuest.getStartTime()
            now = time_utils.getCurrentLocalServerTimestamp()
            timeLeft = endDate - now
            if timeLeft > 0:
                return timeLeft + 1
            if tokenIsAvailable:
                return timeLeft + 1
        return

    def clear(self):
        self.__removeEventHandlers()
        self.__surpriseToken = None
        self.onTimeStatusUpdated.clear()
        self.clearNotification()
        return

    def __addEventHandlers(self):
        self.__lobbyContext.getServerSettings().onServerSettingsChange += self.__onServerSettingsChanged
        self.__eventsCache.onSyncCompleted += self.__update
        self.__nyController.onStateChanged += self.__update
        g_clientUpdateManager.addCallbacks({'tokens': self.__onTokensChanged})

    def __removeEventHandlers(self):
        self.__lobbyContext.getServerSettings().onServerSettingsChange -= self.__onServerSettingsChanged
        self.__eventsCache.onSyncCompleted -= self.__update
        self.__nyController.onStateChanged -= self.__update
        g_clientUpdateManager.removeObjectCallbacks(self)

    def __onServerSettingsChanged(self, diff):
        if diff.get(NY_CONFIG_NAME, {}).get(NYGeneralConsts.CONFIG_NAME) is None:
            return
        else:
            self.__surpriseToken = getNYGeneralConfig().getSurpriseToken()
            self.__update()
            self.startNotification()
            return

    @property
    def surpriseToken(self):
        return self.__surpriseToken

    def __onTokensChanged(self, tokens):
        surpriseToken = self.surpriseToken
        if any(token for token in tokens if token == surpriseToken):
            self.__update()

    def __getSurpriseTokenQuest(self):
        return self.__eventsCache.getQuestByID(self.surpriseToken)

    def __update(self):
        self.isEntryPointAvailable()

    def isEntryPointAvailable(self):
        surpriseTokenQuest = self.__getSurpriseTokenQuest()
        isSurpriseTokenAvailable = surpriseTokenQuest and not surpriseTokenQuest.isCompleted() and (surpriseTokenQuest.isAvailable().isValid or surpriseTokenQuest.isAvailable().reason == 'in_future')
        return self.__nyController.isEnabled() and isSurpriseTokenAvailable

    def getBannerState(self):
        eventStartDate = 0
        eventEndDate = 0
        timerValue = 0
        state = EventBannerState.INACTIVE
        surpriseTokenQuest = self.__getSurpriseTokenQuest()
        if surpriseTokenQuest is not None and self.__nyController.isEnabled():
            timeStamp = surpriseTokenQuest.getFinishTime() if surpriseTokenQuest.isAvailable().isValid else surpriseTokenQuest.getStartTime()
            remainingTime = timeStamp - time_utils.getServerUTCTime()
            eventStartDate = surpriseTokenQuest.getStartTime()
            eventEndDate = surpriseTokenQuest.getFinishTime()
            timerValue = remainingTime
            state = EventBannerState.INTRO if surpriseTokenQuest.isAvailable().isValid else EventBannerState.INACTIVE
        return (state, eventStartDate, eventEndDate, timerValue)