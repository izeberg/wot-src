import typing
from helpers import dependency
from skeletons.gui.shared import IItemsCache
if typing.TYPE_CHECKING:
    import Vehicle
DEFAULT_VEHICLE_STATS = 0

@dependency.replace_none_kwargs(itemsCache=IItemsCache)
def getStatTrackersVehicleStats(vehCD, vehicle=None, databaseID=None, itemsCache=None):
    if vehicle:
        from PlatoonTank import PlatoonTank
        if isinstance(vehicle, PlatoonTank):
            return vehicle.getStFrags()
    accDossier = itemsCache.items.getAccountDossier(databaseID=databaseID)
    vehStats = accDossier.getStatTrackersVehicleStatsBlock().getVehicles().get(vehCD)
    if vehStats:
        return vehStats.frags
    return DEFAULT_VEHICLE_STATS