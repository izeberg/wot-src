from frameworks.wulf import ViewModel

class FortRushWelcomeScreenViewModel(ViewModel):
    __slots__ = ('onVideoPlay', 'onClose', 'onViewLoaded')

    def __init__(self, properties=0, commands=3):
        super(FortRushWelcomeScreenViewModel, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(FortRushWelcomeScreenViewModel, self)._initialize()
        self.onVideoPlay = self._addCommand('onVideoPlay')
        self.onClose = self._addCommand('onClose')
        self.onViewLoaded = self._addCommand('onViewLoaded')