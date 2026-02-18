from __future__ import absolute_import
import typing
from goodies.goodie_constants import GOODIE_VARIETY
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.shared.missions.packers.bonus import GoodiesBonusUIPacker
from gui.impl.backport import TooltipData
from gui.impl.gen.view_models.common.missions.bonuses.icon_bonus_model import IconBonusModel
from gui.server_events.awards_formatters import GoodiesBonusFormatter
from helpers import dependency
from skeletons.gui.goodies import IGoodiesCache
if typing.TYPE_CHECKING:
    from typing import List
    from gui.server_events.bonuses import GoodiesBonus
    from gui.server_events.awards_formatters import PreformattedBonus

class FunRandomGoodiesBonusUIPacker(GoodiesBonusUIPacker):

    @classmethod
    def _pack(cls, bonus):
        result = GoodiesBonusUIPacker._pack(bonus)
        result.sort(reverse=True, key=lambda item: item.getIcon() == GOODIE_VARIETY.MENTORING_LICENSE_NAME)
        return result

    @classmethod
    def _getToolTip(cls, bonus):
        result = GoodiesBonusUIPacker._getToolTip(bonus)
        result.sort(reverse=True, key=lambda item: item.tooltip == TOOLTIPS_CONSTANTS.MENTOR_LICENSE)
        return result


class FunRandomGoodiesBonusFormatter(GoodiesBonusFormatter):
    __goodiesCache = dependency.descriptor(IGoodiesCache)

    def _format(self, bonus):
        result = super(FunRandomGoodiesBonusFormatter, self)._format(bonus)
        result.sort(reverse=True, key=self.__sortBonuses)
        return result

    def __sortBonuses(self, bonus):
        if isinstance(bonus.specialArgs, list) and bonus.specialArgs:
            goodieID = bonus.specialArgs[0]
            goodieData = self.__goodiesCache.getGoodieByID(goodieID)
            return goodieData and goodieData.variety == GOODIE_VARIETY.MENTORING_LICENSE
        return False