from frameworks.wulf import Array
from frameworks.wulf import ViewModel

class WeeklyRewardScreenModel(ViewModel):
    __slots__ = ('onClose', )

    def __init__(self, properties=2, commands=1):
        super(WeeklyRewardScreenModel, self).__init__(properties=properties, commands=commands)

    def getMainRewards(self):
        return self._getArray(0)

    def setMainRewards(self, value):
        self._setArray(0, value)

    def getRewards(self):
        return self._getArray(1)

    def setRewards(self, value):
        self._setArray(1, value)

    def _initialize(self):
        super(WeeklyRewardScreenModel, self)._initialize()
        self._addArrayProperty('mainRewards', Array())
        self._addArrayProperty('rewards', Array())
        self.onClose = self._addCommand('onClose')