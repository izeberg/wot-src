from grinch_progression.gui.impl.gen.view_models.views.lobby.views.enums import VehicleRole
from frameworks.wulf import ViewModel

class MissionModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=8, commands=0):
        super(MissionModel, self).__init__(properties=properties, commands=commands)

    def getQuestId(self):
        return self._getString(0)

    def setQuestId(self, value):
        self._setString(0, value)

    def getRole(self):
        return VehicleRole(self._getString(1))

    def setRole(self, value):
        self._setString(1, value.value)

    def getPrecondition(self):
        return self._getString(2)

    def setPrecondition(self, value):
        self._setString(2, value)

    def getDescription(self):
        return self._getString(3)

    def setDescription(self, value):
        self._setString(3, value)

    def getCurrent(self):
        return self._getNumber(4)

    def setCurrent(self, value):
        self._setNumber(4, value)

    def getTarget(self):
        return self._getNumber(5)

    def setTarget(self, value):
        self._setNumber(5, value)

    def getPrize(self):
        return self._getNumber(6)

    def setPrize(self, value):
        self._setNumber(6, value)

    def getIsEventMission(self):
        return self._getBool(7)

    def setIsEventMission(self, value):
        self._setBool(7, value)

    def _initialize(self):
        super(MissionModel, self)._initialize()
        self._addStringProperty('questId', '')
        self._addStringProperty('role', VehicleRole.CARRIER.value)
        self._addStringProperty('precondition', '')
        self._addStringProperty('description', '')
        self._addNumberProperty('current', 0)
        self._addNumberProperty('target', 0)
        self._addNumberProperty('prize', 0)
        self._addBoolProperty('isEventMission', False)