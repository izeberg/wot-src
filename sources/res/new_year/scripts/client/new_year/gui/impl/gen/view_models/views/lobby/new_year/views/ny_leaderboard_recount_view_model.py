from frameworks.wulf import ViewModel

class NyLeaderboardRecountViewModel(ViewModel):
    __slots__ = ('onClose', )

    def __init__(self, properties=1, commands=1):
        super(NyLeaderboardRecountViewModel, self).__init__(properties=properties, commands=commands)

    def getHasBackground(self):
        return self._getBool(0)

    def setHasBackground(self, value):
        self._setBool(0, value)

    def _initialize(self):
        super(NyLeaderboardRecountViewModel, self)._initialize()
        self._addBoolProperty('hasBackground', False)
        self.onClose = self._addCommand('onClose')