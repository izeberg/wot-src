from __future__ import absolute_import
from fall_tanks_constants import ARENA_GUI_TYPE
from fall_tanks_common.battle_results import fall_tanks
from fun_random_common.fun_battle_mode import FunRandomBattleMode

class FallTanksBattleMode(FunRandomBattleMode):
    _ARENA_GUI_TYPE = ARENA_GUI_TYPE.FALL_TANKS
    _BATTLE_RESULTS_CONFIG = fall_tanks