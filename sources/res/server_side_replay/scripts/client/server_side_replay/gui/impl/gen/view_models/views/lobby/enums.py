from enum import Enum, IntEnum

class ReplaysViews(IntEnum):
    BESTREPLAYS = 0
    MYREPLAYS = 1
    FINDREPLAY = 2


class TankmanLocation(Enum):
    INBARRACKS = 'in_barracks'
    INTANK = 'in_tank'
    DISMISSED = 'dismissed'