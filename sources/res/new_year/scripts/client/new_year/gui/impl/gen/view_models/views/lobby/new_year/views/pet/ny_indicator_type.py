from enum import Enum
from frameworks.wulf import ViewModel

class IndicatorType(Enum):
    FOOD = 'food'
    FUN = 'fun'
    ACTIVITY = 'activity'


class NyIndicatorType(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(NyIndicatorType, self).__init__(properties=properties, commands=commands)

    def getType(self):
        return IndicatorType(self._getString(0))

    def setType(self, value):
        self._setString(0, value.value)

    def _initialize(self):
        super(NyIndicatorType, self)._initialize()
        self._addStringProperty('type')