from frameworks.wulf import ViewModel

class GrinchHelpModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=0, commands=0):
        super(GrinchHelpModel, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(GrinchHelpModel, self)._initialize()