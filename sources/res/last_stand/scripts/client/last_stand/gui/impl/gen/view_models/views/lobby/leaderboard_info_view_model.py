from frameworks.wulf import ViewModel

class LeaderboardInfoViewModel(ViewModel):
    __slots__ = ('onClose', )

    def __init__(self, properties=0, commands=1):
        super(LeaderboardInfoViewModel, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(LeaderboardInfoViewModel, self)._initialize()
        self.onClose = self._addCommand('onClose')