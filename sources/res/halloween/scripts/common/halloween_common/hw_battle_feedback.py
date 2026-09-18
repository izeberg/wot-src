from __future__ import absolute_import
from collections import namedtuple
HWGameplayAction = namedtuple('HWGameplayAction', ('value', 'targetID', 'id'))

class HWGameplayActionID(object):
    UNKNOWN = 0
    VEHICLE_REPAIR_INCOMING = 1
    VEHICLE_REPAIR_OUTCOMING = 2
    MODULES_DAMAGE_BLOCKED = 3
    HEALTH_DRAINED_BY_PASSIVE_VAMPIRE = 4
    SHELLS_LOOT_PICKUP = 5
    HANGAR_ITEMS_LOOT_PICKUP = 6
    HANGAR_ITEMS_LOOT_RECEIVE = 7
    SOULS_LOOT_PICKUP = 8
    SHELLS_LOOT_RECEIVE = 9
    SOULS_LOOT_RECEIVE = 10
    ANOMALY_LOOT_PICKUP = 11
    ANOMALY_LOOT_RECEIVE = 12
    SOULS_LOOT_REFUND = 13
    BOMBER_RESIST = 14
    SOULS_MIRIUMIZATION_ADD = 15
    SOULS_MIRIUMIZATION_DECREASE = 16


def packGameplayActionFeedback(action):
    return (int(action.targetID) & 4294967295) << 32 | (int(action.value) & 65535) << 16 | action.id & 65535


def unpackGameplayActionFeedback(packedData):
    return HWGameplayAction(targetID=packedData >> 32 & 4294967295, value=packedData >> 16 & 65535, id=packedData & 65535)