from frameworks.wulf import ViewModel

class NyTerminalMarkerModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(NyTerminalMarkerModel, self).__init__(properties=properties, commands=commands)

    def getCount(self):
        return self._getNumber(0)

    def setCount(self, value):
        self._setNumber(0, value)

    def getIsVisible(self):
        return self._getBool(1)

    def setIsVisible(self, value):
        self._setBool(1, value)

    def _initialize(self):
        super(NyTerminalMarkerModel, self)._initialize()
        self._addNumberProperty('count', 0)
        self._addBoolProperty('isVisible', True)