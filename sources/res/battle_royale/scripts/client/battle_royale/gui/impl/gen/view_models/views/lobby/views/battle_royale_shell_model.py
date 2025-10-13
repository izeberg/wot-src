from frameworks.wulf import ViewModel

class BattleRoyaleShellModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(BattleRoyaleShellModel, self).__init__(properties=properties, commands=commands)

    def getIconName(self):
        return self._getString(0)

    def setIconName(self, value):
        self._setString(0, value)

    def getIntCD(self):
        return self._getNumber(1)

    def setIntCD(self, value):
        self._setNumber(1, value)

    def getQuantity(self):
        return self._getNumber(2)

    def setQuantity(self, value):
        self._setNumber(2, value)

    def _initialize(self):
        super(BattleRoyaleShellModel, self)._initialize()
        self._addStringProperty('iconName', '')
        self._addNumberProperty('intCD', 0)
        self._addNumberProperty('quantity', 0)