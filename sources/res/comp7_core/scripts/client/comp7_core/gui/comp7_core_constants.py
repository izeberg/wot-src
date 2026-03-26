from constants_utils import ConstInjector
from gui.battle_control import battle_constants

class BATTLE_CTRL_ID(battle_constants.BATTLE_CTRL_ID, ConstInjector):
    COMP7_VOIP_CTRL = 102
    COMP7_VEHICLE_BAN_CTRL = 105