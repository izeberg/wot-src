from frameworks.wulf import ViewModel

class RandomGoodieTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=0, commands=0):
        super(RandomGoodieTooltipModel, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(RandomGoodieTooltipModel, self)._initialize()