from frameworks.wulf import Array
from frameworks.wulf import ViewModel

class SelectedRewardsTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(SelectedRewardsTooltipModel, self).__init__(properties=properties, commands=commands)

    def getSelectedRewards(self):
        return self._getArray(0)

    def setSelectedRewards(self, value):
        self._setArray(0, value)

    @staticmethod
    def getSelectedRewardsType():
        return unicode

    def _initialize(self):
        super(SelectedRewardsTooltipModel, self)._initialize()
        self._addArrayProperty('selectedRewards', Array())