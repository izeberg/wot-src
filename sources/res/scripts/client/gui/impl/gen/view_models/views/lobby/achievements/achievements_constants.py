from enum import Enum
from frameworks.wulf import ViewModel

class KPITypes(Enum):
    BATTLES = 'battles'
    ASSISTANCE = 'assistance'
    DESTROYED = 'destroyed'
    BLOCKED = 'blocked'
    EXPERIENCE = 'experience'
    DAMAGE = 'damage'


class AchievementsConstants(ViewModel):
    __slots__ = ()

    def __init__(self, properties=0, commands=0):
        super(AchievementsConstants, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(AchievementsConstants, self)._initialize()