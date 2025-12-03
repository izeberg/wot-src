from enum import Enum
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.new_year.views.challenge.mastery_progression_reward_level_model import MasteryProgressionRewardLevelModel

class RewardState(Enum):
    AVAILABLE = 'available'
    OBTAINED = 'obtained'
    LOCKED = 'locked'


class HoMasteryProgressionModel(ViewModel):
    __slots__ = ('onGoToDetails', )

    def __init__(self, properties=3, commands=1):
        super(HoMasteryProgressionModel, self).__init__(properties=properties, commands=commands)

    def getCurrentProgress(self):
        return self._getNumber(0)

    def setCurrentProgress(self, value):
        self._setNumber(0, value)

    def getRewardState(self):
        return RewardState(self._getString(1))

    def setRewardState(self, value):
        self._setString(1, value.value)

    def getRewardsLevels(self):
        return self._getArray(2)

    def setRewardsLevels(self, value):
        self._setArray(2, value)

    @staticmethod
    def getRewardsLevelsType():
        return MasteryProgressionRewardLevelModel

    def _initialize(self):
        super(HoMasteryProgressionModel, self)._initialize()
        self._addNumberProperty('currentProgress', 0)
        self._addStringProperty('rewardState')
        self._addArrayProperty('rewardsLevels', Array())
        self.onGoToDetails = self._addCommand('onGoToDetails')