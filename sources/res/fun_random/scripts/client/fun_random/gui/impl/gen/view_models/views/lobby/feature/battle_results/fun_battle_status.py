from frameworks.wulf import ViewModel

class FunBattleStatus(ViewModel):
    __slots__ = ()
    FINISHED = 'finished'
    NOT_FINISHED = 'notFinished'

    def __init__(self, properties=0, commands=0):
        super(FunBattleStatus, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(FunBattleStatus, self)._initialize()