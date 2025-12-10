import logging
from collections import namedtuple
import typing
from wotdecorators import noexcept
import Event
from GrinchProgressionAccountSettings import getSettings, setSettings, PREVIOUS_POINTS_COUNT, IS_FIRST_ENTRY, POINTS_SEEN_COUNT, CLAIMABLE_REWARDS_SEEN_COUNT
from PlayerEvents import g_playerEvents
from account_helpers import AccountSyncData
from adisp import adisp_process, adisp_async
from grinch.skeletons.battle_controller import IGrinchController
from grinch_progression.account_helpers.account_settings import getCompletedQuests, setCompletedQuests
from grinch_progression.account_helpers.grinch_cache_manager import PDATA_KEY, GrinchCacheManager
from grinch_progression.gui.shared.gui_items.processors.processors import OpenStepForChapter
from grinch_progression.skeletons.game_controller import IGrinchProgressionController
from grinch_progression_common import getAvailableForClaimingSteps
from grinch_progression_common.grinch_progression_constants import Configs, ProgressionStates
from helpers import dependency, time_utils
from helpers.CallbackDelayer import CallbackDelayer
from helpers.time_utils import getServerUTCTime
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.server_events import IEventsCache
from skeletons.gui.shared import IItemsCache
from skeletons.gui.system_messages import ISystemMessages
if typing.TYPE_CHECKING:
    from typing import Dict
    from grinch.gui.game_control.grinch_controller import GrinchController
    from gui.shared.events import GUICommonEvent
_logger = logging.getLogger(__name__)
CURRENT_CHAPTER = 1
ClaimStats = namedtuple('ClaimStats', ['claimedPoints', 'claimedCount', 'nonClaimedPoints', 'nonClaimedCount'])

