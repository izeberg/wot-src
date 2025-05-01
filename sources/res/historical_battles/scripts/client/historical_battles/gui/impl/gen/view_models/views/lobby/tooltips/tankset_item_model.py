from frameworks.wulf import ViewModel

class TanksetItemModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(TanksetItemModel, self).__init__(properties=properties, commands=commands)

    def getName(self):
        return self._getString(0)

    def setName(self, value):
        self._setString(0, value)

    def getIcon(self):
        return self._getString(1)

    def setIcon(self, value):
        self._setString(1, value)

    def getVehicleType(self):
        return self._getString(2)

    def setVehicleType(self, value):
        self._setString(2, value)

    def _initialize(self):
        super(TanksetItemModel, self)._initialize()
        self._addStringProperty('name', '')
        self._addStringProperty('icon', '')
        self._addStringProperty('vehicleType', '')