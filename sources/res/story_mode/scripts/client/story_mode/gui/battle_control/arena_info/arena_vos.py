import typing
from story_mode_common.story_mode_constants import VEHICLE_BUNKER_TURRET_TAG
if typing.TYPE_CHECKING:
    from gui.battle_control.arena_info.arena_vos import VehicleTypeInfoVO

def getDisplayedClassTag(vehicleType, defaultClassTag):
    if VEHICLE_BUNKER_TURRET_TAG in vehicleType.tags:
        return VEHICLE_BUNKER_TURRET_TAG
    return defaultClassTag