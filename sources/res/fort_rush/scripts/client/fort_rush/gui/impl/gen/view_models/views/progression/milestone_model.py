from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.item_bonus_model import ItemBonusModel

class MilestoneModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(MilestoneModel, self).__init__(properties=properties, commands=commands)

    def getEventPoints(self):
        return self._getNumber(0)

    def setEventPoints(self, value):
        self._setNumber(0, value)

    def getRewards(self):
        return self._getArray(1)

    def setRewards(self, value):
        self._setArray(1, value)

    @staticmethod
    def getRewardsType():
        return ItemBonusModel

    def _initialize(self):
        super(MilestoneModel, self)._initialize()
        self._addNumberProperty('eventPoints', 0)
        self._addArrayProperty('rewards', Array())