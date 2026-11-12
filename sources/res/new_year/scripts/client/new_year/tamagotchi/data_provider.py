import copy, itertools, typing, Event
from account_helpers.settings_core.settings_constants import NewYearStorageKeys
from helpers import dependency
from helpers.time_utils import getServerUTCTime, ONE_MINUTE
from new_year.skeletons.new_year import ITamagotchiDataProvider, INewYearTamagotchiController
from new_year.gui.impl.gen.view_models.views.lobby.new_year.receipts_panel import TabId
from new_year.tamagotchi.dto.player_info import PlayerInfo
from new_year.tamagotchi.dto.player_stats import PlayerStats
from new_year.tamagotchi.readers import readTamagotchiConfig, readTamagotchiLeaderboard, readTamagotchiLeaderboardUser, readTamagotchiPlayerInfo, readTamagotchiPlayerStats
from new_year.tamagotchi.dto.leaderboard import Leaderboard
from new_year.tamagotchi.dto.config import Config
from skeletons.account_helpers.settings_core import ISettingsCore
from skeletons.gui.shared import IItemsCache
from shared_utils import findFirst
from new_year.helpers.server_settings import getNewYearGeneralConfig
from new_year.ny_constants import NY_CUMULATIVE_LEADERBOARD_SEASON_ID
from new_year.helpers.ny_leaderboard_tank_reward import extractVehicleCD
from new_year_common.items.components.ny_constants import ENT_TAMAGOCHI, RaidState
_INDICATOR_ENT_REQUIREMENTS = {'food': 1, 
   'fun': 2, 
   'activity': 3}

