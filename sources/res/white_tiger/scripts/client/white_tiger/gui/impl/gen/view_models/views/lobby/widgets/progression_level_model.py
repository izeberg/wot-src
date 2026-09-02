from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel

class ProgressionLevelModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(ProgressionLevelModel, self).__init__(properties=properties, commands=commands)

    def getRewards(self):
        return self._getArray(0)

    def setRewards(self, value):
        self._setArray(0, value)

    @staticmethod
    def getRewardsType():
        return BonusModel

    def _initialize(self):
        super(ProgressionLevelModel, self)._initialize()
        self._addArrayProperty('rewards', Array())