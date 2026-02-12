from __future__ import absolute_import
import typing
from fun_random.gui.battle_results.sub_presenters.fun_team_stats import FunTeamStatsSubPresenter
from lunar_possession.gui.battle_results.packers.lunar_packers import LunarTeamStats
if typing.TYPE_CHECKING:
    from gui.battle_results.stats_ctrl import BattleResults

class LunarTeamStatsSubPresenter(FunTeamStatsSubPresenter):

    def packBattleResults(self, battleResults):
        with self.getViewModel().transaction() as (model):
            LunarTeamStats.packModel(model, battleResults)