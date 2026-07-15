from comp7_light.gui.impl.gen.view_models.views.lobby.battle_results.comp7_light_stats_efficiency_model import Comp7LightStatsEfficiencyModel
from gui.impl.gen.view_models.views.lobby.battle_results.random.random_player_model import RandomPlayerModel

class Comp7LightPlayerModel(RandomPlayerModel):
    __slots__ = ()
    NO_PLATOON_SQUAD_INDEX = 0
    SUPER_PLATOON_SQUAD_INDEX = -1

    def __init__(self, properties=14, commands=0):
        super(Comp7LightPlayerModel, self).__init__(properties=properties, commands=commands)

    @property
    def efficiencyValues(self):
        return self._getViewModel(13)

    @staticmethod
    def getEfficiencyValuesType():
        return Comp7LightStatsEfficiencyModel

    def _initialize(self):
        super(Comp7LightPlayerModel, self)._initialize()
        self._addViewModelProperty('efficiencyValues', Comp7LightStatsEfficiencyModel())