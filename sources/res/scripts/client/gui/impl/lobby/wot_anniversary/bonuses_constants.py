from enum import Enum, unique

class BonusesLayoutConsts(object):
    PRIORITY = 'priority'
    VISIBILITY = 'isVisible'
    OVERRIDE = 'override'
    ID = 'id'
    LEVEL = 'level'
    BIG_ICON = 'bigIcon'
    MAIN_KEYS = (
     PRIORITY, VISIBILITY, BIG_ICON)
    INT_VALUES = (PRIORITY,)
    BOOL_VALUES = (VISIBILITY,)


@unique
class ChapterState(Enum):
    ACTIVE = 'active'
    PAUSED = 'paused'
    COMPLETED = 'completed'
    NOT_STARTED = 'notStarted'