from frameworks.wulf import ViewModel

class WelcomeScreenViewModel(ViewModel):
    __slots__ = ('onVideoPlay', 'onClose', 'onViewLoaded')

    def __init__(self, properties=0, commands=3):
        super(WelcomeScreenViewModel, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(WelcomeScreenViewModel, self)._initialize()
        self.onVideoPlay = self._addCommand('onVideoPlay')
        self.onClose = self._addCommand('onClose')
        self.onViewLoaded = self._addCommand('onViewLoaded')