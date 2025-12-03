from frameworks.wulf import ViewModel

class PostBattleMissionModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(PostBattleMissionModel, self).__init__(properties=properties, commands=commands)

    def getTitle(self):
        return self._getString(0)

    def setTitle(self, value):
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

    def getPrize(self):
        return self._getNumber(4)

    def setPrize(self, value):
        self._setNumber(4, value)

    def _initialize(self):
        super(PostBattleMissionModel, self)._initialize()
        self._addStringProperty('title', '')
        self._addStringProperty('description', '')
        self._addNumberProperty('currentProgress', 0)
        self._addNumberProperty('totalProgress', 0)
        self._addNumberProperty('prize', 0)