from frameworks.wulf import ViewModel

class UpgradeInfoTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=0, commands=0):
        super(UpgradeInfoTooltipModel, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(UpgradeInfoTooltipModel, self)._initialize()