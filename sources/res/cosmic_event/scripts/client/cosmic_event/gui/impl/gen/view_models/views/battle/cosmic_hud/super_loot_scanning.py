from frameworks.wulf import ViewModel

class SuperLootScanning(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(SuperLootScanning, self).__init__(properties=properties, commands=commands)

    def getTimeLeft(self):
        return self._getNumber(0)

    def setTimeLeft(self, value):
        self._setNumber(0, value)

    def getIsVisible(self):
        return self._getBool(1)

    def setIsVisible(self, value):
        self._setBool(1, value)

    def _initialize(self):
        super(SuperLootScanning, self)._initialize()
        self._addNumberProperty('timeLeft', 0)
        self._addBoolProperty('isVisible', False)