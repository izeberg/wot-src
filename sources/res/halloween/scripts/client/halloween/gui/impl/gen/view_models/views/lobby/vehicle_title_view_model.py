from enum import Enum
from frameworks.wulf import ViewModel

class VehicleTypes(Enum):
    NONE = 'none'
    LIGHTTANK = 'lightTank'
    MEDIUMTANK = 'mediumTank'
    HEAVYTANK = 'heavyTank'
    SPG = 'SPG'
    AT_SPG = 'AT-SPG'


class VehicleTitleViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(VehicleTitleViewModel, self).__init__(properties=properties, commands=commands)

    def getName(self):
        return self._getString(0)

    def setName(self, value):
        self._setString(0, value)

    def getLevel(self):
        return self._getString(1)

    def setLevel(self, value):
        self._setString(1, value)

    def getNation(self):
        return self._getString(2)

    def setNation(self, value):
        self._setString(2, value)

    def getIsPremium(self):
        return self._getBool(3)

    def setIsPremium(self, value):
        self._setBool(3, value)

    def getVehicleType(self):
        return VehicleTypes(self._getString(4))

    def setVehicleType(self, value):
        self._setString(4, value.value)

    def _initialize(self):
        super(VehicleTitleViewModel, self)._initialize()
        self._addStringProperty('name', '')
        self._addStringProperty('level', '')
        self._addStringProperty('nation', '')
        self._addBoolProperty('isPremium', False)
        self._addStringProperty('vehicleType')