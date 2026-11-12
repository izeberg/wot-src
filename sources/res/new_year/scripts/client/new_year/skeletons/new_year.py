import typing
from adisp import adisp_async, adisp_process
from skeletons.gui.game_control import IFestivityController, IGameController, IFestivityFirstEnterVideoController
if typing.TYPE_CHECKING:
    from Event import Event
    from ..tamagotchi.dto.leaderboard import Leaderboard
    from ..tamagotchi.dto.config import Config
    from ..tamagotchi.dto.player_info import PlayerInfo
    from ..tamagotchi.dto.player_stats import PlayerStats

class INewYearController(IFestivityController):
    onDataUpdated = None
    onUpdateSlot = None
    onSetHangToyEffectEnabled = None
    onVariadicDiscountsUpdated = None
    onCustomizationObjectUpdated = None
    onSpaceObjectHover = None
    onGUIObjectHover = None
    onNySettingsChanged = None
    onOnboardingFinished = None
    onUIControlsLockChanged = None
    onPetVisibilityUpdated = None
    onPetRaidVisibilityUpdated = None

    def isEnabled(self):
        raise NotImplementedError

    def isInProgress(self):
        raise NotImplementedError

    def isPostEvent(self):
        raise NotImplementedError

    def isFinished(self):
        raise NotImplementedError

    def isSuspended(self):
        raise NotImplementedError

    def isFirstEntrance(self):
        raise NotImplementedError

    def isOnboardingOpen(self):
        raise NotImplementedError

    def isMaxAtmosphereLevel(self):
        raise NotImplementedError

    def getHangarQuestsFlagData(self):
        raise NotImplementedError

    def getHangarWidgetLinkage(self):
        raise NotImplementedError

    def getHangarEdgeColor(self):
        raise NotImplementedError

    def getSlotDescrs(self):
        raise NotImplementedError

    def getToyDescr(self, toyID):
        raise NotImplementedError

    def getToyByID(self, toyID):
        raise NotImplementedError

    def getToysByType(self, slotID):
        raise NotImplementedError

    def getAllToysByTypeFromCache(self, typeID):
        raise NotImplementedError

    def getAllCollectedToysId(self, year=None):
        raise NotImplementedError

    @adisp_async
    def hangToy(self, toyID, slotID, callback=None):
        raise NotImplementedError

    @adisp_async
    def buyToy(self, toyID, callback=None):
        raise NotImplementedError

    def getLevel(self, level):
        raise NotImplementedError

    def checkForNewToys(self, slot=None, objectType=None):
        raise NotImplementedError

    def isCollectionCompleted(self, collectionID=None):
        raise NotImplementedError

    def getFinishTime(self):
        raise NotImplementedError

    def showStateMessage(self):
        raise NotImplementedError

    def sendSeenToys(self, toyIDs):
        raise NotImplementedError

    def sendSeenToysInCollection(self, toyIDs):
        raise NotImplementedError

    def sendViewAlbum(self, settingID, rank):
        raise NotImplementedError

    def getUniqueMegaToysCount(self):
        raise NotImplementedError

    def isFullRegularToysGroup(self, typeID, settingID, rank):
        raise NotImplementedError

    def isRegularToysCollected(self):
        raise NotImplementedError

    def getMaxToysStyle(self):
        raise NotImplementedError

    def getActiveSettingBonusValue(self):
        raise NotImplementedError

    def getMaxBonusValue(self):
        raise NotImplementedError

    def getVariadicDiscountCount(self):
        raise NotImplementedError

    def updateVariadicDiscounts(self):
        raise NotImplementedError

    def markPreviousYearTabVisited(self, yearName, settingsKey):
        raise NotImplementedError

    def getCollectionAwardQuest(self, collectionTypeToQuest, collectionType, filterFunc):
        raise NotImplementedError

    @property
    def firstEnterVideo(self):
        raise NotImplementedError

    @property
    def leaderboardTankReward(self):
        raise NotImplementedError

    def isWidgetVisible(self, prbState):
        raise NotImplementedError

    def isCreditBonusVisible(self, prbState):
        raise NotImplementedError

    def setSpaceObjectHover(self, gameObject, value):
        raise NotImplementedError

    def setGuiObjectHover(self, objectName, value):
        raise NotImplementedError

    def lockUIControls(self, lockID):
        raise NotImplementedError

    def unlockUIControls(self, lockID):
        raise NotImplementedError

    def isUIControlsLocked(self):
        raise NotImplementedError

    def isLootboxBigType(self, lbType):
        raise NotImplementedError

    def isLootboxTankType(self, lbType):
        raise NotImplementedError

    @adisp_async
    @adisp_process
    def switchToNewYearPrebattle(self, callback):
        raise NotImplementedError

    @adisp_process
    def switchFromNewYearPrebattle(self):
        raise NotImplementedError

    def isNewYearBattleMode(self):
        raise NotImplementedError

    @property
    def prbNewYearActionName(self):
        raise NotImplementedError

    def isCelebVoiceoverEnabled(self):
        raise NotImplementedError

    def isQuestsCelebVoiceoverEnabled(self):
        raise NotImplementedError

    def isMachineCelebVoiceoverEnabled(self):
        raise NotImplementedError


