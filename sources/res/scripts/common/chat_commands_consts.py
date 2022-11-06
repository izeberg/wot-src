import Math
from enum import Enum, unique
from constants import ARENA_BONUS_TYPE

class BATTLE_CHAT_COMMAND_NAMES(object):
    SOS = 'HELPME'
    CONFIRM = 'CONFIRM'
    RELOADINGGUN = 'RELOADINGGUN'
    RELOADING_READY = 'RELOADING_READY'
    RELOADING_CASSETE = 'RELOADING_CASSETE'
    RELOADING_READY_CASSETE = 'RELOADING_READY_CASSETE'
    RELOADING_UNAVAILABLE = 'RELOADING_UNAVAILABLE'
    ATTACK_ENEMY = 'ATTACK_ENEMY'
    ATTACKING_ENEMY = 'ATTACKING_ENEMY'
    ATTACKING_ENEMY_WITH_SPG = 'ATTACKING_ENEMY_WITH_SPG'
    THANKS = 'THANKS'
    HELPME = 'HELPMEEX'
    TURNBACK = 'TURNBACK'
    POSITIVE = 'POSITIVE'
    AFFIRMATIVE = 'AFFIRMATIVE'
    NEGATIVE = 'NEGATIVE'
    SUPPORTING_ALLY = 'SUPPORTING_ALLY'
    ATTACK_BASE = 'ATTACK_BASE'
    ATTACKING_BASE = 'ATTACKING_BASE'
    DEFEND_BASE = 'DEFEND_BASE'
    DEFENDING_BASE = 'DEFENDING_BASE'
    SPG_AIM_AREA = 'SPG_AIM_AREA'
    GOING_THERE = 'GOING_THERE'
    ATTENTION_TO_POSITION = 'ATTENTION_TO_POSITION'
    PREBATTLE_WAYPOINT = 'PREBATTLE_WAYPOINT'
    VEHICLE_SPOTPOINT = 'VEHICLE_SPOTPOINT'
    SHOOTING_POINT = 'SHOOTING_POINT'
    NAVIGATION_POINT = 'NAVIGATION_POINT'
    EPIC_GLOBAL_SAVE_TANKS_ATK = 'EPIC_GLOBAL_SAVETANKS_ATK'
    EPIC_GLOBAL_SAVE_TANKS_DEF = 'EPIC_GLOBAL_SAVETANKS_DEF'
    EPIC_GLOBAL_TIME_ATK = 'EPIC_GLOBAL_TIME_ATK'
    EPIC_GLOBAL_TIME_DEF = 'EPIC_GLOBAL_TIME_DEF'
    EPIC_GLOBAL_WEST = 'EPIC_GLOBAL_WEST'
    EPIC_GLOBAL_CENTER = 'EPIC_GLOBAL_CENTER'
    EPIC_GLOBAL_EAST = 'EPIC_GLOBAL_EAST'
    EPIC_GLOBAL_HQ_ATK = 'EPIC_GLOBAL_HQ_ATK'
    EPIC_GLOBAL_HQ_DEF = 'EPIC_GLOBAL_HQ_DEF'
    DEFEND_OBJECTIVE = 'DEFEND_OBJECTIVE'
    ATTACK_OBJECTIVE = 'ATTACK_OBJECTIVE'
    DEFENDING_OBJECTIVE = 'DEFENDING_OBJECTIVE'
    ATTACKING_OBJECTIVE = 'ATTACKING_OBJECTIVE'
    EVENT_CHAT_1 = 'EVENT_CHAT_1'
    EVENT_CHAT_2 = 'EVENT_CHAT_2'
    EVENT_CHAT_3 = 'EVENT_CHAT_3'
    EVENT_CHAT_4 = 'EVENT_CHAT_4'
    EVENT_CHAT_5 = 'EVENT_CHAT_5'
    EVENT_CHAT_6 = 'EVENT_CHAT_6'
    EVENT_CHAT_7 = 'EVENT_CHAT_7'
    EVENT_CHAT_1_EX = 'EVENT_CHAT_1_EX'
    EVENT_CHAT_2_EX = 'EVENT_CHAT_2_EX'
    EVENT_CHAT_3_EX = 'EVENT_CHAT_3_EX'
    EVENT_CHAT_4_EX = 'EVENT_CHAT_4_EX'
    EVENT_CHAT_5_EX = 'EVENT_CHAT_5_EX'
    EVENT_CHAT_6_EX = 'EVENT_CHAT_6_EX'
    EVENT_CHAT_7_EX = 'EVENT_CHAT_7_EX'
    REPLY = 'REPLY'
    CANCEL_REPLY = 'CANCEL_REPLY'
    CLEAR_CHAT_COMMANDS = 'CLEAR_CHAT_COMMANDS'


