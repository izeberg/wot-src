from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.new_year.views.challenge.progress_reward_item_model import ProgressRewardItemModel

class NewYearChallengeProgressModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(NewYearChallengeProgressModel, self).__init__(properties=properties, commands=commands)

    def getRewardLevel(self):
        return self._getNumber(0)

    def setRewardLevel(self, value):
        self._setNumber(0, value)

    def getRewards(self):
        return self._getArray(1)

    def setRewards(self, value):
        self._setArray(1, value)

    @staticmethod
    def getRewardsType():
        return ProgressRewardItemModel

    def _initialize(self):
        super(NewYearChallengeProgressModel, self)._initialize()
        self._addNumberProperty('rewardLevel', 0)
        self._addArrayProperty('rewards', Array())