from frameworks.wulf import ViewModel

class AboutViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=0, commands=0):
        super(AboutViewModel, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(AboutViewModel, self)._initialize()