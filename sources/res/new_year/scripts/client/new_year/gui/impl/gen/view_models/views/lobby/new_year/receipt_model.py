from enum import Enum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from new_year.gui.impl.gen.view_models.views.lobby.new_year.components.reward_item_model import RewardItemModel
from new_year.gui.impl.gen.view_models.views.lobby.new_year.raid_item_model import RaidItemModel

class ReceiptState(Enum):
    AVAILABLE = 'available'
    NOT_ENOUGH_RESOURCES = 'not_enough_resources'
    LIMIT_REACHED = 'limit_reached'
    TAMAGOTCHI_STATS = 'tamagotchi_stats'
    TAMAGOTCHI_RAID = 'tamagotchi_raid'


class ReceiptModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=9, commands=0):
        super(ReceiptModel, self).__init__(properties=properties, commands=commands)

    def getReceiptComponents(self):
        return self._getArray(0)

    def setReceiptComponents(self, value):
        self._setArray(0, value)

    @staticmethod
    def getReceiptComponentsType():
        return RaidItemModel

    def getReceiptRewards(self):
        return self._getArray(1)

    def setReceiptRewards(self, value):
        self._setArray(1, value)

    @staticmethod
    def getReceiptRewardsType():
        return RewardItemModel

    def getLimit(self):
        return self._getNumber(2)

    def setLimit(self, value):
        self._setNumber(2, value)

    def getId(self):
        return self._getNumber(3)

    def setId(self, value):
        self._setNumber(3, value)

    def getUsageCount(self):
        return self._getNumber(4)

    def setUsageCount(self, value):
        self._setNumber(4, value)

    def getState(self):
        return ReceiptState(self._getString(5))

    def setState(self, value):
        self._setString(5, value.value)

    def getStartTime(self):
        return self._getNumber(6)

    def setStartTime(self, value):
        self._setNumber(6, value)

    def getIsDisabled(self):
        return self._getBool(7)

    def setIsDisabled(self, value):
        self._setBool(7, value)

    def getWeight(self):
        return self._getReal(8)

    def setWeight(self, value):
        self._setReal(8, value)

    def _initialize(self):
        super(ReceiptModel, self)._initialize()
        self._addArrayProperty('receiptComponents', Array())
        self._addArrayProperty('receiptRewards', Array())
        self._addNumberProperty('limit', 0)
        self._addNumberProperty('id', 0)
        self._addNumberProperty('usageCount', 0)
        self._addStringProperty('state', ReceiptState.AVAILABLE.value)
        self._addNumberProperty('startTime', -1)
        self._addBoolProperty('isDisabled', False)
        self._addRealProperty('weight', 0.0)