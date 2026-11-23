from frameworks.wulf import Array, ViewModel
from advent_calendar.gui.impl.gen.view_models.views.lobby.progression_reward_item_view_model import ProgressionRewardItemViewModel

class ProgressionRewardsViewModel(ViewModel):
    __slots__ = ('onProgressionRewardCompleted', )

    def __init__(self, properties=2, commands=1):
        super(ProgressionRewardsViewModel, self).__init__(properties=properties, commands=commands)

    def getIsCompleted(self):
        return self._getBool(0)

    def setIsCompleted(self, value):
        self._setBool(0, value)

    def getRewards(self):
        return self._getArray(1)

    def setRewards(self, value):
        self._setArray(1, value)

    @staticmethod
    def getRewardsType():
        return ProgressionRewardItemViewModel

    def _initialize(self):
        super(ProgressionRewardsViewModel, self)._initialize()
        self._addBoolProperty('isCompleted', False)
        self._addArrayProperty('rewards', Array())
        self.onProgressionRewardCompleted = self._addCommand('onProgressionRewardCompleted')