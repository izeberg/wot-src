from enum import Enum
from gui.impl.gen.view_models.views.lobby.cn_loot_boxes.reward_model import RewardModel

class VehicleType(Enum):
    HEAVY = 'heavyTank'
    MEDIUM = 'mediumTank'
    LIGHT = 'lightTank'
    SPG = 'SPG'
    ATSPG = 'AT-SPG'


class VehicleModel(RewardModel):
    __slots__ = ()

    def __init__(self, properties=13, commands=0):
        super(VehicleModel, self).__init__(properties=properties, commands=commands)

    def getName(self):
        return self._getString(10)

    def setName(self, value):
        self._setString(10, value)

    def getType(self):
        return VehicleType(self._getString(11))

    def setType(self, value):
        self._setString(11, value.value)

    def getLevel(self):
        return self._getNumber(12)

    def setLevel(self, value):
        self._setNumber(12, value)

    def _initialize(self):
        super(VehicleModel, self)._initialize()
        self._addStringProperty('name', '')
        self._addStringProperty('type')
        self._addNumberProperty('level', 0)