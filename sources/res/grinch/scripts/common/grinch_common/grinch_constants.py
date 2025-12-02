from collections import namedtuple
import enum, UnitBase, arena_bonus_type_caps, constants
from constants_utils import ConstInjector
from BattleFeedbackCommon import BATTLE_EVENT_TYPE as BET
if constants.IS_CLIENT:
    import logging
    _logger = logging.getLogger(__name__)
    _logWarning = _logger.warning
else:
    from debug_utils import LOG_DEBUG, LOG_WARNING as _logWarning

class GrinchAbilities(object):
    GRINCH_REPAIR_KIT = 'builtinGrinchRepairkit'
    GRINCH_TURRET = 'builtinGrinchTurret'
    GRINCH_HEAL = 'builtinGrinchHeal'
    GRINCH_BLIZZARD = 'builtinGrinchBlizzard'
    GRINCH_RAGE = 'builtinGrinchRage'
    GRINCH_FLARE = 'builtinGrinchFlare'
    GRINCH_STEALTH = 'builtinGrinchStealth'
    GRINCH_JUMP = 'builtinGrinchJump'
    GRINCH_MISSILES = 'builtinGrinchMissiles'
    GRINCH_DART = 'builtinGrinchDart'
    GRINCH_SONAR = 'builtinGrinchSonar'
    GRINCH_RAM = 'builtinGrinchRam'


class GrinchShells(object):
    SHELL_ASSAULT = '_152mm_AP_T_grinch'
    SHELL_CARRIER = '_105mm_OFL_105_D1504_grinch'
    SHELL_SUPPORT = '_105mm_AP_DM13_grinch'


class CapturablePointNames(object):
    CAPTURABLE_POINT_A = 'A'
    CAPTURABLE_POINT_B = 'B'
    CAPTURABLE_POINT_C = 'C'
    ALL = (CAPTURABLE_POINT_A, CAPTURABLE_POINT_B, CAPTURABLE_POINT_C)


class ARENA_GUI_TYPE(constants.ARENA_GUI_TYPE, ConstInjector):
    GRINCH = 106


class ARENA_BONUS_TYPE_CAPS(arena_bonus_type_caps.ARENA_BONUS_TYPE_CAPS, ConstInjector):
    _const_type = str
    GRINCH = 'GRINCH'


class ARENA_BONUS_TYPE(constants.ARENA_BONUS_TYPE, ConstInjector):
    GRINCH = 106


class QUEUE_TYPE(constants.QUEUE_TYPE, ConstInjector):
    GRINCH = 106


class PREBATTLE_TYPE(constants.PREBATTLE_TYPE, ConstInjector):
    GRINCH = 106


class UNIT_MGR_FLAGS(UnitBase.UNIT_MGR_FLAGS, ConstInjector):
    GRINCH = 524288


class ROSTER_TYPE(UnitBase.ROSTER_TYPE, ConstInjector):
    GRINCH = UNIT_MGR_FLAGS.SQUAD | UNIT_MGR_FLAGS.GRINCH


class INVITATION_TYPE(constants.INVITATION_TYPE, ConstInjector):
    GRINCH = PREBATTLE_TYPE.GRINCH


class ATTACK_REASON(constants.ATTACK_REASON, ConstInjector):
    _const_type = str
    REDIRECTED_DAMAGE = 'redirected_damage_from_bot'
    SLAVE_BOT_DAMAGED = 'slave_bot_damaged'
    BLIZZARD_ABILITY = 'damage_by_blizzard_ability'
    SONAR_ABILITY = 'damage_by_sonar_ability'
    SNOWSTORM = 'damage_by_snowstorm'
    BASE_DEFENDER_BONUS = 'base_defender_bonus'
    ABILITY_ASSIST_FLARE = 'ability_assist_flare'
    ABILITY_ASSIST_BLIZZARD = 'ability_assist_blizzard'
    ABILITY_ASSIST_BUFF = 'ability_assist_buff'
    RAGE = 'rage'
    DART = 'dart'
    ABILITY_ASSIST_SONAR = 'ability_assist_sonar'
    MISSILE_DAMAGE = 'missile_damage'


