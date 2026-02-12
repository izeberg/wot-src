from frameworks.wulf import ViewModel

class FunTeamStatsColumnTypes(ViewModel):
    __slots__ = ()
    FINISH_TIME = 'finishTime'
    FINISH_POSITION = 'finishPosition'
    CHECKPOINTS = 'checkpoints'

    def __init__(self, properties=0, commands=0):
        super(FunTeamStatsColumnTypes, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(FunTeamStatsColumnTypes, self)._initialize()