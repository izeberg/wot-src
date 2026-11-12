from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel

class CustomizationResourceRewardViewModel(ViewModel):
    __slots__ = ('onClose', )
    MAX_MAIN_REWARDS = 3
    MAX_REWARDS = 10

    def __init__(self, properties=2, commands=1):
        super(CustomizationResourceRewardViewModel, self).__init__(properties=properties, commands=commands)

    def getMainRewards(self):
        return self._getArray(0)

    def setMainRewards(self, value):
        self._setArray(0, value)

    @staticmethod
    def getMainRewardsType():
        return BonusModel

    def getRewards(self):
        return self._getArray(1)

    def setRewards(self, value):
        self._setArray(1, value)

    @staticmethod
    def getRewardsType():
        return BonusModel

    def _initialize(self):
        super(CustomizationResourceRewardViewModel, self)._initialize()
        self._addArrayProperty('mainRewards', Array())
        self._addArrayProperty('rewards', Array())
        self.onClose = self._addCommand('onClose')