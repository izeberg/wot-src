import CommandMapping
from constants_utils import ConstInjector
from gui.prb_control import settings
from gui.Scaleform.daapi.settings import views
from gui.server_events import cond_formatters
from messenger import m_constants
from personal_missions_constants import CONDITION_ICON
ABILITY_COMMANDS = (
 CommandMapping.CMD_AMMO_CHOICE_1,
 CommandMapping.CMD_AMMO_CHOICE_2,
 CommandMapping.CMD_AMMO_CHOICE_3,
 CommandMapping.CMD_CM_VEHICLE_SWITCH_AUTOROTATION)

class FUNCTIONAL_FLAG(settings.FUNCTIONAL_FLAG, ConstInjector):
    GRINCH = 68719476736


class PREBATTLE_ACTION_NAME(settings.PREBATTLE_ACTION_NAME, ConstInjector):
    _const_type = str
    GRINCH = 'grinch'
    GRINCH_SQUAD = 'grinchSquad'


class SELECTOR_BATTLE_TYPES(settings.SELECTOR_BATTLE_TYPES, ConstInjector):
    _const_type = str
    GRINCH = 'grinch'


class VIEW_ALIAS(views.VIEW_ALIAS, ConstInjector):
    _const_type = str
    GRINCH_BATTLE_PAGE = 'grinchBattlePage'
    GRINCH_LOADING = 'grinchLoading'
    GRINCH_SETTINGS_WINDOW = 'grinchSettingsWindow'


class SCH_CLIENT_MSG_TYPE(m_constants.SCH_CLIENT_MSG_TYPE, ConstInjector):
    GRINCH_EVENT_STATE = 421
    GRINCH_EVENT_PROGRESSION = 422
    GRINCH_CONGRATULATIONS_MESSAGE = 423


BATTLE_RESULTS_KEYS = {'grinch/rageDamage': CONDITION_ICON.EXPERIENCE, 
   'grinch/frozenKill': CONDITION_ICON.EXPERIENCE, 
   'grinch/closeRangeDamage': CONDITION_ICON.EXPERIENCE, 
   'grinch/heal': CONDITION_ICON.EXPERIENCE, 
   'grinch/turretDamage': CONDITION_ICON.EXPERIENCE, 
   'grinch/carrierKilled': CONDITION_ICON.EXPERIENCE, 
   'grinch/presentsStealthTheft': CONDITION_ICON.EXPERIENCE, 
   'grinch/presentsDelivery': CONDITION_ICON.EXPERIENCE, 
   'grinch/allPresentsDelivery': CONDITION_ICON.EXPERIENCE, 
   'grinch/flaredDamage': CONDITION_ICON.EXPERIENCE, 
   'grinch/killDefender': CONDITION_ICON.EXPERIENCE, 
   'grinch/progressionPoints': CONDITION_ICON.EXPERIENCE, 
   'grinch/totalGrinchPoints': CONDITION_ICON.EXPERIENCE, 
   'grinch/damageToTurrets': CONDITION_ICON.EXPERIENCE, 
   'grinch/damageToVehiclesUnderDart': CONDITION_ICON.EXPERIENCE, 
   'grinch/damageToAssault': CONDITION_ICON.EXPERIENCE, 
   'grinch/stealthDamage': CONDITION_ICON.EXPERIENCE, 
   'grinch/personalPlace': CONDITION_ICON.EXPERIENCE, 
   'grinch/missileDamage': CONDITION_ICON.EXPERIENCE, 
   'grinch/damageToVehiclesUnderSonar': CONDITION_ICON.EXPERIENCE, 
   'grinch/killCarrier': CONDITION_ICON.EXPERIENCE}
cond_formatters.BATTLE_RESULTS_KEYS.update(BATTLE_RESULTS_KEYS)
GRINCH_LOCK_SOURCE_NAME = 'grinchNotificationLockSource'