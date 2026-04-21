from __future__ import absolute_import
from gui import GUI_NATIONS_ORDER_INDEX
from gui.shared.gui_items.Vehicle import VEHICLE_TYPES_ORDER_INDICES

def vehicleComparisonKey(vehicle):
    return (
     not vehicle.isFavorite,
     GUI_NATIONS_ORDER_INDEX[vehicle.nationName],
     VEHICLE_TYPES_ORDER_INDICES[vehicle.type],
     vehicle.level,
     vehicle.userName)