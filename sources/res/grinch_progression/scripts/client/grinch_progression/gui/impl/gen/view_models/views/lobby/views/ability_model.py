from grinch_progression.gui.impl.gen.view_models.views.lobby.views.enums import VehicleRole
from frameworks.wulf import ViewModel

class AbilityModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=9, commands=0):
        super(AbilityModel, self).__init__(properties=properties, commands=commands)

    def getResourceKey(self):
        return self._getString(0)

    def setResourceKey(self, value):
        self._setString(0, value)

    def getKeyString(self):
        return self._getString(1)

    def setKeyString(self, value):
        self._setString(1, value)

    def getIntCD(self):
        return self._getNumber(2)

    def setIntCD(self, value):
        self._setNumber(2, value)

    def getDescription(self):
        return self._getString(3)

    def setDescription(self, value):
        self._setString(3, value)

    def getRadius(self):
        return self._getNumber(4)

    def setRadius(self, value):
        self._setNumber(4, value)

    def getDuration(self):
        return self._getNumber(5)

    def setDuration(self, value):
        self._setNumber(5, value)

    def getDebuffDuration(self):
        return self._getNumber(6)

    def setDebuffDuration(self, value):
        self._setNumber(6, value)

    def getRole(self):
        return VehicleRole(self._getString(7))

    def setRole(self, value):
        self._setString(7, value.value)

    def getPosition(self):
        return self._getNumber(8)

    def setPosition(self, value):
        self._setNumber(8, value)

    def _initialize(self):
        super(AbilityModel, self)._initialize()
        self._addStringProperty('resourceKey', '')
        self._addStringProperty('keyString', '')
        self._addNumberProperty('intCD', 0)
        self._addStringProperty('description', '')
        self._addNumberProperty('radius', 0)
        self._addNumberProperty('duration', 0)
        self._addNumberProperty('debuffDuration', 0)
        self._addStringProperty('role', VehicleRole.CARRIER.value)
        self._addNumberProperty('position', 0)