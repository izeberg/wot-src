from frameworks.wulf import ViewModel

class PurchaseDialogModel(ViewModel):
    __slots__ = ('onAccept', 'onCancel')

    def __init__(self, properties=7, commands=2):
        super(PurchaseDialogModel, self).__init__(properties=properties, commands=commands)

    def getDayId(self):
        return self._getNumber(0)

    def setDayId(self, value):
        self._setNumber(0, value)

    def getIsWalletAvailable(self):
        return self._getBool(1)

    def setIsWalletAvailable(self, value):
        self._setBool(1, value)

    def getCurrentResource(self):
        return self._getString(2)

    def setCurrentResource(self, value):
        self._setString(2, value)

    def getBalanceCurrencyValue(self):
        return self._getNumber(3)

    def setBalanceCurrencyValue(self, value):
        self._setNumber(3, value)

    def getPrice(self):
        return self._getNumber(4)

    def setPrice(self, value):
        self._setNumber(4, value)

    def getNotEnoughResource(self):
        return self._getBool(5)

    def setNotEnoughResource(self, value):
        self._setBool(5, value)

    def getCurrencyTooltipId(self):
        return self._getString(6)

    def setCurrencyTooltipId(self, value):
        self._setString(6, value)

    def _initialize(self):
        super(PurchaseDialogModel, self)._initialize()
        self._addNumberProperty('dayId', 0)
        self._addBoolProperty('isWalletAvailable', True)
        self._addStringProperty('currentResource', '')
        self._addNumberProperty('balanceCurrencyValue', 0)
        self._addNumberProperty('price', 0)
        self._addBoolProperty('notEnoughResource', False)
        self._addStringProperty('currencyTooltipId', '')
        self.onAccept = self._addCommand('onAccept')
        self.onCancel = self._addCommand('onCancel')