_DEFAULT_SPG_AREA_COMMAND_TIME = 6.0
_DEFAULT_ACTIVE_COMMAND_TIME = 6.0
_PERSONAL_MESSAGE_MUTE_DURATION = 10.0
INVALID_VEHICLE_POSITION = Math.Vector3(-99999.9, -99999.9, -99999.9)

class ReplyState(Enum):
    NO_REPLY = 0
    CAN_REPLY = 1
    CAN_CANCEL_REPLY = 2
    CAN_CONFIRM = 3
    CAN_RESPOND = 4


ONE_SHOT_COMMANDS_TO_REPLIES = {BATTLE_CHAT_COMMAND_NAMES.TURNBACK: BATTLE_CHAT_COMMAND_NAMES.POSITIVE, 
   BATTLE_CHAT_COMMAND_NAMES.THANKS: BATTLE_CHAT_COMMAND_NAMES.POSITIVE, 
   BATTLE_CHAT_COMMAND_NAMES.RELOADINGGUN: BATTLE_CHAT_COMMAND_NAMES.CONFIRM, 
   BATTLE_CHAT_COMMAND_NAMES.SPG_AIM_AREA: BATTLE_CHAT_COMMAND_NAMES.CONFIRM, 
   BATTLE_CHAT_COMMAND_NAMES.ATTENTION_TO_POSITION: BATTLE_CHAT_COMMAND_NAMES.CONFIRM}
COMMAND_RESPONDING_MAPPING = {BATTLE_CHAT_COMMAND_NAMES.SUPPORTING_ALLY: BATTLE_CHAT_COMMAND_NAMES.THANKS}
INVALID_COMMAND_ID = -1
INVALID_MARKER_ID = -1
INVALID_TARGET_ID = -1
INVALID_MARKER_SUBTYPE = ''

@unique
class MarkerType(Enum):
    INVALID_MARKER_TYPE = 'invalid'
    VEHICLE_MARKER_TYPE = 'vehicle'
    LOCATION_MARKER_TYPE = 'location'
    BASE_MARKER_TYPE = 'base'
    HEADQUARTER_MARKER_TYPE = 'headquarter'

    @staticmethod
    def getEnumValueByName(markerTypeName):
        if markerTypeName in MarkerType.__members__:
            return MarkerType.__members__[markerTypeName]
        else:
            return


class DefaultMarkerSubType(Enum):
    ALLY_MARKER_SUBTYPE = 'ally'
    ENEMY_MARKER_SUBTYPE = 'enemy'


class LocationMarkerSubType(Enum):
    ATTENTION_TO_MARKER_SUBTYPE = 'attentionTo'
    GOING_TO_MARKER_SUBTYPE = 'goingThere'
    SPG_AIM_AREA_SUBTYPE = 'spgArea'
    PREBATTLE_WAYPOINT_SUBTYPE = 'prebattle'
    VEHICLE_SPOTPOINT_SUBTYPE = 'spottedVehicle'
    SHOOTING_POINT_SUBTYPE = 'shootingPoint'
    NAVIGATION_POINT_SUBTYPE = 'navigationPoint'


