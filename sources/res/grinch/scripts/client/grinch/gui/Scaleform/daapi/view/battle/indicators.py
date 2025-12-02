from gui.battle_control.battle_constants import HIT_INDICATOR_MAX_ON_SCREEN
from gui.Scaleform.daapi.view.battle.shared.indicators import _DamageIndicator

class GrinchDamageIndicator(_DamageIndicator):
    _DAMAGE_INDICATOR_SWF = 'grinch|grinchBattleDamageIndicatorApp.swf'


def grinchCreateDamageIndicator():
    return GrinchDamageIndicator(HIT_INDICATOR_MAX_ON_SCREEN)