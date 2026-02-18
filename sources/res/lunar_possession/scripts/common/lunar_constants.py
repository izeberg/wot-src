from enum import IntEnum
from fun_random_common import fun_constants
from fun_random_common.fun_constants_utils import addArenaGuiTypesFromExtensionToFunRange
import arena_bonus_type_caps, constants, BattleFeedbackCommon
from constants_utils import ConstInjector, addArenaGuiTypesFromExtension, addArenaBonusCapsFromExtension, addAttackReasonTypesFromExtension, addDamageInfoCodes, addBattleEventTypesFromExtension
LUNAR_ARENA_EVENT_COMPONENT = 'LunarArenaEventsComponent'
LUNAR_SPIRIT_EVENTS_TRACKER = 'LunarSpiritEventsTracker'
LUNAR_SCORE_COMPONENT = 'LunarScoreComponent'
LUNAR_DEVELOPMENT_HELPER = 'LunarDevelopmentHelper'
LUNAR_ARENA_COMPONENT = 'LunarPossessionArenaComponent'
LUNAR_VEHICLE_FEEDBACK = 'LunarVehicleFeedbackComponent'
LUNAR_VEHICLE_CONTROL_LOCK_COMPONENT = 'LunarVehicleControlsLockComponent'
LUNAR_SPIRIT_BUFF = 'LunarSpiritBuffComponent'
LUNAR_HIGHLIGHTER_COMPONENT = 'LunarHighlighterComponent'
LUNAR_HEALTH_MULTIPLIER = 'LunarHealthMultiplierComponent'
LUNAR_SPIRIT_DOT_COMPONENT = 'LunarSpiritCarrierDotComponent'
LUNAR_ACCOUNT_EQUIPMENT_CONTROLLER = 'LunarAccountEquipmentController'
SPIRIT_BUFF_COMPONENT_COLLECTION = (
 LUNAR_SPIRIT_BUFF,
 LUNAR_HIGHLIGHTER_COMPONENT,
 LUNAR_HEALTH_MULTIPLIER,
 LUNAR_SPIRIT_DOT_COMPONENT)

class SpiritStatsCollected(object):
    LUNAR_SPIRIT_DELIVERIES = 'lunarSpiritDeliveries'
    LUNAR_SPIRIT_CARRIERS_DESTROYED = 'lunarSpiritCarriersDestroyed'
    LUNAR_SPIRIT_CARRIERS_DAMAGED = 'lunarSpiritCarriersDamaged'
    LUNAR_SPIRIT_SCORE = 'lunarSpiritScore'


class ARENA_BONUS_TYPE_CAPS(arena_bonus_type_caps.ARENA_BONUS_TYPE_CAPS, ConstInjector):
    _const_type = str
    LUNAR_POSSESSION = 'LUNAR_POSSESSION'


class ARENA_GUI_TYPE(constants.ARENA_GUI_TYPE, ConstInjector):
    LUNAR_POSSESSION = 112


class ATTACK_REASON(constants.ATTACK_REASON, ConstInjector):
    _const_type = str
    SPIRIT_CARRIER_DOT = 'spirit_carrier_dot'


DAMAGE_INFO_CODES_PER_ATTACK_REASON = {ATTACK_REASON.SPIRIT_CARRIER_DOT: 'DEATH_FROM_SPIRIT_CARRIER_DOT'}

class FunSubModeImpl(fun_constants.FunSubModeImpl, ConstInjector):
    LUNAR_POSSESSION = 2


class BATTLE_EVENT_TYPE(BattleFeedbackCommon.BATTLE_EVENT_TYPE, ConstInjector):
    LUNAR_SCORE = 108


class RoundEndReasonEnum(IntEnum):
    TEAM_DESTROYED = 0
    SPIRIT_DELIVERED = 1


def injectConsts(personality):
    addArenaGuiTypesFromExtension(ARENA_GUI_TYPE, personality)
    addArenaGuiTypesFromExtensionToFunRange(ARENA_GUI_TYPE)
    addArenaBonusCapsFromExtension(ARENA_BONUS_TYPE_CAPS, personality)
    addAttackReasonTypesFromExtension(ATTACK_REASON, personality)
    addDamageInfoCodes(DAMAGE_INFO_CODES_PER_ATTACK_REASON, personality)
    addBattleEventTypesFromExtension(BATTLE_EVENT_TYPE, personality)