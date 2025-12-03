from frameworks.wulf import ViewModel

class RerollInfoContainerTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=0, commands=0):
        super(RerollInfoContainerTooltipModel, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(RerollInfoContainerTooltipModel, self)._initialize()