from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.new_year.views.challenge.challenge_reward_item_model import ChallengeRewardItemModel

class NewYearChallengeUpcomingCardModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(NewYearChallengeUpcomingCardModel, self).__init__(properties=properties, commands=commands)

    def getSingleMissionRewards(self):
        return self._getArray(0)

    def setSingleMissionRewards(self, value):
        self._setArray(0, value)

    @staticmethod
    def getSingleMissionRewardsType():
        return ChallengeRewardItemModel

    def getFullMissionRewards(self):
        return self._getArray(1)

    def setFullMissionRewards(self, value):
        self._setArray(1, value)

    @staticmethod
    def getFullMissionRewardsType():
        return ChallengeRewardItemModel

    def _initialize(self):
        super(NewYearChallengeUpcomingCardModel, self)._initialize()
        self._addArrayProperty('singleMissionRewards', Array())
        self._addArrayProperty('fullMissionRewards', Array())