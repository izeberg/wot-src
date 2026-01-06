from frameworks.wulf import ViewModel

class TankmanChagePreviewTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=0, commands=0):
        super(TankmanChagePreviewTooltipModel, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(TankmanChagePreviewTooltipModel, self)._initialize()