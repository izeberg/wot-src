import time
from constants import RESTRICTION_TYPE, NOVICE_RESTRICTIONS_BAN_TYPE
from gui.shared.items_cache import CACHE_SYNC_REASON
from helpers import dependency
from skeletons.gui.shared import IItemsCache
CHAT_LOCK_CACHE_SYNC_REASONS = (
 CACHE_SYNC_REASON.SHOW_GUI,
 CACHE_SYNC_REASON.STATS_RESYNC)

def isNewbieChatLockedFromRestrictions(restrictions):
    if not restrictions:
        return False
    else:
        chatRestrictions = restrictions.get(RESTRICTION_TYPE.CHAT_BAN)
        if not chatRestrictions:
            return False
        curTime = int(time.time())
        for restr in chatRestrictions.itervalues():
            if restr is None:
                continue
            if restr.get('bantype') != NOVICE_RESTRICTIONS_BAN_TYPE:
                continue
            expiryTime = restr.get('expiryTime', 0)
            if expiryTime == 0 or expiryTime > curTime:
                return True

        return False


@dependency.replace_none_kwargs(itemsCache=IItemsCache)
def isNewbieChatLocked(itemsCache=None):
    if itemsCache is None or not itemsCache.isSynced():
        return False
    return isNewbieChatLockedFromRestrictions(itemsCache.items.stats.restrictions)