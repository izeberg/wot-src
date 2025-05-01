from frameworks.wulf import ViewModel

class HbTooltipsConstants(ViewModel):
    __slots__ = ()
    TOOLTIP_NOT_ENOUGH_MONEY = 'TOOLTIP_NOT_ENOUGH_MONEY'
    TOOLTIP_MONEY = 'TOOLTIP_MONEY'
    TOOLTIP_BONUS = 'TOOLTIP_BONUS'

    def __init__(self, properties=0, commands=0):
        super(HbTooltipsConstants, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(HbTooltipsConstants, self)._initialize()