import logging, typing
from shared_utils import CONST_CONTAINER
from shared_utils.account_helpers.diff_utils import synchronizeDicts
_logger = logging.getLogger(__name__)
PDATA_KEY = 'grinchProgression'
if typing.TYPE_CHECKING:
    from typing import Dict

class _SyncDataKeys(CONST_CONTAINER):
    PROGRESSION = 'progression'


class GrinchCacheManager(object):

    def __init__(self):
        self.__cache = {}

    def onDisconnected(self):
        self.__cache.clear()

    def synchronize(self, isFullSync, diff):
        if isFullSync:
            self.__cache.clear()
        itemDiff = diff.get(PDATA_KEY, None)
        _logger.debug('Syncing cache for key %s: %s', PDATA_KEY, itemDiff)
        if itemDiff is not None:
            synchronizeDicts(itemDiff, self.__cache)
        return

    def getProgression(self):
        return self.__cache.get(_SyncDataKeys.PROGRESSION, {})

    def isStepClaimed(self, chapterId, stepId):
        claimedDataInt = self.getProgression().get(chapterId, 0)
        return self.isChapterStepClaimed(claimedDataInt, stepId)

    def isChapterStepClaimed(self, chapterDataInt, stepId):
        return 1 << stepId & chapterDataInt != 0