DAMAGE_INFO_CODES_PER_ATTACK_REASON = {ATTACK_REASON.BLIZZARD_ABILITY: 'DEATH_FROM_ABILITIES', 
   ATTACK_REASON.SNOWSTORM: 'DEATH_FROM_SNOWSTORM', 
   ATTACK_REASON.RAGE: 'DEATH_FROM_RAGE', 
   ATTACK_REASON.MISSILE_DAMAGE: 'DEATH_FROM_MISSILE', 
   ATTACK_REASON.DART: 'DEATH_FROM_DART', 
   ATTACK_REASON.SONAR_ABILITY: 'DEATH_FROM_SONAR'}
BATTLE_FEEDBACK_REASONS_AFTER_DEATH = {
 ATTACK_REASON.ABILITY_ASSIST_BUFF, ATTACK_REASON.ABILITY_ASSIST_FLARE,
 ATTACK_REASON.ABILITY_ASSIST_BLIZZARD, ATTACK_REASON.REDIRECTED_DAMAGE,
 ATTACK_REASON.SLAVE_BOT_DAMAGED, ATTACK_REASON.SNOWSTORM}

class GameSeasonType(constants.GameSeasonType, ConstInjector):
    GRINCH = 107


class CLIENT_UNIT_CMD(UnitBase.CLIENT_UNIT_CMD, ConstInjector):
    pass


class StatsActions(enum.Enum):
    DAMAGE = 'damage'
    RAMMING = 'ramming'
    RAM_ABILITY_DAMAGE = 'ramAbilityRamming'
    HIT_ASSIST = 'hitAssist'
    ABILITY_ASSIST_FLARE = 'abilityAssistFlare'
    ABILITY_ASSIST_BLIZZARD = 'abilityAssistBlizzard'
    ABILITY_ASSIST_BUFF = 'abilityAssistBuff'
    ABILITY_ASSIST_SONAR = 'abilityAssistSonar'
    KILL = 'kill'
    BASE_DEFENDER_BONUS = 'baseDefenderBonus'
    ENEMY_DETECTION = 'enemyDetection'
    PRESENTS_DELIVERY = 'presentsDelivery'
    PRESENTS_PICKED_UP = 'presentsPickedUp'
    BIG_PRESENTS_DELIVERY = 'bigPresentsDelivery'
    PRESENTS_THEFT = 'presentsTheft'
    BIG_PRESENTS_THEFT = 'bigPresentsTheft'
    PRESENTS_STEALTH_THEFT = 'presentsStealthTheft'
    PRESENT_CARRIER_KILLED = 'carrierKilled'
    BIG_PRESENT_CARRIER_KILLED = 'bigCarrierKilled'
    TURRET_DAMAGE = 'turretDamage'
    RAGE_DAMAGE = 'rageDamage'
    STEALTH_DAMAGE = 'stealthDamage'
    HEAL = 'heal'
    FROZEN_KILL = 'frozenKill'
    CLOSE_RANGE_DAMAGE = 'closeRangeDamage'
    FLARED_DAMAGE = 'flaredDamage'
    SONAR_DAMAGE = 'sonarDamage'
    DAMAGE_TO_VEHICLES_UNDER_SONAR = 'damageToVehiclesUnderSonar'
    ALL_PRESENTS_DELIVERY = 'allPresentsDelivery'
    DAMAGE_VEHICLES_UNDER_DART = 'damageToVehiclesUnderDart'
    MISSILE_DAMAGE = 'missileDamage'
    MINI_BASE_CAPTURE = 'miniBaseCapture'
    MINI_BASE_RECAPTURE = 'miniBaseRecapture'
    DAMAGE_TO_ASSAULT = 'damageToAssault'
    KILL_VEHICLE_CARRIER = 'killCarrier'
    KILL_VEHICLE_DEFENDER = 'killDefender'
    DAMAGE_TO_TURRETS = 'damageToTurrets'
    NONE = 'none'


