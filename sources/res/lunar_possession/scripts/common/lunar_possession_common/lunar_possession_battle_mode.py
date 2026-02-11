from fun_random_common.fun_battle_mode import FunRandomBattleMode
from lunar_constants import ARENA_GUI_TYPE
from lunar_possession_common.battle_results import lunar

class LunarPossessionBattleMode(FunRandomBattleMode):
    _ARENA_GUI_TYPE = ARENA_GUI_TYPE.LUNAR_POSSESSION
    _BATTLE_RESULTS_CONFIG = lunar