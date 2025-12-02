import logging
from visual_script.block import Block
from visual_script.vehicle_blocks import VehicleMeta
from visual_script.misc import ASPECT
from visual_script.slot_types import SLOT_TYPE
_logger = logging.getLogger(__name__)

class ChangeMissileLauncherState(Block, VehicleMeta):

    def __init__(self, *args, **kwargs):
        super(ChangeMissileLauncherState, self).__init__(*args, **kwargs)
        self._in = self._makeEventInputSlot('in', self._execute)
        self._vehicle = self._makeDataInputSlot('vehicle', SLOT_TYPE.VEHICLE)
        self._state = self._makeDataInputSlot('state', SLOT_TYPE.INT)

    @classmethod
    def blockIcon(cls):
        return ':vse/blocks/python'

    def _execute(self):
        from grinch_common.cgf.missiles import LAUNCHER_CONTROLLER_COMPONENT_NAME
        playerVehicle = self._vehicle.getValue()
        component = playerVehicle.dynamicComponents.get(LAUNCHER_CONTROLLER_COMPONENT_NAME, None)
        if not component:
            _logger.debug("Failed to find '%s' component for vehicle id=%d", LAUNCHER_CONTROLLER_COMPONENT_NAME, playerVehicle.id)
            return
        else:
            component.updateState(self._state.getValue())
            return

    @classmethod
    def blockAspects(cls):
        return [ASPECT.CLIENT]