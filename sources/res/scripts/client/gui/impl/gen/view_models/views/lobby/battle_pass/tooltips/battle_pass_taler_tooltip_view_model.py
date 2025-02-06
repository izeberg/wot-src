from frameworks.wulf import ViewModel

class BattlePassTalerTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=0, commands=0):
        super(BattlePassTalerTooltipViewModel, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(BattlePassTalerTooltipViewModel, self)._initialize()