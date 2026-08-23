from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel

class RewardsTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(RewardsTooltipModel, self).__init__(properties=properties, commands=commands)

    def getBonuses(self):
        return self._getArray(0)

    def setBonuses(self, value):
        self._setArray(0, value)

    @staticmethod
    def getBonusesType():
        return BonusModel

    def _initialize(self):
        super(RewardsTooltipModel, self)._initialize()
        self._addArrayProperty('bonuses', Array())