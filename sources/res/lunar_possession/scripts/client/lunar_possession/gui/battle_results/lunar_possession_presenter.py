from fun_random.gui.battle_results.sub_presenters.fun_battle_info import FunBattleInfoSubPresenter
from fun_random.gui.battle_results.sub_presenters.fun_personal_efficiency import FunPersonalEfficiencySubPresenter
from fun_random.gui.battle_results.sub_presenters.fun_progression import FunProgressionSubPresenter
from fun_random.gui.impl.gen.view_models.views.lobby.feature.battle_results.fun_battle_results_view_model import FunBattleResultsViewModel
from gui.battle_results.presenters.battle_results_sub_presenter import BattleResultsSubPresenter
from lunar_possession.gui.battle_results.subpresenters.lunar_personal_info import LunarPersonalInfoSubPresenter
from lunar_possession.gui.battle_results.subpresenters.lunar_team_stats import LunarTeamStatsSubPresenter

class LunarPossessionBattleResultsPresenter(BattleResultsSubPresenter):
    __slots__ = ()

    def __init__(self, viewModel, parentView):
        super(LunarPossessionBattleResultsPresenter, self).__init__(viewModel, parentView)
        self.addSubPresenter(LunarPersonalInfoSubPresenter(viewModel, parentView))
        self.addSubPresenter(FunPersonalEfficiencySubPresenter(viewModel.getEfficiency(), parentView))
        self.addSubPresenter(FunBattleInfoSubPresenter(viewModel.battleInfo, parentView))
        self.addSubPresenter(LunarTeamStatsSubPresenter(viewModel.teamStats, parentView))
        self.addSubPresenter(FunProgressionSubPresenter(viewModel.progress, parentView))

    @classmethod
    def getViewModelType(cls):
        return FunBattleResultsViewModel