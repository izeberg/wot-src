from constants_utils import ConstInjector
from messenger import m_constants

class SCH_CLIENT_MSG_TYPE(m_constants.SCH_CLIENT_MSG_TYPE, ConstInjector):
    TANK_ACADEMY_TOKEN_AWARD = 700
    TANK_ACADEMY_BATTLE_AWARD = 701