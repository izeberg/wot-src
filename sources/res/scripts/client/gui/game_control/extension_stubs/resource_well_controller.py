from collections import namedtuple
from typing import Dict, Optional, Set, TYPE_CHECKING, List
from Event import EventManager, Event
from skeletons.gui.resource_well import IResourceWellController
if TYPE_CHECKING:
    from gui.shared.gui_items.Vehicle import Vehicle
_ResourceWellConfig = namedtuple('_ResourceWellConfig', ('isEnabled', 'season', 'finishTime',
                                                         'remindTime', 'rewards',
                                                         'startTime', 'infoPageUrl'))
_RESOURCE_WELL_CONFIG_STUB = _ResourceWellConfig(isEnabled=False, season=0, finishTime=0, remindTime=0, rewards={}, startTime=0, infoPageUrl='')

class ResourceWellController(IResourceWellController):

    def __init__(self):
        self.__eventsManager = EventManager()
        self.onEventUpdated = Event(self.__eventsManager)
        self.onSettingsChanged = Event(self.__eventsManager)
        self.onNumberRequesterUpdated = Event(self.__eventsManager)

    @property
    def config(self):
        return _RESOURCE_WELL_CONFIG_STUB

    def isEnabled(self):
        return False

    def isActive(self):
        return False

    def isStarted(self):
        return False

    def isFinished(self):
        return False

    def isNotStarted(self):
        return False

    def isPaused(self):
        return False

    def isForbiddenAccount(self):
        return False

    def isSeasonNumberDefault(self):
        return False

    def getRewardLimit(self, rewardID):
        return 0

    def getCurrentPoints(self):
        return 0

    def getReceivedRewardIDs(self):
        return set()

    def isRewardReceived(self, rewardID):
        return False

    def getBalance(self):
        return {}

    def getPurchaseMode(self):
        return

    def getRewardVehicle(self, rewardID):
        return

    def getRewardStyleID(self, rewardID):
        return

    def getRewardSequence(self, rewardID):
        return ''

    def getRewardLeftCount(self, rewardID):
        return 0

    def isParentRewardAvailable(self, rewardID):
        return False

    def isRewardAvailable(self, rewardID):
        return False

    def getCurrentRewardID(self):
        return ''

    def isRewardCountAvailable(self, rewardID):
        return False

    def getAvailableRewards(self):
        return []

    def isRewardsOver(self):
        return False

    def isRewardVehicle(self, vehicleCD):
        return False

    def startNumberRequesters(self):
        pass

    def stopNumberRequesters(self):
        pass

    def fini(self):
        self.__eventsManager.clear()