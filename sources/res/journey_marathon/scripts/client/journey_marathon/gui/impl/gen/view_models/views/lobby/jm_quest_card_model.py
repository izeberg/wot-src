from frameworks.wulf import ViewModel

class JmQuestCardModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=8, commands=0):
        super(JmQuestCardModel, self).__init__(properties=properties, commands=commands)

    def getId(self):
        return self._getString(0)

    def setId(self, value):
        self._setString(0, value)

    def getDescription(self):
        return self._getString(1)

    def setDescription(self, value):
        self._setString(1, value)

    def getCurrentProgress(self):
        return self._getNumber(2)

    def setCurrentProgress(self, value):
        self._setNumber(2, value)

    def getTotalProgress(self):
        return self._getNumber(3)

    def setTotalProgress(self, value):
        self._setNumber(3, value)

    def getEarnedProgress(self):
        return self._getNumber(4)

    def setEarnedProgress(self, value):
        self._setNumber(4, value)

    def getReward(self):
        return self._getNumber(5)

    def setReward(self, value):
        self._setNumber(5, value)

    def getIconKey(self):
        return self._getString(6)

    def setIconKey(self, value):
        self._setString(6, value)

    def getIsCompleted(self):
        return self._getBool(7)

    def setIsCompleted(self, value):
        self._setBool(7, value)

    def _initialize(self):
        super(JmQuestCardModel, self)._initialize()
        self._addStringProperty('id', '')
        self._addStringProperty('description', '')
        self._addNumberProperty('currentProgress', 0)
        self._addNumberProperty('totalProgress', 0)
        self._addNumberProperty('earnedProgress', 0)
        self._addNumberProperty('reward', 0)
        self._addStringProperty('iconKey', '')
        self._addBoolProperty('isCompleted', False)