class INewYearFirstEnterVideoController(IFestivityFirstEnterVideoController):
    pass


class INewYearSurpriseMachine(IGameController):
    onStateUpdate = None
    onMachineButtonPress = None
    onScreenButtonClick = None
    onUpdateApplyCoin = None
    onMachineButtonHovered = None
    onActivationChanged = None
    onMachineBusyStatusUpdated = None

    @property
    def machineState(self):
        raise NotImplementedError

    @property
    def canApplyCoin(self):
        raise NotImplementedError

    @property
    def canBuyCoin(self):
        raise NotImplementedError

    @property
    def isMachineBusy(self):
        raise NotImplementedError

    @property
    def isMachineActivated(self):
        raise NotImplementedError

    @property
    def selectedAmountButton(self):
        raise NotImplementedError

    def setState(self, state):
        raise NotImplementedError

    def setViewState(self, state):
        raise NotImplementedError

    def refreshApplyCoinState(self):
        raise NotImplementedError

    def updateSurpriseMachineBusyStatus(self, isBusy):
        raise NotImplementedError

    def tryActivateMachine(self):
        raise NotImplementedError

    def deactivateMachine(self):
        raise NotImplementedError

    def selectAmountButton(self, button):
        raise NotImplementedError

    def resetSelection(self):
        raise NotImplementedError


class IRaccoonAnimationController(IGameController):
    onRaidStateChanged = None
    onTvRaidPresentationChanged = None
    onTvAnimationChanged = None

    @property
    def isRaidStarted(self):
        raise NotImplementedError

    @property
    def isRaidActive(self):
        raise NotImplementedError

    @property
    def tvAnimation(self):
        raise NotImplementedError

    def setRaidActive(self, isActive):
        raise NotImplementedError

    def beginTvRaidPresentation(self):
        raise NotImplementedError

    def endRaidTvPresentation(self):
        raise NotImplementedError

    def onTvPresentationFinished(self):
        raise NotImplementedError

    def setTvAnimation(self, animation):
        raise NotImplementedError

    def activateItem(self, name):
        raise NotImplementedError

    def updateMoodState(self, state):
        raise NotImplementedError

    def setAnimationsEnabled(self, enabled):
        raise NotImplementedError


class INewYearEnvironmentSwitchController(IGameController):
    onEnvironmentSwitched = None

    @property
    def userEnvState(self):
        raise NotImplementedError

    @property
    def resolvedUserEnvState(self):
        raise NotImplementedError

    @property
    def needToShowTip(self):
        raise NotImplementedError

    @property
    def currentDayNightMode(self):
        raise NotImplementedError

    @property
    def currentAppliedDayNightMode(self):
        raise NotImplementedError

    @property
    def isAppliedDay(self):
        raise NotImplementedError

    def notifyTipShouldClose(self):
        raise NotImplementedError

    def skipSwitcherTip(self):
        raise NotImplementedError

    def applyCurrentEnvironment(self):
        raise NotImplementedError

    def switchEnvironment(self, envState, setCallback=True):
        raise NotImplementedError

    def switchDayNightMode(self, envState):
        raise NotImplementedError

    def resolveDayNightMode(self, envState):
        raise NotImplementedError

    def getTimeAngle(self):
        raise NotImplementedError


