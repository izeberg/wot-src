import logging, random, nations
from CurrentVehicle import g_currentVehicle
from gui.Scaleform.daapi.view.lobby.storage.storage_helpers import getTopVehicleByNation
from gui.shared.utils.requesters import REQ_CRITERIA
from helpers import dependency
from items.vehicles import makeVehicleTypeCompDescrByName
from shared_utils import first
from skeletons.gui.shared import IItemsCache
from soft_exception import SoftException
_logger = logging.getLogger(__name__)
_DEFAULT_VEH_ID = 6929

@dependency.replace_none_kwargs(itemsCache=IItemsCache)
def getVehiclePreviewID(style, inInventory=False, itemsCache=None):
    styledVehicleCD = None
    if g_currentVehicle.isPresent() and g_currentVehicle.isCustomizationEnabled() and style.mayInstall(g_currentVehicle.item):
        return g_currentVehicle.item.intCD
    else:
        accDossier = itemsCache.items.getAccountDossier()
        vehiclesStats = accDossier.getRandomStats().getVehicles()
        vehicleGetter = itemsCache.items.getItemByCD
        sortedVehicles = sorted((vehicleGetter(veh) for veh in vehiclesStats.iterkeys()), key=lambda veh: (
         veh.level, vehiclesStats[veh.intCD].battlesCount), reverse=True)
        for vehicle in sortedVehicles:
            if vehicle.isInInventory and not vehicle.isLocked and not vehicle.isBroken and style.mayInstall(vehicle):
                return vehicle.intCD

        suitableVehicles = _getVehiclesForStylePreview(criteria=REQ_CRITERIA.INVENTORY | ~REQ_CRITERIA.VEHICLE.IS_OUTFIT_LOCKED | REQ_CRITERIA.VEHICLE.FOR_ITEM(style))
        if suitableVehicles:
            return first(suitableVehicles).intCD
        if not inInventory:
            suitableVehicles = []
            itemFilter = style.descriptor.filter
            nationsFilter = []
            if itemFilter is not None and itemFilter.include:
                for node in itemFilter.include:
                    if node.nations:
                        nationsFilter += node.nations
                    if node.vehicles:
                        suitableVehicles += node.vehicles

                if not suitableVehicles and nationsFilter:
                    nationName = nations.NAMES[nationsFilter[0]]
                    topVehicle = getTopVehicleByNation(nationName)
                    if topVehicle:
                        try:
                            vehicleCD = makeVehicleTypeCompDescrByName(topVehicle)
                            vehicle = itemsCache.items.getItemByCD(vehicleCD)
                            if style.mayInstall(vehicle):
                                suitableVehicles.append(vehicleCD)
                        except SoftException as e:
                            _logger.warning(e)

            if suitableVehicles:
                styledVehicleCD = random.choice(suitableVehicles)
            else:
                styledVehicleCD = _DEFAULT_VEH_ID
        return styledVehicleCD


@dependency.replace_none_kwargs(itemsCache=IItemsCache)
def _getVehiclesForStylePreview(criteria=None, itemsCache=None):
    return sorted(itemsCache.items.getVehicles(criteria=criteria).values(), key=lambda item: item.level, reverse=True)