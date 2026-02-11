from constants_utils import ConstInjector
from gui.Scaleform.daapi.settings import views
from gui.battle_control import battle_constants
from messenger import m_constants

class BATTLE_CTRL_ID(battle_constants.BATTLE_CTRL_ID, ConstInjector):
    LUNAR_POSSESSION_BATTLE_CTRL = 201


class VIEW_ALIAS(views.VIEW_ALIAS, ConstInjector):
    _const_type = str
    LUNAR_POSSESSION_BATTLE_PAGE = 'LunarPossessionBattlePage'


class SCH_CLIENT_MSG_TYPE(m_constants.SCH_CLIENT_MSG_TYPE, ConstInjector):
    pass


POINT_ZONE_ALLY_ICON = 'LunarAllyPointZoneUI'
POINT_ZONE_OPPONENT_ICON = 'LunarEnemyPointZoneUI'
VEHICLE_SPIRIT_INDICATOR = 'VehicleSpiritMarker'