class INewYearCurrencyController(IGameController):
    onCurrencyUpdated = None
    onVisibleCurrenciesChanged = None

    @property
    def getCurrencies(self):
        raise NotImplementedError

    @property
    def getGiftMachineTokenCount(self):
        raise NotImplementedError

    @property
    def getMandarinTokenCount(self):
        raise NotImplementedError

    @property
    def getGoldCount(self):
        raise NotImplementedError

    def getCurrencyCount(self, currency):
        raise NotImplementedError

    def getCurrencyClickHandler(self, currency):
        raise NotImplementedError

    def setVisibleCurrencies(self, currencies=None):
        raise NotImplementedError


class INewYearTamagotchiController(IGameController):
    onRaidDataUpdated = None

    @property
    def isEntObtained(self):
        raise NotImplementedError

    @property
    def isPetVisible(self):
        raise NotImplementedError

    def getRaidData(self):
        raise NotImplementedError

    def getRaidState(self):
        raise NotImplementedError

    def getRaidMetaData(self):
        raise NotImplementedError

    def getRaidBoostAmount(self):
        raise NotImplementedError

    def onLobbyInited(self, event):
        raise NotImplementedError


class INewYearMetricsLogger(object):
    __slots__ = ()

    def logSwitcherOpened(self):
        raise NotImplementedError

    def logQuestsScreenClosed(self, animation):
        raise NotImplementedError

    def logQuestsVoiceoverSwitch(self, isEnabled):
        raise NotImplementedError

    def logMachineScreenOpened(self, animation):
        raise NotImplementedError

    def logMachineScreenClosed(self, animation):
        raise NotImplementedError

    def logMachineCoinExchange(self, count):
        raise NotImplementedError

    def logMachineTokenUsed(self, count):
        raise NotImplementedError

    def logLeaderboardScreenOpened(self):
        raise NotImplementedError

    def logWeeklyRewardsScreenOpened(self):
        raise NotImplementedError

    def logPetScreenOpened(self):
        raise NotImplementedError

    def logPetRepeatOnboardingClick(self, count):
        raise NotImplementedError

    def logRaidRepeatOnboardingClick(self, count):
        raise NotImplementedError

    def logEasterEggVideoOpened(self, videoId):
        raise NotImplementedError


class ITamagotchiWebRequester(object):
    __slots__ = ()

    def requestPlayerInfo(self, callback=None):
        raise NotImplementedError

    def requestLeaderboardPage(self, page=0, isUserPage=False, cumulative=False):
        raise NotImplementedError

    def requestPlayerStats(self, forFinalCache=False):
        raise NotImplementedError

    def buyItems(self, itemsDict):
        raise NotImplementedError

    def activateItem(self, itemId, count):
        raise NotImplementedError


