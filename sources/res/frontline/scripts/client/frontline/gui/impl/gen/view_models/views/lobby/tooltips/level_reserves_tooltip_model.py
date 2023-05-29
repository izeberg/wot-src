from frameworks.wulf import Array
from frameworks.wulf import ViewModel

class LevelReservesTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(LevelReservesTooltipModel, self).__init__(properties=properties, commands=commands)

    def getLevels(self):
        return self._getArray(0)

    def setLevels(self, value):
        self._setArray(0, value)

    @staticmethod
    def getLevelsType():
        return unicode

    def _initialize(self):
        super(LevelReservesTooltipModel, self)._initialize()
        self._addArrayProperty('levels', Array())