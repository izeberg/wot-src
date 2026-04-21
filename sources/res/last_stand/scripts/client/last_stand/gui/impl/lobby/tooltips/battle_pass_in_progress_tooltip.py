from __future__ import absolute_import
from gui.impl.gen import R
from gui.impl.lobby.battle_pass.tooltips.battle_pass_in_progress_tooltip_view import BattlePassInProgressTooltipView

class LSBattlePassInProgressTooltipView(BattlePassInProgressTooltipView):
    LAYOUT_ID = R.views.last_stand.mono.lobby.tooltips.battle_pass_tooltip()

    def _hasRewardPoints(self):
        return False