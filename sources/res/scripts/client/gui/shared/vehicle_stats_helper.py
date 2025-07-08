from helpers import dependency
from skeletons.gui.shared import IItemsCache
DEFAULT_VEHICLE_STATS = 0

@dependency.replace_none_kwargs(itemsCache=IItemsCache)
def getStatTrackersVehicleStats(vehCD, databaseID=None, itemsCache=None):
    accDossier = itemsCache.items.getAccountDossier(databaseID=databaseID)
    vehStats = accDossier.getStatTrackersVehicleStatsBlock().getVehicles().get(vehCD)
    if vehStats:
        return vehStats.frags
    return DEFAULT_VEHICLE_STATS