import typing
from gui.shared.tooltips.advanced.data.default_alt_key_data import DefaultAltKeyData
if typing.TYPE_CHECKING:
    from typing import Tuple
    from gui.shared.gui_items.vehicle_modules import VehicleTurret

class TurretAltKeyData(DefaultAltKeyData):
    THERMAL_VISION = 'vehicleThermalVision'

    @classmethod
    def _getMechanicKeys(cls, item):
        if item.hasThermalVision():
            return (TurretAltKeyData.THERMAL_VISION,)
        return super(TurretAltKeyData, cls)._getMechanicKeys(item)