from gui.impl.gen import R
from gui.impl.lobby.tooltips.additional_rewards_tooltip import AdditionalRewardsTooltip

class OTGEquipmentSetTooltipView(AdditionalRewardsTooltip):

    @classmethod
    def _getHeader(cls):
        return R.strings.one_time_gift.equipmentSet.tooltip.header()