class TamagotchiDataProvider(ITamagotchiDataProvider):
    __slots__ = ('__config', '__leaderboard', '__cumulativeLeaderboard', '__playerInfo',
                 '__playerStats', '__finalPlayerStatsCached', '__wasInLeaderboard',
                 '__playerStatsGeneration', '__finalPlayerStatsRequestInFlight',
                 '__playerStatsRequestSeq', '__lastAppliedPlayerStatsSeq', '__simulationInfo',
                 '__indicatorStates', '__raccoonState', '__isRaidReady', '__eventManager',
                 '__debValue', '__currentRaidTab')
    _itemsCache = dependency.descriptor(IItemsCache)
    _settingsCore = dependency.descriptor(ISettingsCore)
    __tamagotchiController = dependency.descriptor(INewYearTamagotchiController)

    def __init__(self):
        super(TamagotchiDataProvider, self).__init__()
        self.__config = Config.Dto()
        self.__leaderboard = Leaderboard.Dto()
        self.__cumulativeLeaderboard = Leaderboard.Dto()
        self.__playerInfo = PlayerInfo.Dto()
        self.__simulationInfo = PlayerInfo.Dto()
        self.__playerStats = PlayerStats.Dto()
        self.__finalPlayerStatsCached = False
        self.__wasInLeaderboard = False
        self.__playerStatsGeneration = 0
        self.__finalPlayerStatsRequestInFlight = False
        self.__playerStatsRequestSeq = 0
        self.__lastAppliedPlayerStatsSeq = 0
        self.__indicatorStates = dict()
        self.__raccoonState = False
        self.__isRaidReady = False
        self.__debValue = 0
        self.__currentRaidTab = TabId.PUBLIC
        self.__eventManager = Event.EventManager()
        self.onLeaderBoardUpdated = Event.Event(self.__eventManager)
        self.onPlayerStatsUpdated = Event.Event(self.__eventManager)
        self.onRaccoonStateUpdated = Event.Event(self.__eventManager)
        self.onBonusUpdated = Event.Event(self.__eventManager)
        self.onSimulationEnd = Event.Event(self.__eventManager)
        self.onItemsActivateRequested = Event.Event(self.__eventManager)
        self.onItemsActivated = Event.Event(self.__eventManager)
        self.onItemsPurchased = Event.Event(self.__eventManager)
        self.onOnboardingChanged = Event.Event(self.__eventManager)
        self.onOnboardingSkipped = Event.Event(self.__eventManager)
        self.onViewVisibilityChanged = Event.Event(self.__eventManager)
        self.onPlayerInfoUpdated = Event.Event(self.__eventManager)
        self.onUpdateTipsRequested = Event.Event(self.__eventManager)
        self.onNextSeasonStarted = Event.Event(self.__eventManager)
        self.onSeasonEnded = Event.Event(self.__eventManager)
        self.onRaidReadyUpdated = Event.Event(self.__eventManager)
        self.onTamagotchiRaidViewEnabledChanged = Event.Event(self.__eventManager)
        self.onDecreasedIndicatorsPoints = Event.Event(self.__eventManager)

    def reset(self):
        self.resetData()
        self.__eventManager.clear()

    def resetData(self):
        self.__config = Config.Dto()
        self.__leaderboard = Leaderboard.Dto()
        self.__cumulativeLeaderboard = Leaderboard.Dto()
        self.__playerInfo = PlayerInfo.Dto()
        self.__simulationInfo = PlayerInfo.Dto()
        self.__playerStats = PlayerStats.Dto()
        self.__finalPlayerStatsCached = False
        self.__wasInLeaderboard = False
        self.__playerStatsGeneration += 1
        self.__finalPlayerStatsRequestInFlight = False
        self.__playerStatsRequestSeq = 0
        self.__lastAppliedPlayerStatsSeq = 0
        self.__indicatorStates = dict()
        self.__raccoonState = False
        self.__isRaidReady = False
        self.__debValue = 0
        self.__currentRaidTab = TabId.PUBLIC

    @property
    def isValidConfig(self):
        return self.config and self.config.startTime <= getServerUTCTime() <= self.config.endTime

    @property
    def debValue(self):
        return self.__debValue

    @debValue.setter
    def debValue(self, value):
        self.__debValue = value

    @property
    def currentSeason(self):
        if not self.isValidConfig:
            return
        else:
            if self.config.currentSeason is not None:
                return self.config.currentSeason
            seasons = self.config.seasons
            if not seasons:
                return
            now = getServerUTCTime()
            for season in seasons:
                if season.startTime <= now <= season.endTime:
                    return season

            for season in reversed(seasons):
                if season.endTime <= now:
                    return season

            return seasons[(-1)]

    @property
    def isLeaderboardFinished(self):
        return self.isValidConfig and self.config.seasons and getServerUTCTime() > self.config.seasons[(-1)].endTime

    @property
    def isLeaderboardRecalcPeriod(self):
        if not self.isValidConfig or not self.config.seasons:
            return False
        now = getServerUTCTime()
        if now < self.config.seasons[0].startTime:
            return False
        if self.isLeaderboardFinished:
            return self._isLastWeekRewardPeriod(now)
        if self._isRecalcTimeActive(self.__leaderboard, now):
            return True
        return self.isScheduleBetweenSeasons(now)

    def _isLastWeekRewardPeriod(self, now):
        lastSeason = self.config.seasons[(-1)]
        if lastSeason.rewardTime and now <= lastSeason.rewardTime:
            return True
        return self._isRecalcTimeActive(self.__leaderboard, now)

    def _isRecalcTimeActive(self, leaderboard, now):
        if not leaderboard.isRecalcTime or not leaderboard.updateTime:
            return False
        return now < leaderboard.nextUpdateTime

    def isScheduleBetweenSeasons(self, now=None):
        if not self.isValidConfig or not self.config.seasons:
            return False
        now = now or getServerUTCTime()
        if now < self.config.seasons[0].startTime or self.isLeaderboardFinished:
            return False
        return not any(season.startTime <= now <= season.endTime for season in self.config.seasons)

    @property
    def isCumulativeFinished(self):
        cumulative = self.config.cumulative if self.isValidConfig else None
        return bool(cumulative) and getServerUTCTime() > cumulative.endTime

    def canCacheFinalPlayerStats(self):
        if not self.isLeaderboardFinished:
            return False
        weekly = self.__leaderboard
        if not weekly.updateTime or weekly.isRecalcTime:
            return False
        if self.hasCumulativeLeaderboard:
            cumulative = self.__cumulativeLeaderboard
            if not cumulative.updateTime or cumulative.isRecalcTime:
                return False
        return True

    @property
    def hasCumulativeLeaderboard(self):
        return bool(self.isValidConfig and self.config.cumulative)

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
        self.__setLeaderboardData(value, cumulative=False)

    @property
    def cumulativeLeaderboard(self):
        return self.__cumulativeLeaderboard

    @cumulativeLeaderboard.setter
    def cumulativeLeaderboard(self, value):
        self.__setLeaderboardData(value, cumulative=True)

    def __setLeaderboardData(self, value, cumulative):
        isSuccess = value is not None
        if isSuccess:
            primary = readTamagotchiLeaderboard(value, cumulative=cumulative)
            other = self.__leaderboard if cumulative else self.__cumulativeLeaderboard
            if cumulative:
                self.__cumulativeLeaderboard = primary
            else:
                self.__leaderboard = primary
            user = readTamagotchiLeaderboardUser(value, cumulative=not cumulative)
            if user is not None:
                other.user = user
                if not other.updateTime:
                    other.updateTime = primary.updateTime
        self.onLeaderBoardUpdated(isSuccess)
        return

    @property
    def playerInfo(self):
        return self.__simulationInfo

    @playerInfo.setter
    def playerInfo(self, value):
        isSuccess = value is not None
        if isSuccess:
            self.__playerInfo = readTamagotchiPlayerInfo(value, self.playerInfo)
            self.__simulationInfo = copy.deepcopy(self.__playerInfo)
            self.__normalizeOpenedIndicators()
        self.onPlayerInfoUpdated(isSuccess)
        if isSuccess:
            self.setRaidReady()
        else:
            self.setRaidReady(False)
        return

    @property
    def playerStats(self):
        return self.__playerStats

    @playerStats.setter
    def playerStats(self, value):
        self.applyPlayerStats(value, asFinalCache=False, startedWhenFinalReady=False, requestGeneration=self.__playerStatsGeneration, requestSeq=None)
        return

    @property
    def playerStatsGeneration(self):
        return self.__playerStatsGeneration

    def tryStartFinalPlayerStatsRequest(self):
        if self.__finalPlayerStatsCached or self.__finalPlayerStatsRequestInFlight:
            return False
        if not self.canCacheFinalPlayerStats():
            return False
        self.__finalPlayerStatsRequestInFlight = True
        return True

    def allocatePlayerStatsRequestSeq(self):
        self.__playerStatsRequestSeq += 1
        return self.__playerStatsRequestSeq

    def applyPlayerStats(self, value, asFinalCache=False, startedWhenFinalReady=False, requestGeneration=None, requestSeq=None):
        if requestGeneration is not None and requestGeneration != self.__playerStatsGeneration:
            return
        else:
            if asFinalCache:
                self.__finalPlayerStatsRequestInFlight = False
            isSuccess = value is not None
            if isSuccess:
                if self.__finalPlayerStatsCached and not startedWhenFinalReady:
                    self.onPlayerStatsUpdated(True)
                    return
                staleStatsWrite = requestSeq is not None and requestSeq < self.__lastAppliedPlayerStatsSeq
                parsedStats = readTamagotchiPlayerStats(value)
                if not staleStatsWrite:
                    self.__playerStats = parsedStats
                    if requestSeq is not None:
                        self.__lastAppliedPlayerStatsSeq = requestSeq
                if asFinalCache and not self.__finalPlayerStatsCached and self.canCacheFinalPlayerStats():
                    self.__wasInLeaderboard = self.__calcWasInLeaderboard(parsedStats)
                    self.__finalPlayerStatsCached = True
            self.onPlayerStatsUpdated(isSuccess)
            return

    @property
    def hasFinalPlayerStatsCache(self):
        return self.__finalPlayerStatsCached

    @property
    def wasInLeaderboard(self):
        return self.__wasInLeaderboard

    @staticmethod
    def __calcWasInLeaderboard(stats):
        return any(weekStat.position or weekStat.point for weekStat in itertools.chain(stats.weekStats, stats.cumulativeStats))

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
    def isTamagotchiRaidViewEnabled(self):
        return self._settingsCore.serverSettings.getNewYearStorage().get(NewYearStorageKeys.NY_TAMAGOTCHI_RAID_VIEW_ENABLED, False)

    @isTamagotchiRaidViewEnabled.setter
    def isTamagotchiRaidViewEnabled(self, value):
        if not value or self.isTamagotchiRaidViewEnabled:
            return
        self._settingsCore.serverSettings.saveInNewYearStorage({NewYearStorageKeys.NY_TAMAGOTCHI_RAID_VIEW_ENABLED: True})
        self.onTamagotchiRaidViewEnabledChanged(True)

    @property
    def isOnboarding(self):
        return not bool(self._settingsCore.serverSettings.getNewYearStorage().get(NewYearStorageKeys.NY_TAMAGOTCHI_TUTORIAL_COMPLETED, 0))

    @isOnboarding.setter
    def isOnboarding(self, value):
        if self.isOnboarding != value:
            self._settingsCore.serverSettings.saveInNewYearStorage({NewYearStorageKeys.NY_TAMAGOTCHI_TUTORIAL_COMPLETED: not value})
            self.onOnboardingChanged(value)
            if not value:
                self.setRaidReady()

    @property
    def currentRaidTab(self):
        return self.__currentRaidTab

    @currentRaidTab.setter
    def currentRaidTab(self, value):
        self.__currentRaidTab = value

    def getIndicatorCurrency(self, name):
        if not self.isValidConfig:
            return -1
        name = self.config.indicators[name].item.dynCurrencyCode
        return self._itemsCache.items.stats.dynamicCurrencies.get(name, -1)

    def getDeb(self):
        config = getNewYearGeneralConfig()
        if not config.getPetVisible():
            return config.getEmergencyDEB()
        return self.debValue

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

    def isIndicatorLocked(self, name):
        entCount = self._itemsCache.items.stats.entitlements.get(ENT_TAMAGOCHI, 0)
        requiredEntCount = _INDICATOR_ENT_REQUIREMENTS.get((name or '').lower())
        return requiredEntCount is None or entCount < requiredEntCount

    def syncOpenedIndicators(self):
        changed = self.__normalizeOpenedIndicators()
        self.setRaidReady()
        return changed

    def setRaidReady(self, isReady=None):
        isReady = self.__evaluateRaidReady() if isReady is None else bool(isReady)
        if not self.isOnboarding and (isReady or self.getRaidState() != RaidState.NOT_ACTIVE):
            self.isTamagotchiRaidViewEnabled = True
        if self.__isRaidReady == isReady:
            return
        else:
            self.__isRaidReady = isReady
            self.onRaidReadyUpdated(self.isReadyForRaid())
            return

    def __normalizeOpenedIndicators(self):
        if not self.config or not self.__simulationInfo.indicators:
            return False
        changed = False
        for name in self.config.indicators.iterkeys():
            if self.isIndicatorLocked(name):
                continue
            for info in (self.__simulationInfo, self.__playerInfo):
                if info.indicators.get(name, -1) < 0:
                    info.indicators[name] = 0
                    changed = True

        return changed

    def __evaluateRaidReady(self):
        if not self.config or not self.config.indicators:
            return False
        indicators = self.__simulationInfo.indicators
        threshold = self.__config.raidScalePoint
        for name in self.config.indicators.iterkeys():
            if self.isIndicatorLocked(name):
                continue
            value = max(0, indicators.get(name, -1))
            if value < threshold:
                return False

        return True

    @property
    def isRaidReady(self):
        return self.__isRaidReady

    def getRaidState(self):
        return self.__tamagotchiController.getRaidState()

    def getRaidRemainingTime(self):
        if self.getRaidState() != RaidState.ACTIVE:
            return 0
        raidData = self.__tamagotchiController.getRaidData() or {}
        startTime = raidData.get('startTime', 0)
        duration = raidData.get('duration', 0)
        if not startTime or not duration:
            return 0
        return max(0, int(startTime + duration - getServerUTCTime()))

    def isRaidActive(self):
        return self.getRaidState() == RaidState.ACTIVE

    def hasRaidLoot(self):
        return self.getRaidState() == RaidState.FINISHED

    def isReadyForRaid(self):
        return self.__isRaidReady and self.getRaidState() == RaidState.NOT_ACTIVE

    def getIndicatorStateDecayTime(self, name):
        if name not in self.__indicatorStates:
            return 0
        index = self.__indicatorStates[name]
        level = self.__config.indicators[name].levels[index]
        return ONE_MINUTE * (self.__simulationInfo.indicators[name] - level.points) / level.degradation

    def getIndicatorDecayTime(self, name):
        if name not in self.__indicatorStates:
            return 0
        else:
            result = self.getIndicatorStateDecayTime(name)
            index = self.__indicatorStates[name]
            it, nextIt = itertools.tee(reversed(self.__config.indicators[name].levels))
            next(nextIt, None)
            for level in it:
                nextLevel = next(nextIt, None)
                if level.state > index or nextLevel is None:
                    continue
                points = max(0, level.points - nextLevel.points - 1)
                result += ONE_MINUTE * points / nextLevel.degradation

            return result

    def getIndicatorStates(self):
        return self.__indicatorStates

    def getPlayerWeekStat(self, seasonId):
        if self.playerStats:
            return findFirst(lambda weekStat: weekStat.week == seasonId, self.playerStats.weekStats)
        else:
            return

    def getPlayerCumulativeStat(self, seasonId):
        if not self.playerStats or not self.playerStats.cumulativeStats:
            return None
        if seasonId == NY_CUMULATIVE_LEADERBOARD_SEASON_ID:
            return self.playerStats.cumulativeStats[0]
        else:
            return findFirst(lambda weekStat: weekStat.week == seasonId, self.playerStats.cumulativeStats)

    def getPlayerStat(self, seasonId):
        if seasonId == NY_CUMULATIVE_LEADERBOARD_SEASON_ID:
            return self.getPlayerCumulativeStat(seasonId)
        return self.getPlayerWeekStat(seasonId)

    def getLeaderboard(self, seasonId):
        if seasonId == NY_CUMULATIVE_LEADERBOARD_SEASON_ID:
            return self.cumulativeLeaderboard
        return self.leaderboard

    def getRewardedTopThreshold(self, seasonId, playerPos):
        if seasonId == NY_CUMULATIVE_LEADERBOARD_SEASON_ID:
            cumulative = self.config.cumulative
            if cumulative is None:
                return -1
            return self.getRewardedTopThresholdForTops(cumulative.topConfig, playerPos)
        else:
            season = findFirst(lambda season: season.id == seasonId, self.config.seasons)
            if season is None:
                return -1
            return self.getRewardedTopThresholdForTops(season.topConfig, playerPos)

    def getRewardedTopThresholdForTops(self, tops, playerPos):
        if not tops:
            return -1
        minEdge = min(top.startPos for top in tops)
        maxEdge = max(top.endPos for top in tops)
        if playerPos == 0:
            return -1
        if playerPos == -1 or playerPos > maxEdge:
            return 0
        if playerPos < minEdge:
            return minEdge
        for top in reversed(tops):
            if top.startPos <= playerPos <= top.endPos:
                return top.endPos

        return -1

    def updateCurrentSeason(self):
        if not self.isValidConfig:
            return
        else:
            self.__config.currentSeason = None
            for season in self.config.seasons:
                if season.startTime <= getServerUTCTime() <= season.endTime:
                    self.__config.currentSeason = season
                    return

            return

    def getCumulativeReward(self):
        cumulative = self.config.cumulative
        if cumulative is None:
            return
        else:
            return extractVehicleCD(cumulative.drawReward.rewards)