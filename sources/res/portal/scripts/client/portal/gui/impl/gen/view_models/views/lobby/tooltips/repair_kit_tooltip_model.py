from frameworks.wulf import ViewModel

class RepairKitTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=0, commands=0):
        super(RepairKitTooltipModel, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(RepairKitTooltipModel, self)._initialize()