from frameworks.wulf import ViewModel

class TeamStatsColumnTypes(ViewModel):
    __slots__ = ()
    SQUAD = 'squad'
    PLAYER = 'player'
    DAMAGE = 'damage'
    FRAG = 'frag'
    XP = 'xp'
    VEHICLE = 'tank'

    def __init__(self, properties=0, commands=0):
        super(TeamStatsColumnTypes, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(TeamStatsColumnTypes, self)._initialize()