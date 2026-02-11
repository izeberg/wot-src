from __future__ import absolute_import
from fun_random.gui.impl.gen.view_models.views.lobby.feature.battle_results.fun_team_stats_column_types import FunTeamStatsColumnTypes
from fun_random.gui.impl.gen.view_models.views.lobby.feature.battle_results.fun_player_model import FunPlayerModel
from gui.battle_results.presenters.packers.interfaces import IBattleResultsPacker
from gui.battle_results.presenters.packers.team.team_stats_packer import TeamStats
from gui.battle_results.presenters.packers.user_info import UserNames
from gui.battle_results.settings import BATTLE_RESULTS_RECORD as _RECORD
from gui.impl.gen.view_models.views.lobby.battle_results.team_stats_model import SortingOrder

class LunarTeamStats(TeamStats):
    _PLAYER_MODEL_CLS = FunPlayerModel
    _STATS_VALUES_COLUMNS = {FunTeamStatsColumnTypes.DAMAGE: None, 
       FunTeamStatsColumnTypes.FRAG: None, 
       FunTeamStatsColumnTypes.SPIRIT_POINTS: None}
    _SORTING_PRIORITIES = (
     (
      FunTeamStatsColumnTypes.SPIRIT_POINTS, SortingOrder.DESC),
     (
      FunTeamStatsColumnTypes.DAMAGE, SortingOrder.DESC),
     (
      FunTeamStatsColumnTypes.PLAYER, SortingOrder.ASC))

    @classmethod
    def _packEfficiency(cls, efficiencyModel, summarizeInfo):
        super(LunarTeamStats, cls)._packEfficiency(efficiencyModel, summarizeInfo)
        efficiencyModel.setSpiritPoints(summarizeInfo.spiritPoints)


class LunarPersonalInfo(IBattleResultsPacker):

    @classmethod
    def packModel(cls, model, battleResults):
        reusable, results = battleResults.reusable, battleResults.results
        vehicleSumInfo = reusable.getPersonalVehiclesInfo(results[_RECORD.PERSONAL])
        UserNames.packBaseUserNames(model.userNames, reusable.getPlayerInfo(), vehicleSumInfo, battleResults)