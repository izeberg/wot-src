from UnitRoster import BaseUnitRoster, BaseUnitRosterLimits
from unit_roster_config import RosterSlot11

class FunRandomRoster(BaseUnitRoster):
    MAX_SLOTS = 3
    MAX_EMPTY_SLOTS = 2
    SLOT_TYPE = RosterSlot11
    DEFAULT_SLOT_PACK = RosterSlot11().pack()
    LIMITS_TYPE = BaseUnitRosterLimits