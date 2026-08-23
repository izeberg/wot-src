from __future__ import absolute_import
import typing
from enum import IntEnum
from helpers.time_utils import ONE_DAY
if typing.TYPE_CHECKING:
    from typing import Set
    JmNodesUpdTypes = Set['JmNodesUpdType']
    JmTokensUpdTypes = Set['JmTokensUpdType']
    JmTimeUpdTypes = Set['JmTimeUpdTypes']
JM_RUNNING_OUT_THRESHOLD = ONE_DAY * 4

class JmFtState(IntEnum):
    DISABLED = 0
    PAUSED = 1
    HIDDEN = 2
    ACTIVE = 3


JM_BANNER_ENABLED_FT_STATES = frozenset((JmFtState.ACTIVE, JmFtState.PAUSED))
JM_MAP_VIEW_DISABLED_FT_STATES = frozenset((JmFtState.DISABLED, JmFtState.PAUSED))

class JmTimeState(IntEnum):
    UNDEFINED = 0
    PRE = 1
    DURING = 2
    RUNNING_OUT = 3
    POST = 4


JM_BANNER_ENABLED_TIME_STATES = frozenset((JmTimeState.DURING, JmTimeState.RUNNING_OUT))
JM_MAP_VIEW_DISABLED_TIME_STATES = frozenset((JmTimeState.POST, JmTimeState.PRE))

class JmNodesUpdType(IntEnum):
    CONFIG = 1
    CURR_NODE = 2
    EXPLORED_NODES = 3
    TOKENS = 4


JM_NODES_UPD_TYPES = frozenset((
 JmNodesUpdType.CONFIG, JmNodesUpdType.CURR_NODE, JmNodesUpdType.EXPLORED_NODES, JmNodesUpdType.TOKENS))
JM_NODE_PATHS_UPD_TYPES = frozenset((JmNodesUpdType.EXPLORED_NODES, JmNodesUpdType.TOKENS))

class JmTokensUpdType(IntEnum):
    COINS = 1
    LOCK = 2
    QUEST = 3
    SHOP_BUNDLE = 4


JM_MAP_TOKENS_UPD_TYPES = frozenset((JmTokensUpdType.COINS, JmTokensUpdType.LOCK, JmTokensUpdType.SHOP_BUNDLE))
JM_TOKENS_CURRENCY_UPDATE_TYPES = frozenset((JmTokensUpdType.COINS, JmTokensUpdType.LOCK))

class JmTimeUpdType(IntEnum):
    STATE = 1
    STAMPS = 2
    QUESTS_REROLL = 3


JM_TIME_UPD_TYPES = frozenset((JmTimeUpdType.STATE, JmTimeUpdType.STAMPS, JmTimeUpdType.QUESTS_REROLL))