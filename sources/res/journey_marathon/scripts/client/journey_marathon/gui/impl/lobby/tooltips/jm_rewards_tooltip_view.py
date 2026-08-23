from __future__ import absolute_import
import typing
from frameworks.wulf import ViewSettings
from frameworks.wulf.view.array import fillViewModelsArray
from gui.impl.gen import R
from gui.impl.pub import ViewImpl
from journey_marathon.gui.impl.gen.view_models.views.lobby.src.views.tooltips.rewards_tooltip_model import RewardsTooltipModel
if typing.TYPE_CHECKING:
    from frameworks.wulf import Array
    from gui.impl.gen.view_models.common.bonus_model import BonusModel

class JmRewardsTooltipView(ViewImpl):
    LAYOUT_ID = R.views.journey_marathon.mono.lobby.tooltips.rewards_tooltip()
    __slots__ = ('__bonusModels', )

    def __init__(self, bonusModels):
        super(JmRewardsTooltipView, self).__init__(settings=ViewSettings(layoutID=self.LAYOUT_ID, model=RewardsTooltipModel()))
        self.__bonusModels = bonusModels

    def _onLoading(self, *args, **kwargs):
        super(JmRewardsTooltipView, self)._onLoading(*args, **kwargs)
        with self.getViewModel().transaction() as (tx):
            fillViewModelsArray(self.__bonusModels, tx.getBonuses())