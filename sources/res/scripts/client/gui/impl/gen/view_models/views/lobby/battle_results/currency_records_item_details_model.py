from frameworks.wulf import ViewModel

class CurrencyRecordsItemDetailsModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(CurrencyRecordsItemDetailsModel, self).__init__(properties=properties, commands=commands)

    def getItemName(self):
        return self._getString(0)

    def setItemName(self, value):
        self._setString(0, value)

    def getItemValue(self):
        return self._getString(1)

    def setItemValue(self, value):
        self._setString(1, value)

    def _initialize(self):
        super(CurrencyRecordsItemDetailsModel, self)._initialize()
        self._addStringProperty('itemName', '')
        self._addStringProperty('itemValue', '')