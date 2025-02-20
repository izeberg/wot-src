from frameworks.wulf import ViewModel

class FunRandomMapsMapModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(FunRandomMapsMapModel, self).__init__(properties=properties, commands=commands)

    def getId(self):
        return self._getString(0)

    def setId(self, value):
        self._setString(0, value)

    def getIsEnabled(self):
        return self._getBool(1)

    def setIsEnabled(self, value):
        self._setBool(1, value)

    def getIsSelected(self):
        return self._getBool(2)

    def setIsSelected(self, value):
        self._setBool(2, value)

    def _initialize(self):
        super(FunRandomMapsMapModel, self)._initialize()
        self._addStringProperty('id', '')
        self._addBoolProperty('isEnabled', False)
        self._addBoolProperty('isSelected', False)