from frameworks.wulf import ViewModel

class LunarHelpViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=0, commands=0):
        super(LunarHelpViewModel, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(LunarHelpViewModel, self)._initialize()