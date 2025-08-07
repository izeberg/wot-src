from frameworks.wulf import ViewModel

class MarkerViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(MarkerViewModel, self).__init__(properties=properties, commands=commands)

    def getAvailableEnvelopesAmount(self):
        return self._getNumber(0)

    def setAvailableEnvelopesAmount(self, value):
        self._setNumber(0, value)

    def getIsVisible(self):
        return self._getBool(1)

    def setIsVisible(self, value):
        self._setBool(1, value)

    def _initialize(self):
        super(MarkerViewModel, self)._initialize()
        self._addNumberProperty('availableEnvelopesAmount', 0)
        self._addBoolProperty('isVisible', True)