from frameworks.wulf import ViewModel

class GrinchCapturablePointMarkerModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(GrinchCapturablePointMarkerModel, self).__init__(properties=properties, commands=commands)

    def getPosx(self):
        return self._getReal(0)

    def setPosx(self, value):
        self._setReal(0, value)

    def getPosy(self):
        return self._getReal(1)

    def setPosy(self, value):
        self._setReal(1, value)

    def getIsVisible(self):
        return self._getBool(2)

    def setIsVisible(self, value):
        self._setBool(2, value)

    def _initialize(self):
        super(GrinchCapturablePointMarkerModel, self)._initialize()
        self._addRealProperty('posx', 0.0)
        self._addRealProperty('posy', 0.0)
        self._addBoolProperty('isVisible', False)