ACTIONS_AWARDING_PROGRESS_POINTS = (
 StatsActions.DAMAGE, StatsActions.HIT_ASSIST, StatsActions.ABILITY_ASSIST_FLARE,
 StatsActions.KILL, StatsActions.BASE_DEFENDER_BONUS, StatsActions.ENEMY_DETECTION,
 StatsActions.PRESENTS_DELIVERY, StatsActions.ABILITY_ASSIST_BLIZZARD,
 StatsActions.ABILITY_ASSIST_BUFF, StatsActions.ABILITY_ASSIST_SONAR,
 StatsActions.RAMMING)
ACTIONS_AWARDING_PROGRESS_POINTS_REMAP = {StatsActions.BIG_PRESENTS_DELIVERY: StatsActions.PRESENTS_DELIVERY}
ACTION_AWARDING_GROUPING = {StatsActions.PRESENTS_DELIVERY: (
                                  StatsActions.ALL_PRESENTS_DELIVERY,), 
   StatsActions.BIG_PRESENTS_DELIVERY: (
                                      StatsActions.ALL_PRESENTS_DELIVERY,)}
BattleEventTypeInfo = namedtuple('BattleEventTypeInfo', ('battleEventType', 'attackReason'))
STATS_ACTION_TO_BET_INFO = {StatsActions.PRESENTS_DELIVERY: BattleEventTypeInfo(BET.BASE_CAPTURE_DROPPED, None), 
   StatsActions.BIG_PRESENTS_DELIVERY: BattleEventTypeInfo(BET.BASE_CAPTURE_DROPPED, None), 
   StatsActions.ABILITY_ASSIST_FLARE: BattleEventTypeInfo(BET.DAMAGE, ATTACK_REASON.ABILITY_ASSIST_FLARE), 
   StatsActions.ABILITY_ASSIST_BLIZZARD: BattleEventTypeInfo(BET.DAMAGE, ATTACK_REASON.ABILITY_ASSIST_BLIZZARD), 
   StatsActions.ABILITY_ASSIST_BUFF: BattleEventTypeInfo(BET.DAMAGE, ATTACK_REASON.ABILITY_ASSIST_BUFF), 
   StatsActions.BASE_DEFENDER_BONUS: BattleEventTypeInfo(BET.DAMAGE, ATTACK_REASON.BASE_DEFENDER_BONUS), 
   StatsActions.SONAR_DAMAGE: BattleEventTypeInfo(BET.DAMAGE, ATTACK_REASON.SONAR_ABILITY), 
   StatsActions.DAMAGE_TO_VEHICLES_UNDER_SONAR: BattleEventTypeInfo(BET.DAMAGE, ATTACK_REASON.SONAR_ABILITY), 
   StatsActions.ABILITY_ASSIST_SONAR: BattleEventTypeInfo(BET.DAMAGE, ATTACK_REASON.ABILITY_ASSIST_SONAR)}

class GrinchClientArenaComponents(object):
    GRINCH_VISUAL_STATE_GO_STORAGE = 'grinchVisualStateGOStorage'


class Configs(enum.Enum):
    GRINCH_CONFIG = 'grinch_config'


class EventStates(enum.Enum):
    START = 0
    BATTLES_FINISH = 1
    SUSPEND = 2
    RESUME = 3
    ENDED = 4


class Teams(enum.IntEnum):
    NONE = 0
    CYAN = 1
    YELL = 2
    MGNT = 3
    BOTS = 4


PLAYER_TEAMS = (
 Teams.CYAN,
 Teams.YELL,
 Teams.MGNT)
PLAYER_VEHICLE_TYPES = ('lightTank', 'mediumTank', 'heavyTank')
TURRET_SPHERE_COLLIDER_RADIUS = 3

