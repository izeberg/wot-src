from frameworks.wulf import ViewModel

class RewardsHeaderTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(RewardsHeaderTooltipModel, self).__init__(properties=properties, commands=commands)

    def getIsLevelAchieved(self):
        return self._getBoolean(0)

    def setIsLevelAchieved(self, value):
        self._setBoolean(0, value)

    def getIsCurrentLevel(self):
        return self._getBoolean(1)

    def setIsCurrentLevel(self, value):
        self._setBoolean(1, value)

    def _initialize(self):
        super(RewardsHeaderTooltipModel, self)._initialize()
        self._addBooleanProperty('isLevelAchieved')
        self._addBooleanProperty('isCurrentLevel')