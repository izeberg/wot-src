from gui.impl.gen.view_models.views.lobby.battle_results.team_stats_column_types import TeamStatsColumnTypes

class FunTeamStatsColumnTypes(TeamStatsColumnTypes):
    __slots__ = ()
    SPIRIT_POINTS = 'spiritPoints'

    def __init__(self, properties=0, commands=0):
        super(FunTeamStatsColumnTypes, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(FunTeamStatsColumnTypes, self)._initialize()