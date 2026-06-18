from __future__ import absolute_import
import logging, typing, CGF
from cgf_script.registration import registerComponent
if typing.TYPE_CHECKING:
    from vehicle_appearance.common_tank_appearance import CommonTankAppearance
    from gui.hangar_vehicle_appearance import HangarVehicleAppearance
    TAppearance = typing.Union[(HangarVehicleAppearance, CommonTankAppearance, None)]
_logger = logging.getLogger(__name__)

@registerComponent
class VehicleAppearanceComponent(object):
    domain = CGF.Domain.ClientEditor
    userVisible = False
    vseVisible = False

    def __init__(self, appearance):
        if appearance is None:
            _logger.error('Unable to find appearance')
        self.appearance = appearance
        return