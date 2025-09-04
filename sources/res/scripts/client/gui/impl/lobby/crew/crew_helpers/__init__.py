import logging, typing
from helpers.dependency import replace_none_kwargs
from skeletons.gui.game_control import IWotPlusController
from skeletons.gui.shared import IItemsCache
if typing.TYPE_CHECKING:
    from typing import Tuple
    from gui.shared.gui_items.Vehicle import Vehicle
    from gui.shared.gui_items.Tankman import Tankman
_logger = logging.getLogger(__name__)

@replace_none_kwargs(itemsCache=IItemsCache)
def _getVehicleFromTankman(tankman, itemsCache=None):
    if tankman.vehicleDescr:
        return itemsCache.items.getVehicle(tankman.vehicleInvID)
    return itemsCache.items.getItemByCD(tankman.vehicleNativeDescr.type.compactDescr)


@replace_none_kwargs(wotPlusCtrl=IWotPlusController)
def tankmanHasCrewAssistOrderSets(tankman, tankmanRole, wotPlusCtrl=None):
    vehicle = _getVehicleFromTankman(tankman)
    if not vehicle:
        _logger.warning("Couldn't find a Vehicle for %r.", tankman)
        return (
         False, False)
    return wotPlusCtrl.hasCrewAssistOrderSets(vehicle.intCD, tankmanRole)


@replace_none_kwargs(wotPlusCtrl=IWotPlusController)
def getTankmanCrewAssistOrderSets(tankman, tankmanRole, wotPlusCtrl=None):
    vehicle = _getVehicleFromTankman(tankman)
    if not vehicle:
        _logger.warning("Couldn't find a Vehicle for %r.", tankman)
        return {}
    return wotPlusCtrl.getCrewAssistOrderSets(vehicle.intCD, tankmanRole)