from frameworks.wulf import ViewModel

class DefaultModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(DefaultModel, self).__init__(properties=properties, commands=commands)

    def getOldStyle(self):
        return self._getBool(0)

    def setOldStyle(self, value):
        self._setBool(0, value)

    def getIsHOPanelVisible(self):
        return self._getBool(1)

    def setIsHOPanelVisible(self, value):
        self._setBool(1, value)

    def getIsHOEventEnabled(self):
        return self._getBool(2)

    def setIsHOEventEnabled(self, value):
        self._setBool(2, value)

    def _initialize(self):
        super(DefaultModel, self)._initialize()
        self._addBoolProperty('oldStyle', False)
        self._addBoolProperty('isHOPanelVisible', False)
        self._addBoolProperty('isHOEventEnabled', False)