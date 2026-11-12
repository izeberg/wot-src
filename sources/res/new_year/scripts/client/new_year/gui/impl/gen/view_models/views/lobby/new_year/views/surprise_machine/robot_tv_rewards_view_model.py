from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel

class RobotTvRewardsViewModel(ViewModel):
    __slots__ = ('onClose', )

    def __init__(self, properties=3, commands=1):
        super(RobotTvRewardsViewModel, self).__init__(properties=properties, commands=commands)

    def getTokensUsed(self):
        return self._getNumber(0)

    def setTokensUsed(self, value):
        self._setNumber(0, value)

    def getHasBlur(self):
        return self._getBool(1)

    def setHasBlur(self, value):
        self._setBool(1, value)

    def getRewards(self):
        return self._getArray(2)

    def setRewards(self, value):
        self._setArray(2, value)

    @staticmethod
    def getRewardsType():
        return BonusModel

    def _initialize(self):
        super(RobotTvRewardsViewModel, self)._initialize()
        self._addNumberProperty('tokensUsed', 10)
        self._addBoolProperty('hasBlur', True)
        self._addArrayProperty('rewards', Array())
        self.onClose = self._addCommand('onClose')