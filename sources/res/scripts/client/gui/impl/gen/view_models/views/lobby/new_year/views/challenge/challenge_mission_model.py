from frameworks.wulf import ViewModel

class ChallengeMissionModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(ChallengeMissionModel, self).__init__(properties=properties, commands=commands)

    def getDescription(self):
        return self._getString(0)

    def setDescription(self, value):
        self._setString(0, value)

    def getIcon(self):
        return self._getString(1)

    def setIcon(self, value):
        self._setString(1, value)

    def getIsCumulative(self):
        return self._getBool(2)

    def setIsCumulative(self, value):
        self._setBool(2, value)

    def getCurrentProgress(self):
        return self._getNumber(3)

    def setCurrentProgress(self, value):
        self._setNumber(3, value)

    def getFinalProgress(self):
        return self._getNumber(4)

    def setFinalProgress(self, value):
        self._setNumber(4, value)

    def getGoalValue(self):
        return self._getNumber(5)

    def setGoalValue(self, value):
        self._setNumber(5, value)

    def getIsCompleted(self):
        return self._getBool(6)

    def setIsCompleted(self, value):
        self._setBool(6, value)

    def _initialize(self):
        super(ChallengeMissionModel, self)._initialize()
        self._addStringProperty('description', '')
        self._addStringProperty('icon', '')
        self._addBoolProperty('isCumulative', False)
        self._addNumberProperty('currentProgress', 0)
        self._addNumberProperty('finalProgress', 0)
        self._addNumberProperty('goalValue', 0)
        self._addBoolProperty('isCompleted', False)