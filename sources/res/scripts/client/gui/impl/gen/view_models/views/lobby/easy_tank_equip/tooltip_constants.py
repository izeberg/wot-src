from frameworks.wulf import ViewModel

class TooltipConstants(ViewModel):
    __slots__ = ()
    TANKMAN = 'tankman'
    HANGAR_MODULE = 'hangarModule'
    TECH_MAIN_SHELL = 'techMainShell'
    PRICE_DISCOUNT = 'priceDiscount'

    def __init__(self, properties=0, commands=0):
        super(TooltipConstants, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(TooltipConstants, self)._initialize()