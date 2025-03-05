import logging, typing
from comp7.gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as COMP7_TOOLTIPS
from comp7.gui.selectable_reward.constants import Features
from gui.impl.backport import TooltipData
from gui.selectable_reward.common import SelectableRewardManager
if typing.TYPE_CHECKING:
    pass
_logger = logging.getLogger(__name__)

class Comp7SelectableRewardManager(SelectableRewardManager):
    _FEATURE = Features.COMP7

    @classmethod
    def getTabTooltipData(cls, selectableBonus):
        tokenID = selectableBonus.getValue().keys()[0]
        if cls.isFeatureReward(tokenID):
            return TooltipData(tooltip=None, isSpecial=True, specialAlias=COMP7_TOOLTIPS.COMP7_SELECTABLE_REWARD, specialArgs=[
             cls._getGiftTokenFromOffer(tokenID), True])
        else:
            return