from frameworks.wulf import ViewModel

class RerollDescriptionTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=0, commands=0):
        super(RerollDescriptionTooltipViewModel, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(RerollDescriptionTooltipViewModel, self)._initialize()