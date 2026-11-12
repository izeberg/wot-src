from frameworks.wulf import ViewModel

class NyDailyQuestsInfoViewModel(ViewModel):
    __slots__ = ('onClose', )

    def __init__(self, properties=0, commands=1):
        super(NyDailyQuestsInfoViewModel, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(NyDailyQuestsInfoViewModel, self)._initialize()
        self.onClose = self._addCommand('onClose')