class GrinchModeSelectorRewardID(enum.Enum):
    ATTACHMENT_3D = 'attachment3D'
    STYLE_2D = 'style2D'


VEHICLE_MARKER_UPDATE_TIME = 0.1

class MissileExplosionRaycast(object):
    IS_ENABLED = True
    CORE_SIZE = (0.5, 1.5, 0.5)
    HARD_RADIUS = 2.0
    RESOLUTION = (4, 3)
    H_BORDERS = (0.1, 0.1)
    V_BORDERS = (0.2, 0.1)
    DEFAULT_EFFICIENCY = 0.5
    PENETRATION_THRESHOLD = 0.3
    SINGLE_RAY_IMPACT = 0.5
    MULTI_RAY_IMPACT = 1
    RAYCAST_LIMIT = 200


EXPLOSION_PARAMS = (
 MissileExplosionRaycast.CORE_SIZE,
 MissileExplosionRaycast.HARD_RADIUS,
 MissileExplosionRaycast.RESOLUTION[0],
 MissileExplosionRaycast.RESOLUTION[1],
 MissileExplosionRaycast.H_BORDERS,
 MissileExplosionRaycast.V_BORDERS,
 MissileExplosionRaycast.DEFAULT_EFFICIENCY,
 MissileExplosionRaycast.PENETRATION_THRESHOLD,
 MissileExplosionRaycast.SINGLE_RAY_IMPACT,
 MissileExplosionRaycast.MULTI_RAY_IMPACT,
 MissileExplosionRaycast.RAYCAST_LIMIT)
NETWORK_TOLERANCE = 0.05
TURRET_MINIMUM_ROTATION = 0.75

class CaptureStates(enum.IntEnum):
    NEUTRAL = 0
    CAPTURED = 1
    CAN_BE_RECAPTURED = 2

    def transitionTo(self, target):
        if self.value == target:
            _logWarning('Grinch: CaptureState is already in this state')
            return self
        if target is CaptureStates.NEUTRAL:
            _logWarning('Grinch: Cannot return to NEUTRAL state, once it has been left.')
            return self
        if target is CaptureStates.CAN_BE_RECAPTURED and self.value == self.NEUTRAL:
            _logWarning('Grinch: CaptureState cannot transition from NEUTRAL to CAN_BE_RECAPTURED')
            return self
        LOG_DEBUG('Grinch_minibase: CaptureStates: transition from ', self.value, ' to ', target, nice=True)
        return target


GRINCH_INVADER_COMPONENT = 'GrinchInvaderComponent'
CAPTURABLE_BASE_MAP_GEOMETRY_ID = 2027

class GrinchVehicleClasses(enum.IntEnum):
    DEFENDER = 0
    CARRIER = 1
    ASSAULT = 2


DEFENDER_VEHICLE_TYPE = 'germany:G89_Leopard1_grinch'
ASSAULT_VEHICLE_TYPE = 'china:Ch48_BZ_75_grinch'
CARRIER_VEHICLE_TYPE = 'france:F88_AMX_13_105_grinch'
grinchVehicleTypeToClass = {DEFENDER_VEHICLE_TYPE: GrinchVehicleClasses.DEFENDER, 
   CARRIER_VEHICLE_TYPE: GrinchVehicleClasses.CARRIER, 
   ASSAULT_VEHICLE_TYPE: GrinchVehicleClasses.ASSAULT}

class MissileLauncherStatuses(enum.IntEnum):
    IDLE = 0
    RELOADING = 1
    PREPARING = 2
    CANCEL_PREPARING = 3
    SHOT = 4


SWITCHING_AREA_PERCENTAGE = 0.04
Y_CENTER_OFFSET_PERCENTAGE = 0.08
MISSILE_ABILITY_EQUIPMENT_ID = 22011
TARGET_LOST_MARKER_DISABLE_ANIMATION_DELAY = 0.5