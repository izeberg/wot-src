from frameworks.wulf import ViewModel

class CustomizationResourceVideoRewardViewModel(ViewModel):
    __slots__ = ('onClose', )

    def __init__(self, properties=0, commands=1):
        super(CustomizationResourceVideoRewardViewModel, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(CustomizationResourceVideoRewardViewModel, self)._initialize()
        self.onClose = self._addCommand('onClose')