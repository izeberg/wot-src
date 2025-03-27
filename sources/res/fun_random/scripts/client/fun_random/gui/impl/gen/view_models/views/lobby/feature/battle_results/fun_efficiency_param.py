from frameworks.wulf import ViewModel

class FunEfficiencyParam(ViewModel):
    __slots__ = ()
    FINISH_TIME = 'finishTime'
    FINISH_POSITION = 'finishPosition'
    CHECKPOINTS_PASSED = 'checkpointsPassed'
    DESTROYED = 'kills'
    DEATH_COUNT = 'deathCount'

    def __init__(self, properties=0, commands=0):
        super(FunEfficiencyParam, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(FunEfficiencyParam, self)._initialize()