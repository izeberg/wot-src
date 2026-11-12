from frameworks.wulf import ViewModel

class EnvSwitcherBtnViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=0, commands=0):
        super(EnvSwitcherBtnViewModel, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(EnvSwitcherBtnViewModel, self)._initialize()