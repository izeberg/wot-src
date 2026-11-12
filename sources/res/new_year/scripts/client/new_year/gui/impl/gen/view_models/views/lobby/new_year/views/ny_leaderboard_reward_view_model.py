from frameworks.wulf import ViewModel
from gui.impl.wrappers.user_list_model import UserListModel
from new_year.gui.impl.gen.view_models.views.lobby.new_year.components.reward_item_model import RewardItemModel

class NyLeaderboardRewardViewModel(ViewModel):
    __slots__ = ('onClose', )

    def __init__(self, properties=6, commands=1):
        super(NyLeaderboardRewardViewModel, self).__init__(properties=properties, commands=commands)

    @property
    def rewards(self):
        return self._getViewModel(0)

    @staticmethod
    def getRewardsType():
        return RewardItemModel

    def getIsPreorder(self):
        return self._getBool(1)

    def setIsPreorder(self, value):
        self._setBool(1, value)

    def getIsFinal(self):
        return self._getBool(2)

    def setIsFinal(self, value):
        self._setBool(2, value)

    def getPosition(self):
        return self._getNumber(3)

    def setPosition(self, value):
        self._setNumber(3, value)

    def getTop(self):
        return self._getNumber(4)

    def setTop(self, value):
        self._setNumber(4, value)

    def getStage(self):
        return self._getNumber(5)

    def setStage(self, value):
        self._setNumber(5, value)

    def _initialize(self):
        super(NyLeaderboardRewardViewModel, self)._initialize()
        self._addViewModelProperty('rewards', UserListModel())
        self._addBoolProperty('isPreorder', False)
        self._addBoolProperty('isFinal', False)
        self._addNumberProperty('position', 0)
        self._addNumberProperty('top', 0)
        self._addNumberProperty('stage', 0)
        self.onClose = self._addCommand('onClose')