import copy, typing, Event
from account_helpers.settings_core.settings_constants import NewYearStorageKeys
from helpers import dependency
from helpers.time_utils import getServerUTCTime, ONE_MINUTE
from new_year.skeletons.new_year import ITamagotchiDataProvider
from new_year.tamagotchi.dto.player_info import PlayerInfo
from new_year.tamagotchi.dto.player_stats import PlayerStats
from new_year.tamagotchi.readers import readTamagotchiConfig, readTamagotchiLeaderboard, readTamagotchiPlayerInfo, readTamagotchiPlayerStats
from new_year.tamagotchi.dto.leaderboard import Leaderboard
from new_year.tamagotchi.dto.config import Config
from skeletons.account_helpers.settings_core import ISettingsCore
from skeletons.gui.shared import IItemsCache
from shared_utils import findFirst

class TamagotchiDataProvider(ITamagotchiDataProvider):
    __slots__ = ('__config', '__leaderboard', '__playerInfo', '__playerStats', '__simulationInfo',
                 '__indicatorStates', '__raccoonState', '__eventManager')
    _itemsCache = dependency.descriptor(IItemsCache)
    _settingsCore = dependency.descriptor(ISettingsCore)

    def __init__(self):
        super(TamagotchiDataProvider, self).__init__()
        self.__config = Config.Dto()
        self.__leaderboard = Leaderboard.Dto()
        self.__playerInfo = PlayerInfo.Dto()
        self.__simulationInfo = PlayerInfo.Dto()
        self.__playerStats = PlayerStats.Dto()
        self.__indicatorStates = dict()
        self.__raccoonState = False
        self.__eventManager = Event.EventManager()
        self.onLeaderBoardUpdated = Event.Event(self.__eventManager)
        self.onPlayerStatsUpdated = Event.Event(self.__eventManager)
        self.onRaccoonStateUpdated = Event.Event(self.__eventManager)
        self.onBonusUpdated = Event.Event(self.__eventManager)
        self.onGiftCountUpdated = Event.Event(self.__eventManager)
        self.onSimulationEnd = Event.Event(self.__eventManager)
        self.onItemsActivateRequested = Event.Event(self.__eventManager)
        self.onItemsActivated = Event.Event(self.__eventManager)
        self.onItemsPurchased = Event.Event(self.__eventManager)
        self.onOnboardingChanged = Event.Event(self.__eventManager)
        self.onGiftObtained = Event.Event(self.__eventManager)
        self.onViewVisibilityChanged = Event.Event(self.__eventManager)
        self._onPlayerInfoUpdated = Event.Event(self.__eventManager)
        self.onMailRewards = Event.Event(self.__eventManager)
        self.onUpdateTipsRequested = Event.Event(self.__eventManager)

    def reset(self):
        self.__config = Config.Dto()
        self.__leaderboard = Leaderboard.Dto()
        self.__playerInfo = PlayerInfo.Dto()
        self.__simulationInfo = PlayerInfo.Dto()
        self.__playerStats = PlayerStats.Dto()
        self.__indicatorStates = dict()
        self.__raccoonState = False
        self.__eventManager.clear()

    @property
    def isValidConfig(self):
        return self.config and self.config.startTime <= getServerUTCTime() <= self.config.endTime

    @property
    def currentSeason(self):
        if self.isValidConfig:
            return self.config.currentSeason or self.config.seasons[(-1)]
        else:
            return

    @property
    def config(self):
        return self.__config

    @config.setter
    def config(self, value):
        if value is not None:
            self.__config = readTamagotchiConfig(value)
        return

    @property
    def leaderboard(self):
        return self.__leaderboard

    @leaderboard.setter
    def leaderboard(self, value):
        isSuccess = value is not None
        if isSuccess:
            self.__leaderboard = readTamagotchiLeaderboard(value)
        self.onLeaderBoardUpdated(isSuccess)
        return

    @property
    def playerInfo(self):
        return self.__simulationInfo

    @playerInfo.setter
    def playerInfo(self, value):
        isSuccess = value is not None
        if isSuccess:
            self.__playerInfo = readTamagotchiPlayerInfo(value)
            self.__simulationInfo = copy.deepcopy(self.__playerInfo)
        self._onPlayerInfoUpdated(isSuccess)
        return

    @property
    def playerStats(self):
        return self.__playerStats

    @playerStats.setter
    def playerStats(self, value):
        isSuccess = value is not None
        if isSuccess:
            self.__playerStats = readTamagotchiPlayerStats(value)
        self.onPlayerStatsUpdated(isSuccess)
        return

    @property
    def initialPlayerInfo(self):
        return self.__playerInfo

    @property
    def raccoonState(self):
        return self.__raccoonState

    @raccoonState.setter
    def raccoonState(self, value):
        if self.__raccoonState != value:
            self.__raccoonState = value
            self.onRaccoonStateUpdated(value)

    @property
    def isOnboarding(self):
        return not bool(self._settingsCore.serverSettings.getNewYearStorage().get(NewYearStorageKeys.NY_TAMAGOTCHI_TUTORIAL_COMPLETED, 0))

    @isOnboarding.setter
    def isOnboarding(self, value):
        if self.isOnboarding != value:
            self._settingsCore.serverSettings.saveInNewYearStorage({NewYearStorageKeys.NY_TAMAGOTCHI_TUTORIAL_COMPLETED: not value})
            self.onOnboardingChanged(value)

    def getIndicatorCurrency(self, name):
        if not self.isValidConfig:
            return -1
        name = self.config.indicators[name].item.dynCurrencyCode
        return self._itemsCache.items.stats.dynamicCurrencies.get(name, -1)

    def getDeb(self):
        clientTime = getServerUTCTime()
        for bonus in self.__simulationInfo.debHistory:
            if bonus.expirationTime >= clientTime:
                return bonus.value

        return 0

    def getIndicatorDeb(self, name):
        if name not in self.__indicatorStates:
            return 0
        index = self.__indicatorStates[name]
        return self.__config.indicators[name].levels[index].debPercent

    def getNeeds(self):
        result = []
        for name, config in self.config.indicators.iteritems():
            if name in self.__indicatorStates and self.__indicatorStates[name] < config.levels[(-1)].state:
                result.append(name)

        return result

    def getIndicatorStateDecayTime(self, name):
        if name not in self.__indicatorStates:
            return 0
        index = self.__indicatorStates[name]
        level = self.__config.indicators[name].levels[index]
        return ONE_MINUTE * (self.__simulationInfo.indicators[name] - level.points) / level.degradation

    def getGiftDelay(self):
        return self.playerInfo.giftTime - getServerUTCTime()

    def getIndicatorDecayTime(self, name):
        if name not in self.__indicatorStates:
            return 0
        result = 0
        index = self.__indicatorStates[name]
        for level in reversed(self.__config.indicators[name].levels):
            if level.state > index:
                continue
            elif level.state == index:
                result = self.getIndicatorStateDecayTime(name)
            points = max(0, level.points - 1)
            result += ONE_MINUTE * points / level.degradation

        return result

    def getIndicatorStates(self):
        return self.__indicatorStates

    def getPlayerWeekStat(self, seasonId):
        if self.playerStats:
            return findFirst(lambda weekStat: weekStat.week == seasonId, self.playerStats.weekStats)
        else:
            return

    def getRewardedTopThreshold(self, seasonId):
        playerWeekStat = self.getPlayerWeekStat(seasonId)
        if playerWeekStat is None:
            return -1
        else:
            season = findFirst(lambda season: season.id == seasonId, self.config.seasons)
            if season is None:
                return -1
            tops = season.topConfig
            playerPos = playerWeekStat.position
            minEdge = min(top.startPos for top in tops)
            maxEdge = max(top.endPos for top in tops)
            if playerPos < minEdge:
                return minEdge
            if playerPos > maxEdge:
                return 0
            for top in reversed(tops):
                if top.startPos <= playerPos <= top.endPos:
                    return top.endPos

            return -1