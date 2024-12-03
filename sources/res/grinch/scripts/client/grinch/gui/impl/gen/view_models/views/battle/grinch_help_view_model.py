from frameworks.wulf import ViewModel

class GrinchHelpViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=0, commands=0):
        super(GrinchHelpViewModel, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(GrinchHelpViewModel, self)._initialize()