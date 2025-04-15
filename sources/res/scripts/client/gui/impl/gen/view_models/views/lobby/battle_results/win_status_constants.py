from frameworks.wulf import ViewModel

class WinStatusConstants(ViewModel):
    __slots__ = ()
    WIN = 'win'
    DRAW = 'tie'
    LOSE = 'lose'

    def __init__(self, properties=0, commands=0):
        super(WinStatusConstants, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(WinStatusConstants, self)._initialize()