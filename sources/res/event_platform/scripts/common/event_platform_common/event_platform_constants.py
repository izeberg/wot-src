from __future__ import absolute_import
import arena_bonus_type_caps
from constants_utils import ConstInjector

class ARENA_BONUS_TYPE_CAPS(arena_bonus_type_caps.ARENA_BONUS_TYPE_CAPS, ConstInjector):
    _const_type = str
    RESPAWN_FRAMEWORK_VEHICLE_SELECTION = 'RESPAWN_FRAMEWORK_VEHICLE_SELECTION'