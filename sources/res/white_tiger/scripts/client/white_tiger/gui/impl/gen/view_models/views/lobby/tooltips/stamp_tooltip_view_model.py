from frameworks.wulf import ViewModel

class StampTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=0, commands=0):
        super(StampTooltipViewModel, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(StampTooltipViewModel, self)._initialize()