_COMMAND_NAME_TRANSFORM_MARKER_TYPE = {BATTLE_CHAT_COMMAND_NAMES.ATTACK_ENEMY: MarkerType.VEHICLE_MARKER_TYPE, 
   BATTLE_CHAT_COMMAND_NAMES.SOS: MarkerType.VEHICLE_MARKER_TYPE, 
   BATTLE_CHAT_COMMAND_NAMES.HELPME: MarkerType.VEHICLE_MARKER_TYPE, 
   BATTLE_CHAT_COMMAND_NAMES.ATTACKING_ENEMY_WITH_SPG: MarkerType.VEHICLE_MARKER_TYPE, 
   BATTLE_CHAT_COMMAND_NAMES.ATTACKING_ENEMY: MarkerType.VEHICLE_MARKER_TYPE, 
   BATTLE_CHAT_COMMAND_NAMES.SUPPORTING_ALLY: MarkerType.VEHICLE_MARKER_TYPE, 
   BATTLE_CHAT_COMMAND_NAMES.RELOADINGGUN: MarkerType.VEHICLE_MARKER_TYPE, 
   BATTLE_CHAT_COMMAND_NAMES.TURNBACK: MarkerType.VEHICLE_MARKER_TYPE, 
   BATTLE_CHAT_COMMAND_NAMES.THANKS: MarkerType.VEHICLE_MARKER_TYPE, 
   BATTLE_CHAT_COMMAND_NAMES.DEFEND_BASE: MarkerType.BASE_MARKER_TYPE, 
   BATTLE_CHAT_COMMAND_NAMES.ATTACK_BASE: MarkerType.BASE_MARKER_TYPE, 
   BATTLE_CHAT_COMMAND_NAMES.DEFENDING_BASE: MarkerType.BASE_MARKER_TYPE, 
   BATTLE_CHAT_COMMAND_NAMES.ATTACKING_BASE: MarkerType.BASE_MARKER_TYPE, 
   BATTLE_CHAT_COMMAND_NAMES.GOING_THERE: MarkerType.LOCATION_MARKER_TYPE, 
   BATTLE_CHAT_COMMAND_NAMES.ATTENTION_TO_POSITION: MarkerType.LOCATION_MARKER_TYPE, 
   BATTLE_CHAT_COMMAND_NAMES.SPG_AIM_AREA: MarkerType.LOCATION_MARKER_TYPE, 
   BATTLE_CHAT_COMMAND_NAMES.PREBATTLE_WAYPOINT: MarkerType.LOCATION_MARKER_TYPE, 
   BATTLE_CHAT_COMMAND_NAMES.RELOADING_READY: MarkerType.VEHICLE_MARKER_TYPE, 
   BATTLE_CHAT_COMMAND_NAMES.POSITIVE: MarkerType.VEHICLE_MARKER_TYPE, 
   BATTLE_CHAT_COMMAND_NAMES.AFFIRMATIVE: MarkerType.VEHICLE_MARKER_TYPE, 
   BATTLE_CHAT_COMMAND_NAMES.NEGATIVE: MarkerType.VEHICLE_MARKER_TYPE, 
   BATTLE_CHAT_COMMAND_NAMES.CONFIRM: MarkerType.VEHICLE_MARKER_TYPE, 
   BATTLE_CHAT_COMMAND_NAMES.ATTACK_OBJECTIVE: MarkerType.HEADQUARTER_MARKER_TYPE, 
   BATTLE_CHAT_COMMAND_NAMES.DEFEND_OBJECTIVE: MarkerType.HEADQUARTER_MARKER_TYPE, 
   BATTLE_CHAT_COMMAND_NAMES.ATTACKING_OBJECTIVE: MarkerType.HEADQUARTER_MARKER_TYPE, 
   BATTLE_CHAT_COMMAND_NAMES.DEFENDING_OBJECTIVE: MarkerType.HEADQUARTER_MARKER_TYPE, 
   BATTLE_CHAT_COMMAND_NAMES.VEHICLE_SPOTPOINT: MarkerType.LOCATION_MARKER_TYPE, 
   BATTLE_CHAT_COMMAND_NAMES.SHOOTING_POINT: MarkerType.LOCATION_MARKER_TYPE, 
   BATTLE_CHAT_COMMAND_NAMES.NAVIGATION_POINT: MarkerType.LOCATION_MARKER_TYPE}
CHAT_COMMANDS_THAT_IGNORE_COOLDOWNS = [
 BATTLE_CHAT_COMMAND_NAMES.REPLY,
 BATTLE_CHAT_COMMAND_NAMES.CANCEL_REPLY,
 BATTLE_CHAT_COMMAND_NAMES.CLEAR_CHAT_COMMANDS]
BLOCKING_TEAM_COMM_CHAT_COMMANDS = [
 BATTLE_CHAT_COMMAND_NAMES.ATTENTION_TO_POSITION]

def getUniqueTeamOrControlPointID(baseTeamID, baseID):
    return baseID | baseTeamID << 4


def getBaseTeamAndIDFromUniqueID(uniqueID):
    return (
     uniqueID >> 4, uniqueID & 15)