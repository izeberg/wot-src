from frameworks.wulf import ViewModel

class CustomizationResourceCurrencyTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(CustomizationResourceCurrencyTooltipViewModel, self).__init__(properties=properties, commands=commands)

    def getBalance(self):
        return self._getNumber(0)

    def setBalance(self, value):
        self._setNumber(0, value)

    def getStartTimestamp(self):
        return self._getNumber(1)

    def setStartTimestamp(self, value):
        self._setNumber(1, value)

    def getEndTimestamp(self):
        return self._getNumber(2)

    def setEndTimestamp(self, value):
        self._setNumber(2, value)

    def _initialize(self):
        super(CustomizationResourceCurrencyTooltipViewModel, self)._initialize()
        self._addNumberProperty('balance', 0)
        self._addNumberProperty('startTimestamp', 0)
        self._addNumberProperty('endTimestamp', 0)