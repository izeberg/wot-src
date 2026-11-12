from frameworks.wulf import ViewModel
from gui.impl.wrappers.user_list_model import UserListModel
from new_year.gui.impl.gen.view_models.views.lobby.new_year.components.reward_item_model import RewardItemModel

class NyPersonalinfoModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=9, commands=0):
        super(NyPersonalinfoModel, self).__init__(properties=properties, commands=commands)

    @property
    def rewards(self):
        return self._getViewModel(0)

    @staticmethod
    def getRewardsType():
        return RewardItemModel

    def getScore(self):
        return self._getNumber(1)

    def setScore(self, value):
        self._setNumber(1, value)

    def getTop(self):
        return self._getNumber(2)

    def setTop(self, value):
        self._setNumber(2, value)

    def getPosition(self):
        return self._getNumber(3)

    def setPosition(self, value):
        self._setNumber(3, value)

    def getNextTopPoints(self):
        return self._getNumber(4)

    def setNextTopPoints(self, value):
        self._setNumber(4, value)

    def getOpponentPoints(self):
        return self._getNumber(5)

    def setOpponentPoints(self, value):
        self._setNumber(5, value)

    def getFromTimestamp(self):
        return self._getNumber(6)

    def setFromTimestamp(self, value):
        self._setNumber(6, value)

    def getToTimestamp(self):
        return self._getNumber(7)

    def setToTimestamp(self, value):
        self._setNumber(7, value)

    def getIsFinal(self):
        return self._getBool(8)

    def setIsFinal(self, value):
        self._setBool(8, value)

    def _initialize(self):
        super(NyPersonalinfoModel, self)._initialize()
        self._addViewModelProperty('rewards', UserListModel())
        self._addNumberProperty('score', 0)
        self._addNumberProperty('top', 0)
        self._addNumberProperty('position', 0)
        self._addNumberProperty('nextTopPoints', 0)
        self._addNumberProperty('opponentPoints', 0)
        self._addNumberProperty('fromTimestamp', 0)
        self._addNumberProperty('toTimestamp', 0)
        self._addBoolProperty('isFinal', False)