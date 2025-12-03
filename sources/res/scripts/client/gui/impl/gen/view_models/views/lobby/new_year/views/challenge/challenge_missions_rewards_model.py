from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.new_year.views.challenge.challenge_reward_item_model import ChallengeRewardItemModel

class ChallengeMissionsRewardsModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(ChallengeMissionsRewardsModel, self).__init__(properties=properties, commands=commands)

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
        return ChallengeRewardItemModel

    def _initialize(self):
        super(ChallengeMissionsRewardsModel, self)._initialize()
        self._addBoolProperty('isCompleted', False)
        self._addArrayProperty('rewards', Array())