from frameworks.wulf import ViewModel

class CosmicSimpleTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=0, commands=0):
        super(CosmicSimpleTooltipModel, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(CosmicSimpleTooltipModel, self)._initialize()