from enum import Enum
from new_year.ny_constants import EnvironmentState
FEATURE = 'holiday_ops_2026'

class HOObjects(str, Enum):
    BALLOON = 'balloon'


class HOLogActions(str, Enum):
    CLICK = 'click'


class HOEnvironmentStates(str, Enum):
    DAY = 'day'
    NIGHT = 'night'


class HOParentScreens(str, Enum):
    HANGAR = 'hangar'


ENVIRONMENT_STATE_MAPPING = {EnvironmentState.DAY: HOEnvironmentStates.DAY, 
   EnvironmentState.NIGHT: HOEnvironmentStates.NIGHT}