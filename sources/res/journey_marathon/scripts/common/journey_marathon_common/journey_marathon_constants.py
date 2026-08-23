from enum import Enum, unique
from typing import Optional, Tuple

@unique
class NodeType(str, Enum):
    START = 'start'
    SMALL = 'small'
    MEDIUM = 'medium'
    LARGE = 'large'
    LOCKED = 'locked'


JM_GAME_PARAMS_KEY = 'journeyMarathon'
QUEST_GROUPS = ('easy', 'medium', 'hard')
TOTAL_QUESTS_COUNT = 5
SEPARATOR = ':'
PREFIX = 'journey'
QUEST_PREFIX = 'journey:'
DAILY_QUEST_POSTFIX = 'daily'
JM_ANNIVERSARY_PRESENT_POSTFIX = 'anniversary_present'
JM_PREFIX_FMT = PREFIX + SEPARATOR + '{journeyId}' + SEPARATOR
QUEST_ISSUED_POSTFIX = 'issued'
LOCK_TOKEN_POSTFIX = 'unlock'
JM_COIN_TOKEN_FMT = JM_PREFIX_FMT + 'coin'
JM_UNLOCK_TOKEN_PREFIX_FMT = JM_PREFIX_FMT + SEPARATOR
JM_SHOP_BUNDLE_ACCRUING_TOKEN_FMT = JM_PREFIX_FMT + 'pet:2:accruing'
JM_SHOP_BUNDLE_PROMO_TOKEN_FMT = JM_PREFIX_FMT + 'pet:2:promo'

class JmTokenQuestPartsIdxs(object):
    PREFIX = 0
    JOURNEY_ID = 1
    GROUP = 2
    NUM = 3
    ISSUED = 4


class JmPdataKeys(object):
    MAIN_SECTION = 'journey'
    JOURNEY_ID = 'currentEventId'
    PROGRESS_SECTION = 'progress'
    CURRENT = 'currentNodeId'
    COMPLETED = 'completedNodeIds'


JM_CMDS_COOLDOWN = 1.0

def __splitQuestID(questID, partsCount=4):
    if not isinstance(questID, basestring):
        return None
    else:
        parts = tuple(str(questID).split(SEPARATOR))
        if len(parts) != partsCount or parts[0] != PREFIX:
            return None
        return parts


def isUnlockToken(token, fillterJourneyID=None):
    parts = __splitQuestID(token)
    if parts is None:
        return False
    else:
        tokenPrefix, journeyLaunchID, unlock, _ = parts
        return tokenPrefix == PREFIX and (not fillterJourneyID or journeyLaunchID == fillterJourneyID) and unlock == LOCK_TOKEN_POSTFIX


def isDailyRewardQuest(questID):
    return questID.startswith(QUEST_PREFIX) and questID.endswith(DAILY_QUEST_POSTFIX)


def parseUnlockTokenKey(token):
    return __splitQuestID(token)[(-1)]