from frameworks.wulf import Array
from fun_random.gui.impl.gen.view_models.views.lobby.feature.battle_results.fun_player_model import FunPlayerModel
from gui.impl.gen.view_models.views.lobby.battle_results.team_stats_model import TeamStatsModel

class FunTeamStatsModel(TeamStatsModel):
    __slots__ = ()

    def __init__(self, properties=9, commands=1):
        super(FunTeamStatsModel, self).__init__(properties=properties, commands=commands)

    def getAllies(self):
        return self._getArray(5)

    def setAllies(self, value):
        self._setArray(5, value)

    @staticmethod
    def getAlliesType():
        return FunPlayerModel

    def getEnemies(self):
        return self._getArray(6)

    def setEnemies(self, value):
        self._setArray(6, value)

    @staticmethod
    def getEnemiesType():
        return FunPlayerModel

    def getSortingColumn(self):
        return self._getString(7)

    def setSortingColumn(self, value):
        self._setString(7, value)

    def getIsSingleTeamPostbattle(self):
        return self._getBool(8)

    def setIsSingleTeamPostbattle(self, value):
        self._setBool(8, value)

    def _initialize(self):
        super(FunTeamStatsModel, self)._initialize()
        self._addArrayProperty('allies', Array())
        self._addArrayProperty('enemies', Array())
        self._addStringProperty('sortingColumn', 'spiritPoints')
        self._addBoolProperty('isSingleTeamPostbattle', False)