from gui.impl.gen.view_models.views.lobby.battle_results.stats_efficiency_model import StatsEfficiencyModel

class FunStatsEfficiencyModel(StatsEfficiencyModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(FunStatsEfficiencyModel, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(FunStatsEfficiencyModel, self)._initialize()