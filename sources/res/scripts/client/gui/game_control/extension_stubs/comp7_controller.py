import Event
from skeletons.gui.game_control import IComp7Controller
from gui.periodic_battles.models import PrimeTimeStatus

class Comp7Controller(IComp7Controller):

    def __init__(self):
        super(Comp7Controller, self).__init__()
        self.__eventsManager = em = Event.EventManager()
        self.onStatusUpdated = Event.Event(em)
        self.onStatusTick = Event.Event(em)
        self.onRankUpdated = Event.Event(em)
        self.onModeConfigChanged = Event.Event(em)
        self.onComp7RanksConfigChanged = Event.Event(em)
        self.onBanUpdated = Event.Event(em)
        self.onOfflineStatusUpdated = Event.Event(em)
        self.onQualificationBattlesUpdated = Event.Event(em)
        self.onQualificationStateUpdated = Event.Event(em)
        self.onSeasonPointsUpdated = Event.Event(em)
        self.onComp7RewardsConfigChanged = Event.Event(em)
        self.onHighestRankAchieved = Event.Event(em)
        self.onEntitlementsUpdated = Event.Event(em)
        self.onEntitlementsUpdateFailed = Event.Event(em)

    @property
    def rating(self):
        return 0

    @property
    def isElite(self):
        return False

    @property
    def isBanned(self):
        return False

    @property
    def banDuration(self):
        return 0

    @property
    def isOffline(self):
        return False

    @property
    def leaderboard(self):
        return

    @property
    def activityPoints(self):
        return 0

    @property
    def battleModifiers(self):
        return ()

    @property
    def qualificationBattlesNumber(self):
        return 0

    @property
    def qualificationBattlesStatuses(self):
        return []

    @property
    def qualificationState(self):
        return

    @property
    def remainingOfferTokensNotifications(self):
        return []

    def fini(self):
        self.__eventsManager.clear()

    def isAvailable(self):
        return False

    def isBattlesPossible(self):
        return False

    def isInPrimeTime(self):
        return False

    def isFrozen(self):
        return True

    def isNotSet(self, now=None, peripheryID=None):
        return True

    def isWithinSeasonTime(self, seasonID):
        return False

    def hasAnySeason(self):
        return False

    def hasAvailablePrimeTimeServers(self, now=None):
        return False

    def hasConfiguredPrimeTimeServers(self, now=None):
        return False

    def hasPrimeTimesLeftForCurrentCycle(self):
        return False

    def getClosestStateChangeTime(self, now=None):
        return 0

    def getCurrentCycleID(self):
        return

    def getCurrentCycleInfo(self):
        return (
         None, False)

    def getCurrentOrNextActiveCycleNumber(self, season):
        return 0

    def getEventEndTimestamp(self):
        return

    def getModeSettings(self):
        return

    def getRanksConfig(self):
        return

    def getYearlyRewards(self):
        return

    def getNextSeason(self, now=None):
        return

    def getPeriodInfo(self, now=None, peripheryID=None):
        return

    def getPrimeTimes(self):
        return {}

    def getPrimeTimesForDay(self, selectedTime, groupIdentical=False):
        return {}

    def getPrimeTimeStatus(self, now=None, peripheryID=None):
        return (PrimeTimeStatus.NOT_SET, 0, False)

    def getPreviousSeason(self, now=None):
        return

    def getSeason(self, seasonID):
        return

    def getSeasonsPassed(self, now=None):
        return []

    def getAllSeasons(self):
        return []

    def getTimer(self, now=None, peripheryID=None):
        return 0

    def getLeftTimeToPrimeTimesEnd(self, now=None):
        return 0

    def getQuestsTimerLeft(self):
        return 0

    def isEnabled(self):
        return False

    def isTrainingEnabled(self):
        return False

    def hasActiveSeason(self, includePreannounced=False):
        return False

    def getActualSeasonNumber(self):
        return

    def getCurrentSeason(self, now=None, includePreannounced=False):
        return

    def isQualificationActive(self):
        return False

    def isQualificationResultsProcessing(self):
        return False

    def isQualificationCalculationRating(self):
        return False

    def isQualificationSquadAllowed(self):
        return

    def preannounceSeasonId(self):
        return

    def isInPreannounceState(self):
        return False

    def getPreannouncedSeason(self):
        return

    def getRoleEquipment(self, roleName):
        return

    def getEquipmentStartLevel(self, roleName):
        return

    def getRoleEquipmentOverrides(self, roleName):
        return

    def getPoiEquipmentOverrides(self, poiName):
        return

    def getViewData(self, viewAlias):
        return {}

    def isSuitableVehicle(self, vehicle):
        return False

    def hasSuitableVehicles(self):
        return False

    def vehicleIsAvailableForBuy(self):
        return False

    def vehicleIsAvailableForRestore(self):
        return False

    def hasPlayableVehicle(self):
        return False

    def isModePrbActive(self):
        return False

    def isBattleModifiersAvailable(self):
        return False

    def getAlertBlock(self):
        return (
         False, None, None)

    def getPlatoonRatingRestriction(self):
        return

    def getPlatoonMaxRankRestriction(self):
        return 0

    def getStatsSeasonsKeys(self):
        return []

    def getReceivedSeasonPoints(self):
        return {}

    def getMaxAvailableSeasonPoints(self):
        return 0

    def isQualificationPassedInSeason(self, seasonNumber):
        return False

    def getRatingForSeason(self, seasonNumber):
        return 0

    def getMaxRankNumberForSeason(self, seasonNumber=None):
        return 0

    def isEliteForSeason(self, seasonNumber=None):
        return False

    def updateEntitlementsCache(self, force=False, retryTimes=None):
        pass

    def getPlatoonRankRestriction(self, squadSize=None):
        return 0

    def tryToShowSeasonStatistics(self):
        pass