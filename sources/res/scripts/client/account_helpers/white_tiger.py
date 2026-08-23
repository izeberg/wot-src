import typing, logging
from account_helpers.account_data_cache import AccountDataStorage
from white_tiger_common.wt_constants import PDATA_WT_KEY, PDATA_WT_LOOTBOXES_KEY
if typing.TYPE_CHECKING:
    from typing import Dict
_logger = logging.getLogger(__name__)

class WhiteTiger(object):

    def __init__(self):
        self.__accountDataCache = AccountDataStorage(PDATA_WT_KEY, onAccountDataChangeCallback=self.__onAccountDataChanged)

    def clear(self):
        self.__accountDataCache.clear()

    @property
    def _data(self):
        return self.__accountDataCache.accountData

    def synchronize(self, isFullSync, diff):
        if self.__accountDataCache.isSynchronizationNeeded(diff):
            self.__accountDataCache.synchronize(isFullSync, diff)

    def __onAccountDataChanged(self, accountData):
        pass

    def getReRollCountByBoxID(self, boxID):
        if not boxID:
            _logger.error('There is no boxID provided!')
            return
        pendingBoxes = self.getPendingBoxesByBoxID(boxID)
        if not pendingBoxes:
            return 0
        return max(pendingBoxes.get('rolls', 0))

    def getPendingBoxesByBoxID(self, boxID):
        if not boxID:
            _logger.error('There is no boxID provided!')
            return
        pendingBoxes = self.getPendingBoxes()
        return pendingBoxes.get(boxID, {})

    def getPendingBoxes(self):
        return self._data.get(PDATA_WT_LOOTBOXES_KEY).get('pending', {})