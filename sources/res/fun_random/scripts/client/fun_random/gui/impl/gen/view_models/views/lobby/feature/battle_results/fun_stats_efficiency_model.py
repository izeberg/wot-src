from gui.impl.gen.view_models.views.lobby.battle_results.stats_efficiency_model import StatsEfficiencyModel

class FunStatsEfficiencyModel(StatsEfficiencyModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(FunStatsEfficiencyModel, self).__init__(properties=properties, commands=commands)

    def getSpiritPoints(self):
        return self._getNumber(3)

    def setSpiritPoints(self, value):
        self._setNumber(3, value)

    def _initialize(self):
        super(FunStatsEfficiencyModel, self)._initialize()
        self._addNumberProperty('spiritPoints', 0)