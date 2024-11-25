from frameworks.wulf import ViewModel

class MarkerViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(MarkerViewModel, self).__init__(properties=properties, commands=commands)

    def getAvailableDoorsAmount(self):
        return self._getNumber(0)

    def setAvailableDoorsAmount(self, value):
        self._setNumber(0, value)

    def getIsVisible(self):
        return self._getBool(1)

    def setIsVisible(self, value):
        self._setBool(1, value)

    def getIsFirstDay(self):
        return self._getBool(2)

    def setIsFirstDay(self, value):
        self._setBool(2, value)

    def _initialize(self):
        super(MarkerViewModel, self)._initialize()
        self._addNumberProperty('availableDoorsAmount', 0)
        self._addBoolProperty('isVisible', True)
        self._addBoolProperty('isFirstDay', False)