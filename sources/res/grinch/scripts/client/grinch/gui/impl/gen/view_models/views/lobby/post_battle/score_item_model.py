from enum import Enum
from frameworks.wulf import ViewModel

class ScoreTypeEnum(Enum):
    DAMAGECAUSED = 'damage_caused'
    DESTROYED = 'destroyed'
    SPOTANDDAMAGEASSIST = 'spot_and_damage_assist'
    BASEDEFENDED = 'base_defended'
    DELIVERED = 'delivered'
    ABILITYASSIST = 'ability_assist'
    RAM = 'ram'


class ScoreItemModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(ScoreItemModel, self).__init__(properties=properties, commands=commands)

    def getType(self):
        return ScoreTypeEnum(self._getString(0))

    def setType(self, value):
        self._setString(0, value.value)

    def getScore(self):
        return self._getNumber(1)

    def setScore(self, value):
        self._setNumber(1, value)

    def _initialize(self):
        super(ScoreItemModel, self)._initialize()
        self._addStringProperty('type', ScoreTypeEnum.DAMAGECAUSED.value)
        self._addNumberProperty('score', 0)