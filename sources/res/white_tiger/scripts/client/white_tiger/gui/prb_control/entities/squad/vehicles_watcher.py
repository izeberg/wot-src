import typing
from gui.prb_control.entities.base.pre_queue.vehicles_watcher import BaseVehiclesWatcher
from gui.shared.utils.requesters.ItemsRequester import REQ_CRITERIA
from helpers import dependency
from skeletons.gui.shared import IItemsCache

class WhiteTigerBattlesSquadVehiclesWatcher(BaseVehiclesWatcher):
    __itemsCache = dependency.descriptor(IItemsCache)

    def _getUnsuitableVehicles(self, onClear=False):
        vehs = self.__itemsCache.items.getVehicles(REQ_CRITERIA.INVENTORY).values()
        return vehs