from frameworks.wulf import ViewModel

class CustomizationResourceExchangeItemModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=13, commands=0):
        super(CustomizationResourceExchangeItemModel, self).__init__(properties=properties, commands=commands)

    def getIntCD(self):
        return self._getNumber(0)

    def setIntCD(self, value):
        self._setNumber(0, value)

    def getVehicleCD(self):
        return self._getNumber(1)

    def setVehicleCD(self, value):
        self._setNumber(1, value)

    def getName(self):
        return self._getString(2)

    def setName(self, value):
        self._setString(2, value)

    def getIcon(self):
        return self._getString(3)

    def setIcon(self, value):
        self._setString(3, value)

    def getVehicleName(self):
        return self._getString(4)

    def setVehicleName(self, value):
        self._setString(4, value)

    def getTooltip(self):
        return self._getString(5)

    def setTooltip(self, value):
        self._setString(5, value)

    def getInventoryCount(self):
        return self._getNumber(6)

    def setInventoryCount(self, value):
        self._setNumber(6, value)

    def getInstalledCount(self):
        return self._getNumber(7)

    def setInstalledCount(self, value):
        self._setNumber(7, value)

    def getAvailableCount(self):
        return self._getNumber(8)

    def setAvailableCount(self, value):
        self._setNumber(8, value)

    def getSelectedCount(self):
        return self._getNumber(9)

    def setSelectedCount(self, value):
        self._setNumber(9, value)

    def getIsWide(self):
        return self._getBool(10)

    def setIsWide(self, value):
        self._setBool(10, value)

    def getExchangePrice(self):
        return self._getNumber(11)

    def setExchangePrice(self, value):
        self._setNumber(11, value)

    def getIsFilled(self):
        return self._getBool(12)

    def setIsFilled(self, value):
        self._setBool(12, value)

    def _initialize(self):
        super(CustomizationResourceExchangeItemModel, self)._initialize()
        self._addNumberProperty('intCD', 0)
        self._addNumberProperty('vehicleCD', 0)
        self._addStringProperty('name', '')
        self._addStringProperty('icon', '')
        self._addStringProperty('vehicleName', '')
        self._addStringProperty('tooltip', '')
        self._addNumberProperty('inventoryCount', 0)
        self._addNumberProperty('installedCount', 0)
        self._addNumberProperty('availableCount', 0)
        self._addNumberProperty('selectedCount', 0)
        self._addBoolProperty('isWide', False)
        self._addNumberProperty('exchangePrice', 0)
        self._addBoolProperty('isFilled', False)