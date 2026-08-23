from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel

class JmNodePopoverModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(JmNodePopoverModel, self).__init__(properties=properties, commands=commands)

    def getRewards(self):
        return self._getArray(0)

    def setRewards(self, value):
        self._setArray(0, value)

    @staticmethod
    def getRewardsType():
        return BonusModel

    def getCoinTokenPrice(self):
        return self._getNumber(1)

    def setCoinTokenPrice(self, value):
        self._setNumber(1, value)

    def getUnlockTokenPrice(self):
        return self._getNumber(2)

    def setUnlockTokenPrice(self, value):
        self._setNumber(2, value)

    def getUnlockTokenNodeId(self):
        return self._getString(3)

    def setUnlockTokenNodeId(self, value):
        self._setString(3, value)

    def _initialize(self):
        super(JmNodePopoverModel, self)._initialize()
        self._addArrayProperty('rewards', Array())
        self._addNumberProperty('coinTokenPrice', 0)
        self._addNumberProperty('unlockTokenPrice', 0)
        self._addStringProperty('unlockTokenNodeId', '')