from frameworks.wulf import ViewModel

class KeysModel(ViewModel):
    __slots__ = ('onClick', )

    def __init__(self, properties=2, commands=1):
        super(KeysModel, self).__init__(properties=properties, commands=commands)

    def getAmount(self):
        return self._getNumber(0)

    def setAmount(self, value):
        self._setNumber(0, value)

    def getIsDisabled(self):
        return self._getBool(1)

    def setIsDisabled(self, value):
        self._setBool(1, value)

    def _initialize(self):
        super(KeysModel, self)._initialize()
        self._addNumberProperty('amount', 0)
        self._addBoolProperty('isDisabled', False)
        self.onClick = self._addCommand('onClick')