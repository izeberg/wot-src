from frameworks.wulf import ViewModel

class SummerSaleIntroPageViewModel(ViewModel):
    __slots__ = ('onGoToFeature', 'onClose')

    def __init__(self, properties=0, commands=2):
        super(SummerSaleIntroPageViewModel, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(SummerSaleIntroPageViewModel, self)._initialize()
        self.onGoToFeature = self._addCommand('onGoToFeature')
        self.onClose = self._addCommand('onClose')