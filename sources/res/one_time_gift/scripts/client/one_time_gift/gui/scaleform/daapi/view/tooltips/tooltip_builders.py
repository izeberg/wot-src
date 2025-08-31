from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.shared.tooltips import vehicle
from gui.shared.tooltips.builders import DataBuilder
from one_time_gift.gui.gui_constants import TOOLTIP_CONSTANTS as _TOOLTIPS
from one_time_gift.gui.shared.tooltips.contexts import OneTimeGiftVehicleContext
__all__ = ('getTooltipBuilders', )

def getTooltipBuilders():
    return (
     DataBuilder(_TOOLTIPS.ONE_TIME_GIFT_VEHICLE_TOOLTIP, TOOLTIPS_CONSTANTS.VEHICLE_INFO_UI, vehicle.VehicleInfoTooltipData(OneTimeGiftVehicleContext())),)