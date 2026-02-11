from frameworks.wulf import ViewModel

class LunarPossessionTopScorePanelModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(LunarPossessionTopScorePanelModel, self).__init__(properties=properties, commands=commands)

    def getCurrentPoints(self):
        return self._getNumber(0)

    def setCurrentPoints(self, value):
        self._setNumber(0, value)

    def getEnemyPoints(self):
        return self._getNumber(1)

    def setEnemyPoints(self, value):
        self._setNumber(1, value)

    def getMaxPoints(self):
        return self._getNumber(2)

    def setMaxPoints(self, value):
        self._setNumber(2, value)

    def getIsColorblindMode(self):
        return self._getBool(3)

    def setIsColorblindMode(self, value):
        self._setBool(3, value)

    def getIsAllyTeamSpiritCarrier(self):
        return self._getBool(4)

    def setIsAllyTeamSpiritCarrier(self, value):
        self._setBool(4, value)

    def _initialize(self):
        super(LunarPossessionTopScorePanelModel, self)._initialize()
        self._addNumberProperty('currentPoints', 0)
        self._addNumberProperty('enemyPoints', 0)
        self._addNumberProperty('maxPoints', 0)
        self._addBoolProperty('isColorblindMode', False)
        self._addBoolProperty('isAllyTeamSpiritCarrier', False)