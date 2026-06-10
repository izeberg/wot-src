from frameworks.wulf import ViewModel

class LeaderboardRewardTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(LeaderboardRewardTooltipModel, self).__init__(properties=properties, commands=commands)

    def getPlace(self):
        return self._getNumber(0)

    def setPlace(self, value):
        self._setNumber(0, value)

    def _initialize(self):
        super(LeaderboardRewardTooltipModel, self)._initialize()
        self._addNumberProperty('place', 0)