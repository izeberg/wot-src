import AccountCommands
from functools import partial
from new_year.ny_constants import SyncDataKeys
from shared_utils.account_helpers.diff_utils import synchronizeDicts

class NyTamagotchiRaid(object):

    def __init__(self, syncData):
        self.__account = None
        self.__syncData = syncData
        self.__cache = {}
        self.__ignore = True
        return

    def onAccountBecomePlayer(self):
        self.__ignore = False

    def onAccountBecomeNonPlayer(self):
        self.__ignore = True

    def setAccount(self, account):
        self.__account = account

    def synchronize(self, isFullSync, diff):
        if isFullSync and self.__cache:
            self.__cache.clear()
        cache = diff.get('cache', {})
        raidDiff = cache.get(SyncDataKeys.NY_TAMAGOTCHI_RAID)
        if raidDiff is not None:
            if not raidDiff.get('currentRaid', {}):
                self.__cache['currentRaid'] = {}
            synchronizeDicts(raidDiff, self.__cache)
        return

    def getCache(self, callback=None):
        if self.__ignore:
            if callback is not None:
                callback(AccountCommands.RES_NON_PLAYER, None)
            return
        self.__syncData.waitForSync(partial(self.__onGetCacheResponse, callback))
        return

    def __onGetCacheResponse(self, callback, resultID):
        if resultID < 0:
            if callback is not None:
                callback(resultID, None)
            return
        if callback is not None:
            callback(resultID, self.__cache)
        return