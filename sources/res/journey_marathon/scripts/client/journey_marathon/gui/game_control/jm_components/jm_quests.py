from __future__ import absolute_import
import typing
from helpers.dependency import descriptor
from journey_marathon.jm_constants import JmTokensUpdType
from journey_marathon.jm_helpers import jmCtrl, packJmQuests
from journey_marathon_common.journey_marathon_constants import SEPARATOR, QUEST_ISSUED_POSTFIX, JmTokenQuestPartsIdxs, QUEST_GROUPS
from skeletons.gui.server_events import IEventsCache
from skeletons.gui.shared import IItemsCache
if typing.TYPE_CHECKING:
    from typing import Callable, Dict, List, Tuple
    from gui.server_events.event_items import Quest
    from journey_marathon.jm_constants import JmTokensUpdTypes
    from journey_marathon.jm_helpers import JmQuestInfo
_TOKEN_SUFFIX = SEPARATOR + QUEST_ISSUED_POSTFIX

class JmQuests(object):
    __eventsCache = descriptor(IEventsCache)
    __itemsCache = descriptor(IItemsCache)

    def __init__(self):
        self.__quests = {}
        self.__currQuests = []
        self.__currQuestInfos = []

    def init(self):
        jmCtrl().onJmTokensChange += self.__onJmTokensChange
        self.__eventsCache.onSyncCompleted += self.invalidateJmQuests

    def fini(self):
        jmCtrl().onJmTokensChange -= self.__onJmTokensChange
        self.__eventsCache.onSyncCompleted -= self.invalidateJmQuests
        self.__clear()

    def getJmQuests(self):
        quests = self.__quests
        if not quests:
            quests.update(self.__eventsCache.getAllQuests(_makeQuestFilter(), makeRelations=False))
        return quests

    def getJmCurrentQuests(self):
        currQuests = self.__currQuests
        if not currQuests:
            quests = self.getJmQuests()
            allTokens = self.__itemsCache.items.tokens.getTokens()
            currQuests[:] = [ quests[qID] for qID in quests if qID + _TOKEN_SUFFIX in allTokens ]
            currQuests.sort(key=_questSortKey)
        return currQuests

    def getJmCurrQuestInfos(self):
        questInfos = self.__currQuestInfos
        if not questInfos:
            quests = self.getJmCurrentQuests()
            questInfos[:] = packJmQuests(quests)
        return questInfos

    def invalidateJmQuests(self):
        self.__clear()
        jmCtrl().onJmQuestsChange()

    def __onJmTokensChange(self, updTypes, _):
        if JmTokensUpdType.QUEST in updTypes:
            self.invalidateJmQuests()

    def __clear(self):
        self.__quests.clear()
        self.__currQuests = []
        self.__currQuestInfos = []


def _makeQuestFilter():
    prefix = jmCtrl().jmConfig.getJmQuestTokenPrefix()

    def _jmQuestFilter(quest):
        return quest.getID().startswith(prefix)

    return _jmQuestFilter


def _questSortKey(quest):
    parts = quest.getID().split(SEPARATOR)
    return (QUEST_GROUPS.index(parts[_groupIdx]), int(parts[_numIdx]))


_groupIdx = JmTokenQuestPartsIdxs.GROUP
_numIdx = JmTokenQuestPartsIdxs.NUM