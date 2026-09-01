from __future__ import absolute_import
from enum import Enum

class PresenterUpdateTypes(object):
    XP_BONUS = 'updateXpBonus'


class CommonTooltipType(Enum):
    EFFICIENCY_PARAMETER = 'efficiencyParameter'
    CRITICAL_DAMAGE_EFFICIENCY_PARAMETER = 'criticalDamageEfficiencyParameter'