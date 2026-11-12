from frameworks.wulf import ViewModel

class NyTabsModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(NyTabsModel, self).__init__(properties=properties, commands=commands)

    def getTop(self):
        return self._getNumber(0)

    def setTop(self, value):
        self._setNumber(0, value)

    def getIsAvailable(self):
        return self._getBool(1)

    def setIsAvailable(self, value):
        self._setBool(1, value)

    def _initialize(self):
        super(NyTabsModel, self)._initialize()
        self._addNumberProperty('top', 0)
        self._addBoolProperty('isAvailable', True)