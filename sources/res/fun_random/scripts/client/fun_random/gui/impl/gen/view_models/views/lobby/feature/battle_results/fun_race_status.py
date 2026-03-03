from frameworks.wulf import ViewModel

class FunRaceStatus(ViewModel):
    __slots__ = ()
    FINISHED = 'finished'
    NOT_FINISHED = 'notFinished'

    def __init__(self, properties=0, commands=0):
        super(FunRaceStatus, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(FunRaceStatus, self)._initialize()