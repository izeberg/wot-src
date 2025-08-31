from enum import Enum

class MissionCategory(Enum):
    ASSAULT = 'assault'
    SNIPER = 'sniper'
    SUPPORT = 'support'


class OperationState(Enum):
    COMPLETED_WITH_HONORS = 'completedWithHonors'
    COMPLETED = 'completed'
    ACTIVE = 'active'
    AVAILABLE = 'available'
    UNAVAILABLE = 'unavailable'
    LOCKED = 'locked'


class ParamTooltipType(Enum):
    PROGRESSION = 'progression'
    PM3_POINTS = 'pm3_points'
    CUSTOM_SIMPLE = 'custom_simple'