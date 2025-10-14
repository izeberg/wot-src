from collections import namedtuple
HWGameplayAction = namedtuple('HWGameplayAction', ('value', 'targetID', 'id'))

class HWGameplayActionID(object):
    UNKNOWN = 0
    VEHICLE_REPAIR_INCOMING = 1
    VEHICLE_REPAIR_OUTCOMING = 2
    MODULES_DAMAGE_BLOCKED = 3
    HEALTH_DRAINED_BY_PASSIVE_VAMPIRE = 4
    SHELLS_LOOT_PICKUP = 5


def packGameplayActionFeedback(action):
    return (int(action.targetID) & 4294967295) << 32 | (int(action.value) & 65535) << 16 | action.id & 65535


def unpackGameplayActionFeedback(packedData):
    return HWGameplayAction(targetID=packedData >> 32 & 4294967295, value=packedData >> 16 & 65535, id=packedData & 65535)