class ITamagotchiDataProvider(object):
    __slots__ = ('onLeaderBoardUpdated', 'onPlayerInfoUpdated', 'onPlayerStatsUpdated',
                 'onRaccoonStateUpdated', 'onBonusUpdated', 'onSimulationEnd', 'onItemsActivateRequested',
                 'onItemsActivated', 'onItemsPurchased', 'onOnboardingChanged', 'onViewVisibilityChanged',
                 'onUpdateTipsRequested', 'onNextSeasonStarted', 'onSeasonEnded',
                 'onOnboardingSkipped', 'onRaidReadyUpdated', 'onTamagotchiRaidViewEnabledChanged',
                 'onDecreasedIndicatorsPoints')

    def __init__(self):
        super(ITamagotchiDataProvider, self).__init__()
        self.onLeaderBoardUpdated = None
        self.onPlayerStatsUpdated = None
        self.onRaccoonStateUpdated = None
        self.onBonusUpdated = None
        self.onSimulationEnd = None
        self.onItemsActivateRequested = None
        self.onItemsActivated = None
        self.onItemsPurchased = None
        self.onOnboardingChanged = None
        self.onOnboardingSkipped = None
        self.onViewVisibilityChanged = None
        self.onPlayerInfoUpdated = None
        self.onUpdateTipsRequested = None
        self.onNextSeasonStarted = None
        self.onSeasonEnded = None
        self.onRaidReadyUpdated = None
        self.onTamagotchiRaidViewEnabledChanged = None
        self.onDecreasedIndicatorsPoints = None
        return

    @property
    def isValidConfig(self):
        raise NotImplementedError

    @property
    def raccoonState(self):
        raise NotImplementedError

    @raccoonState.setter
    def raccoonState(self, value):
        raise NotImplementedError

    @property
    def leaderboard(self):
        raise NotImplementedError

    @leaderboard.setter
    def leaderboard(self, value):
        raise NotImplementedError

    @property
    def cumulativeLeaderboard(self):
        raise NotImplementedError

    @cumulativeLeaderboard.setter
    def cumulativeLeaderboard(self, value):
        raise NotImplementedError

    @property
    def config(self):
        raise NotImplementedError

    @config.setter
    def config(self, value):
        raise NotImplementedError

    @property
    def playerInfo(self):
        raise NotImplementedError

    @playerInfo.setter
    def playerInfo(self, value):
        raise NotImplementedError

    @property
    def initialPlayerInfo(self):
        raise NotImplementedError

    @property
    def isOnboarding(self):
        raise NotImplementedError

    @isOnboarding.setter
    def isOnboarding(self, value):
        raise NotImplementedError

    @property
    def isLeaderboardFinished(self):
        raise NotImplementedError

    @property
    def isLeaderboardRecalcPeriod(self):
        raise NotImplementedError

    @property
    def isCumulativeFinished(self):
        raise NotImplementedError

    def canCacheFinalPlayerStats(self):
        raise NotImplementedError

    @property
    def hasCumulativeLeaderboard(self):
        raise NotImplementedError

    def reset(self):
        raise NotImplementedError

    def resetData(self):
        raise NotImplementedError

    def getIndicatorCurrency(self, name):
        raise NotImplementedError

    def getDeb(self):
        raise NotImplementedError

    def getIndicatorDeb(self, name):
        raise NotImplementedError

    def getNeeds(self):
        raise NotImplementedError

    def isIndicatorLocked(self, name):
        raise NotImplementedError

    def syncOpenedIndicators(self):
        raise NotImplementedError

    def setRaidReady(self, isReady=None):
        raise NotImplementedError

    @property
    def isRaidReady(self):
        raise NotImplementedError

    def getRaidState(self):
        raise NotImplementedError

    def getRaidRemainingTime(self):
        raise NotImplementedError

    def isRaidActive(self):
        raise NotImplementedError

    def hasRaidLoot(self):
        raise NotImplementedError

    def isReadyForRaid(self):
        raise NotImplementedError

    def getIndicatorStateDecayTime(self, name):
        raise NotImplementedError

    def getIndicatorDecayTime(self, name):
        raise NotImplementedError

    def getIndicatorStates(self):
        raise NotImplementedError

    @property
    def playerStats(self):
        raise NotImplementedError

    @playerStats.setter
    def playerStats(self, value):
        raise NotImplementedError

    @property
    def playerStatsGeneration(self):
        raise NotImplementedError

    def tryStartFinalPlayerStatsRequest(self):
        raise NotImplementedError

    def allocatePlayerStatsRequestSeq(self):
        raise NotImplementedError

    def applyPlayerStats(self, value, asFinalCache=False, startedWhenFinalReady=False, requestGeneration=None, requestSeq=None):
        raise NotImplementedError

    @property
    def hasFinalPlayerStatsCache(self):
        raise NotImplementedError

    @property
    def wasInLeaderboard(self):
        raise NotImplementedError

    def getRewardedTopThreshold(self, seasonId, playerPos):
        raise NotImplementedError

    def getCumulativeReward(self):
        raise NotImplementedError

    def getPlayerStat(self, seasonId):
        raise NotImplementedError

    def getLeaderboard(self, seasonId):
        raise NotImplementedError