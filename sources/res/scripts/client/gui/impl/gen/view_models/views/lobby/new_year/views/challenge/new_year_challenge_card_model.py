from enum import IntEnum
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.new_year.views.challenge.challenge_mission_model import ChallengeMissionModel
from gui.impl.gen.view_models.views.lobby.new_year.views.challenge.challenge_reward_item_model import ChallengeRewardItemModel

class CardState(IntEnum):
    ACTIVE = 0
    INPROGRESS = 1
    COMPLETED = 2
    JUSTCOMPLETED = 3


class NewYearChallengeCardModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(NewYearChallengeCardModel, self).__init__(properties=properties, commands=commands)

    def getState(self):
        return CardState(self._getNumber(0))

    def setState(self, value):
        self._setNumber(0, value.value)

    def getIsVisited(self):
        return self._getBool(1)

    def setIsVisited(self, value):
        self._setBool(1, value)

    def getToken(self):
        return self._getString(2)

    def setToken(self, value):
        self._setString(2, value)

    def getMissions(self):
        return self._getArray(3)

    def setMissions(self, value):
        self._setArray(3, value)

    @staticmethod
    def getMissionsType():
        return ChallengeMissionModel

    def getSingleMissionRewards(self):
        return self._getArray(4)

    def setSingleMissionRewards(self, value):
        self._setArray(4, value)

    @staticmethod
    def getSingleMissionRewardsType():
        return ChallengeRewardItemModel

    def getFullMissionRewards(self):
        return self._getArray(5)

    def setFullMissionRewards(self, value):
        self._setArray(5, value)

    @staticmethod
    def getFullMissionRewardsType():
        return ChallengeRewardItemModel

    def _initialize(self):
        super(NewYearChallengeCardModel, self)._initialize()
        self._addNumberProperty('state')
        self._addBoolProperty('isVisited', False)
        self._addStringProperty('token', '')
        self._addArrayProperty('missions', Array())
        self._addArrayProperty('singleMissionRewards', Array())
        self._addArrayProperty('fullMissionRewards', Array())