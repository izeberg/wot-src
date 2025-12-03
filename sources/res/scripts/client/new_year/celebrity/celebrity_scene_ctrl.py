import logging, typing
from Event import Event, EventManager
from account_helpers.AccountSettings import AccountSettings, NY_CELEBRITY_DAY_QUESTS_COMPLETED_MASK
from helpers import dependency
from items.components.ny_constants import CelebrityQuestTokenParts
from new_year.celebrity.celebrity_quests_helpers import getCelebrityMarathonQuests, getCelebrityQuestByFullID, getCelebrityTokens, getCelebrityQuestCount, iterAllTypeCelebrityActiveQuestsIDs
from ny_common.settings import NY_CONFIG_NAME, CelebrityConsts
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.server_events import IEventsCache
from skeletons.gui.shared import IItemsCache
from skeletons.new_year import ICelebritySceneController
if typing.TYPE_CHECKING:
    from typing import Dict, Union
    from gui.server_events.event_items import TokenQuest, CelebrityQuest, CelebrityTokenQuest
_logger = logging.getLogger(__name__)

class CelebritySceneController(ICelebritySceneController):
    __slots__ = ('__eventsManager', '__quests', '__isInChallengeView', '__tokens',
                 '__marathonQuests', '__completedDayQuestsMask', '__questsCount',
                 '__completedQuestsCount')
    __eventsCache = dependency.descriptor(IEventsCache)
    __lobbyContext = dependency.descriptor(ILobbyContext)
    __itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self):
        super(CelebritySceneController, self).__init__()
        self.__eventsManager = EventManager()
        self.onQuestsUpdated = Event(self.__eventsManager)
        self.__quests = {}
        self.__tokens = {}
        self.__marathonQuests = {}
        self.__completedDayQuestsMask = 0
        self.__fullyCompletedDayQuestsMask = 0
        self.__questsCount = 0
        self.__completedQuestsCount = 0
        self.__fullyCompletedQuestsCount = 0
        self.__isInChallengeView = False

    @property
    def isInChallengeView(self):
        return self.__isInChallengeView

    @property
    def isChallengeCompleted(self):
        return self.fullyCompletedQuestsCount == self.questsCount

    @property
    def isCelebrityQuestsCompleted(self):
        return self.completedQuestsCount >= self.questsCount

    @property
    def hasNewCompletedQuests(self):
        completedMask = self.__getCompletedQuestsMask(NY_CELEBRITY_DAY_QUESTS_COMPLETED_MASK)
        return bool(completedMask ^ self.__completedDayQuestsMask)

    @property
    def quests(self):
        return self.__quests

    @property
    def tokens(self):
        return self.__tokens

    @property
    def marathonQuests(self):
        return self.__marathonQuests

    @property
    def completedDayQuestsMask(self):
        return self.__completedDayQuestsMask

    @property
    def fullyCompletedDayQuestsMask(self):
        return self.__fullyCompletedDayQuestsMask

    @property
    def questsCount(self):
        return self.__questsCount

    @property
    def completedQuestsCount(self):
        if not self.__tokens:
            self.__updateQuests()
        return self.__completedQuestsCount

    @property
    def fullyCompletedQuestsCount(self):
        if not self.__tokens:
            self.__updateQuests()
        return self.__fullyCompletedQuestsCount

    def fini(self):
        self.__destroy()
        super(CelebritySceneController, self).fini()

    def onLobbyInited(self, _):
        self.__subscribe()
        self.__updateQuests()

    def onDisconnected(self):
        self.__destroy()

    def onAvatarBecomePlayer(self):
        self.__destroy()

    def onEnterChallenge(self):
        self.__isInChallengeView = True

    def onExitChallenge(self):
        self.__isInChallengeView = False

    def __destroy(self):
        self.__unsubscribe()
        self.__eventsManager.clear()
        self.__quests.clear()
        self.__tokens.clear()
        self.__marathonQuests.clear()
        self.__isInChallengeView = False

    def __subscribe(self):
        self.__eventsCache.onSyncCompleted += self.__onSyncCompleted
        self.__eventsCache.onQuestConditionUpdated += self.__onSyncCompleted
        self.__lobbyContext.getServerSettings().onServerSettingsChange += self.__onServerSettingsChange

    def __unsubscribe(self):
        self.__eventsCache.onSyncCompleted -= self.__onSyncCompleted
        self.__eventsCache.onQuestConditionUpdated -= self.__onSyncCompleted
        self.__lobbyContext.getServerSettings().onServerSettingsChange -= self.__onServerSettingsChange

    def __onSyncCompleted(self):
        self.__updateQuests()

    def __onServerSettingsChange(self, diff):
        if diff.get(NY_CONFIG_NAME, {}).get(CelebrityConsts.CONFIG_NAME) is None:
            return
        else:
            self.__updateQuests()
            return

    def __updateQuests(self):
        self.__marathonQuests = getCelebrityMarathonQuests()
        self.__tokens = getCelebrityTokens()
        self.__completedDayQuestsMask = 0
        self.__fullyCompletedDayQuestsMask = 0
        for firstToken, secondToken in iterAllTypeCelebrityActiveQuestsIDs():
            firstQuest = getCelebrityQuestByFullID(firstToken)
            secondQuest = getCelebrityQuestByFullID(secondToken)
            if not firstQuest or not secondQuest or not firstQuest.isCompleted() and not secondQuest.isCompleted():
                continue
            self.__quests[firstToken] = firstQuest
            qType, qNum = CelebrityQuestTokenParts.getFullQuestOrderInfo(firstToken)
            qNumBit = 1 << qNum - 1
            if qType == CelebrityQuestTokenParts.QUEST:
                self.__completedDayQuestsMask |= qNumBit
            if firstQuest.isCompleted() and secondQuest.isCompleted():
                self.__fullyCompletedDayQuestsMask |= qNumBit

        self.__questsCount = getCelebrityQuestCount()
        self.__completedQuestsCount = bin(self.completedDayQuestsMask).count('1')
        self.__fullyCompletedQuestsCount = bin(self.__fullyCompletedDayQuestsMask).count('1')
        self.onQuestsUpdated()

    @staticmethod
    def __getCompletedQuestsMask(maskSettingName):
        completedQuestsMask = AccountSettings.getUIFlag(maskSettingName)
        return completedQuestsMask