from enum import Enum
from frameworks.wulf import ViewModel

class FrontlineState(Enum):
    ANNOUNCE = 'announce'
    ACTIVE = 'active'
    FINISHED = 'finished'
    FROZEN = 'frozen'
    INTRO = 'intro'


class FrontlineConst(ViewModel):
    __slots__ = ()
    BATTLE_ABILITIES = 'battleAbilities'

    def __init__(self, properties=0, commands=0):
        super(FrontlineConst, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(FrontlineConst, self)._initialize()