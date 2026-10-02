from frameworks.wulf import ViewModel

class SessionProgressRewardsTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(SessionProgressRewardsTooltipModel, self).__init__(properties=properties, commands=commands)

    def getIsCompleted(self):
        return self._getBool(0)

    def setIsCompleted(self, value):
        self._setBool(0, value)

    def getIsProgressionCompleted(self):
        return self._getBool(1)

    def setIsProgressionCompleted(self, value):
        self._setBool(1, value)

    def _initialize(self):
        super(SessionProgressRewardsTooltipModel, self)._initialize()
        self._addBoolProperty('isCompleted', False)
        self._addBoolProperty('isProgressionCompleted', False)