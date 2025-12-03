from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.new_year.views.gift_machine.reward_group_model import RewardGroupModel

class NyGiftMachineLootListViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(NyGiftMachineLootListViewModel, self).__init__(properties=properties, commands=commands)

    def getRewardGroups(self):
        return self._getArray(0)

    def setRewardGroups(self, value):
        self._setArray(0, value)

    @staticmethod
    def getRewardGroupsType():
        return RewardGroupModel

    def _initialize(self):
        super(NyGiftMachineLootListViewModel, self)._initialize()
        self._addArrayProperty('rewardGroups', Array())