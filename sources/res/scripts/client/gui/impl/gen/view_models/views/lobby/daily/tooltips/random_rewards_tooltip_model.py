from frameworks.wulf import ViewModel

class RandomRewardsTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(RandomRewardsTooltipModel, self).__init__(properties=properties, commands=commands)

    def getRewards(self):
        return self._getString(0)

    def setRewards(self, value):
        self._setString(0, value)

    def _initialize(self):
        super(RandomRewardsTooltipModel, self)._initialize()
        self._addStringProperty('rewards', '')