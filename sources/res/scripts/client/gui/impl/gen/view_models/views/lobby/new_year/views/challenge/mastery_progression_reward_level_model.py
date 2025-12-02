from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel

class MasteryProgressionRewardLevelModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(MasteryProgressionRewardLevelModel, self).__init__(properties=properties, commands=commands)

    def getProgress(self):
        return self._getNumber(0)

    def setProgress(self, value):
        self._setNumber(0, value)

    def getRewards(self):
        return self._getArray(1)

    def setRewards(self, value):
        self._setArray(1, value)

    @staticmethod
    def getRewardsType():
        return BonusModel

    def _initialize(self):
        super(MasteryProgressionRewardLevelModel, self)._initialize()
        self._addNumberProperty('progress', 0)
        self._addArrayProperty('rewards', Array())