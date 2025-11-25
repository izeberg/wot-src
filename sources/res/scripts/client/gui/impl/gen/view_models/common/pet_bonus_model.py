from frameworks.wulf import ViewModel

class PetBonusModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(PetBonusModel, self).__init__(properties=properties, commands=commands)

    def getName(self):
        return self._getString(0)

    def setName(self, value):
        self._setString(0, value)

    def getValue(self):
        return self._getNumber(1)

    def setValue(self, value):
        self._setNumber(1, value)

    def _initialize(self):
        super(PetBonusModel, self)._initialize()
        self._addStringProperty('name', '')
        self._addNumberProperty('value', 0)