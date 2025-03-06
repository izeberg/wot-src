from helpers import dependency, time_utils
from skeletons.gui.shared import IItemsCache

@dependency.replace_none_kwargs(itemsCache=IItemsCache)
def setTankmanRestoreInfo(vm, itemsCache=None):
    tankmenRestoreConfig = itemsCache.items.shop.tankmenRestoreConfig
    freeDays = tankmenRestoreConfig.freeDuration / time_utils.ONE_DAY
    billableDays = tankmenRestoreConfig.billableDuration / time_utils.ONE_DAY - freeDays
    restoreCost = tankmenRestoreConfig.cost
    restoreLimit = tankmenRestoreConfig.limit
    vm.setFreePeriod(freeDays)
    vm.setPaidPeriod(billableDays)
    vm.setRecoverPrice(restoreCost.get(restoreCost.getCurrency(), 0))
    vm.setMembersBuffer(restoreLimit)