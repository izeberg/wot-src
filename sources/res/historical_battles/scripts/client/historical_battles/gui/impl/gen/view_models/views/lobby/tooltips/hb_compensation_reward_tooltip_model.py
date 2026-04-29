from frameworks.wulf import ViewModel

class HbCompensationRewardTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(HbCompensationRewardTooltipModel, self).__init__(properties=properties, commands=commands)

    def getVehicleLvl(self):
        return self._getNumber(0)

    def setVehicleLvl(self, value):
        self._setNumber(0, value)

    def getVehicleName(self):
        return self._getString(1)

    def setVehicleName(self, value):
        self._setString(1, value)

    def getCurrencyName(self):
        return self._getString(2)

    def setCurrencyName(self, value):
        self._setString(2, value)

    def getCurrencyAmount(self):
        return self._getNumber(3)

    def setCurrencyAmount(self, value):
        self._setNumber(3, value)

    def _initialize(self):
        super(HbCompensationRewardTooltipModel, self)._initialize()
        self._addNumberProperty('vehicleLvl', 0)
        self._addStringProperty('vehicleName', '')
        self._addStringProperty('currencyName', '')
        self._addNumberProperty('currencyAmount', 0)