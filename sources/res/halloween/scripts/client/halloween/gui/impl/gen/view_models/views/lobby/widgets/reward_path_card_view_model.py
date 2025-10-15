from frameworks.wulf import ViewModel

class RewardPathCardViewModel(ViewModel):
    __slots__ = ('onClick', )

    def __init__(self, properties=4, commands=1):
        super(RewardPathCardViewModel, self).__init__(properties=properties, commands=commands)

    def getCurrentProgress(self):
        return self._getNumber(0)

    def setCurrentProgress(self, value):
        self._setNumber(0, value)

    def getMaxProgress(self):
        return self._getNumber(1)

    def setMaxProgress(self, value):
        self._setNumber(1, value)

    def getIsCompleted(self):
        return self._getBool(2)

    def setIsCompleted(self, value):
        self._setBool(2, value)

    def getCertificates(self):
        return self._getNumber(3)

    def setCertificates(self, value):
        self._setNumber(3, value)

    def _initialize(self):
        super(RewardPathCardViewModel, self)._initialize()
        self._addNumberProperty('currentProgress', 0)
        self._addNumberProperty('maxProgress', 0)
        self._addBoolProperty('isCompleted', False)
        self._addNumberProperty('certificates', 0)
        self.onClick = self._addCommand('onClick')