class GrinchProgressionController(IGrinchProgressionController):
    __lobbyContext = dependency.descriptor(ILobbyContext)
    __grinchCtrl = dependency.descriptor(IGrinchController)
    __itemsCache = dependency.descriptor(IItemsCache)
    __eventsCache = dependency.descriptor(IEventsCache)
    __systemMessages = dependency.descriptor(ISystemMessages)

    def __init__(self):
        super(GrinchProgressionController, self).__init__()
        self.__callbackDelayer = CallbackDelayer()
        self.__grinchConfig = None
        self.__grinchCacheManager = GrinchCacheManager()
        self._prevState = False
        self.onDataUpdated = Event.Event()
        return

    @noexcept
    def onLobbyInited(self, event):
        self._prevState = self.isEnabled
        self.__resetCompletedQuests()
        self.__setUpdateTimer()

    def fini(self):
        self.__callbackDelayer.clearCallbacks()
        self.__grinchConfig = None
        return

    def onAccountBecomePlayer(self):
        g_playerEvents.onClientUpdated += self.__onClientUpdated
        self.__lobbyContext.getServerSettings().onServerSettingsChange += self.__onServerSettingsChange
        self.__grinchCtrl.onConfigChanged += self.__updateGrinchConfig
        self.__grinchCtrl.onPrimeTimeStatusUpdated += self.__onUpdatePrimeTime

    def onAccountBecomeNonPlayer(self):
        g_playerEvents.onClientUpdated -= self.__onClientUpdated
        self.__lobbyContext.getServerSettings().onServerSettingsChange -= self.__onServerSettingsChange
        self.__grinchCtrl.onConfigChanged -= self.__updateGrinchConfig
        self.__grinchCtrl.onPrimeTimeStatusUpdated -= self.__onUpdatePrimeTime

    def onDisconnected(self):
        self.__grinchCacheManager.onDisconnected()

    @property
    def isEnabled(self):
        return self.__grinchConfig['isEnabled']

    @property
    def token(self):
        return self.getConfig().get('progressionTokenID')

    def getClaimStats(self):
        claimedPoints = 0
        claimedCount = 0
        nonClaimedPoints = 0
        nonClaimedCount = 0
        chapterConfig = self.getCurrentChapterData()
        progressionDataInt = self.__grinchCacheManager.getProgression().get(self.getCurrentChapter(), 0)
        for stepId, step in enumerate(chapterConfig.get('steps', {}), 1):
            if self.__grinchCacheManager.isChapterStepClaimed(progressionDataInt, stepId):
                claimedPoints += step['price']
                claimedCount += 1
            else:
                nonClaimedPoints += step['price']
                nonClaimedCount += 1

        return ClaimStats(claimedPoints, claimedCount, nonClaimedPoints, nonClaimedCount)

    def getNumberOfClaimableRewards(self):
        currentPoints = self.getPoints()
        numberOfClaimableRewards = 0
        for stepId, step in enumerate(self.getCurrentChapterData().get('steps', []), 1):
            if not self.isStepClaimed(self.getCurrentChapter(), stepId) and step['price'] <= currentPoints:
                numberOfClaimableRewards += 1
                currentPoints -= step['price']

        return numberOfClaimableRewards

    def getMaxPointsForCurChapter(self):
        chapter = self.getCurrentChapterData()
        return sum([ step['price'] for step in chapter.get('steps', []) ])

    @property
    def enoughForClaimReward(self):
        return len(getAvailableForClaimingSteps(self.getActiveChapters(), self.__grinchCacheManager.getProgression(), self.getPoints())) > 0

    def getProgressionState(self):
        timeTill = self.getTimeTillSeasonStart()
        if timeTill or not self.isEnabled:
            return ProgressionStates.NOT_STARTED
        if self.__anyChapterAvailable():
            return ProgressionStates.IN_PROGRESS
        return ProgressionStates.FINISHED

    def getConfig(self):
        return self.__lobbyContext.getServerSettings().getSettings().get(Configs.GRINCH_PROGRESSION_CONFIG.value)

    def getPoints(self):
        return self.__itemsCache.items.tokens.getTokenCount(self.token)

    def getTimeTillSeasonStart(self):
        timeTill = self.getStartEventDate() - getServerUTCTime()
        if timeTill < 0:
            return 0
        return timeTill

    def getCurrentChapter(self):
        return CURRENT_CHAPTER

    def getCurrentChapterData(self):
        return self.getActiveChapters().get(self.getCurrentChapter(), {})

    def getStartEventDate(self):
        seasonData = self.__getCurrentSeasonData()
        if seasonData:
            return seasonData['seasonStart']
        return 0

    def getEndEventDate(self):
        seasonData = self.__getCurrentSeasonData()
        if seasonData:
            return seasonData['seasonFinish']
        return 0

    def getCurrentSeasonChapters(self):
        return self.__getCurrentSeasonData().get('chapters', {})

    def getActiveChapters(self):
        chaptersData = self.getCurrentSeasonChapters()
        currentTime = getServerUTCTime()
        result = dict()
        for chapterID, chapterData in chaptersData.iteritems():
            if chapterData['chapterStart'] < currentTime < chapterData['chapterFinish']:
                result[chapterID] = chapterData

        return result

    def getUserProgression(self):
        return self.__grinchCacheManager.getProgression()

    def getGrinchVehicles(self):
        return self.__grinchConfig.get('vehicles', [])

    def isPostProgression(self):
        return self.getMaxChapterStep() == self.getClaimStats().claimedCount

    def getChapterDates(self, chapterId):
        chaptersData = self.getCurrentSeasonChapters()
        chapterData = chaptersData.get(chapterId)
        return (chapterData['chapterStart'], chapterData['chapterFinish'])

    def getMaxChapterStep(self):
        chaptersSteps = [ len(chapterData['steps']) for chapterData in self.getCurrentSeasonChapters().itervalues() ]
        return max(chaptersSteps)

    def getPointsSeenCount(self):
        return getSettings(POINTS_SEEN_COUNT)

    def setPointsSeenCount(self, value):
        return setSettings(POINTS_SEEN_COUNT, value)

    def getClaimableRewardsSeenCount(self):
        return getSettings(CLAIMABLE_REWARDS_SEEN_COUNT)

    def setClaimableRewardsSeenCount(self, value):
        return setSettings(CLAIMABLE_REWARDS_SEEN_COUNT, value)

    def getPreviousPointsCount(self):
        return getSettings(PREVIOUS_POINTS_COUNT)

    def setPreviousPointsCount(self, value):
        return setSettings(PREVIOUS_POINTS_COUNT, value)

    def getIsFirstEntry(self):
        return getSettings(IS_FIRST_ENTRY)

    def setIsFirstEntry(self, value):
        return setSettings(IS_FIRST_ENTRY, value)

    def isStepClaimed(self, chapterId, stepId):
        return self.__grinchCacheManager.isStepClaimed(chapterId, stepId)

    @adisp_async
    @adisp_process
    def claimReward(self, chapterID, stepID, callback):
        if not self.isEnabled:
            return
        result = yield OpenStepForChapter(chapterID, stepID).request()
        callback(result)

    def __getCurrentSeasonData(self):
        config = self.getConfig()
        currentTime = getServerUTCTime()
        firstNotStartedSeason = {}
        for _, seasonData in config.get('seasons').iteritems():
            if not firstNotStartedSeason and currentTime < seasonData['seasonStart']:
                firstNotStartedSeason = seasonData
            if seasonData['seasonStart'] < currentTime < seasonData['seasonFinish']:
                return seasonData

        return firstNotStartedSeason

    def __anyChapterAvailable(self):
        chaptersData = self.getCurrentSeasonChapters()
        currentTime = getServerUTCTime()
        for _, chapterData in chaptersData.iteritems():
            if chapterData['chapterStart'] < currentTime < chapterData['chapterFinish']:
                return True

        return False

    def getFinalStepPrice(self):
        activeChapters = self.getActiveChapters()
        return activeChapters[self.getCurrentChapter()]['finalStep']['price']

    def __updateGrinchConfig(self, _):
        self.__grinchConfig = self.__grinchCtrl.getConfig()
        self.onDataUpdated()

    def __onClientUpdated(self, diff, _):
        isFullSync = AccountSyncData.isFullSyncDiff(diff)
        self.__grinchCacheManager.synchronize(isFullSync, diff)
        if PDATA_KEY in diff or self.token in diff.get('tokens', {}):
            self.onDataUpdated()

    def __onServerSettingsChange(self, diff):
        if Configs.GRINCH_PROGRESSION_CONFIG.value in diff:
            self.onDataUpdated()

    def __onUpdatePrimeTime(self, *_):
        self.onDataUpdated()
        self.__setUpdateTimer()

    def __resetCompletedQuests(self):
        completedQuests = getCompletedQuests() or set()
        resetedSet = set()
        for qID in completedQuests:
            quest = self.__eventsCache.getQuestByID(qID)
            if quest and quest.isCompleted():
                resetedSet.add(qID)

        setCompletedQuests(resetedSet)

    def __setUpdateTimer(self):
        timeLeft = self.__grinchCtrl.getClosestStateChangeTime() - time_utils.getCurrentLocalServerTimestamp()
        if timeLeft > 0:
            self.__callbackDelayer.delayCallback(timeLeft, self.__onUpdatePrimeTime)

    def showClaimableRewards(self):
        now = time_utils.getCurrentLocalServerTimestamp()
        return self.__grinchCtrl.getAllSeasonsEndDate() < now and self.isAnyRewardAvailable()

    def isAnyRewardAvailable(self):
        return self.getNumberOfClaimableRewards() > 0 or self.getPoints() >= self.getFinalStepPrice()