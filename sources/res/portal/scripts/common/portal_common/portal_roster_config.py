from UnitRoster import BaseUnitRoster, BaseUnitRosterLimits
from unit_roster_config import RosterSlot11

class PortalRoster(BaseUnitRoster):
    MAX_SLOTS = 5
    MAX_EMPTY_SLOTS = 4
    SLOT_TYPE = RosterSlot11
    DEFAULT_SLOT_PACK = RosterSlot11().pack()
    LIMITS_TYPE = BaseUnitRosterLimits