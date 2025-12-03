from frameworks.wulf import ViewModel

class DeadlineTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=0, commands=0):
        super(DeadlineTooltipModel, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(DeadlineTooltipModel, self)._initialize()