from gui.Scaleform.daapi.view.battle.shared.indicators import _DamageIndicator
from gui.battle_control.battle_constants import HIT_INDICATOR_MAX_ON_SCREEN

class LunarPossessionDamageIndicator(_DamageIndicator):
    pass


def createLunarPossessionDamageIndicator():
    return LunarPossessionDamageIndicator(HIT_INDICATOR_MAX_ON_SCREEN)