from frameworks.wulf import ViewModel

class PriceModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(PriceModel, self).__init__(properties=properties, commands=commands)

    def getCurrency(self):
        return self._getString(0)

    def setCurrency(self, value):
        self._setString(0, value)

    def getAmount(self):
        return self._getNumber(1)

    def setAmount(self, value):
        self._setNumber(1, value)

    def _initialize(self):
        super(PriceModel, self)._initialize()
        self._addStringProperty('currency', '')
        self._addNumberProperty('amount', 0)