from frameworks.wulf import ViewModel

class GoldTicketTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=0, commands=0):
        super(GoldTicketTooltipModel, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(GoldTicketTooltipModel, self)._initialize()