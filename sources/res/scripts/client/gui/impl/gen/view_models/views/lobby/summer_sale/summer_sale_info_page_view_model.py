from frameworks.wulf import ViewModel

class SummerSaleInfoPageViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=0, commands=0):
        super(SummerSaleInfoPageViewModel, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(SummerSaleInfoPageViewModel, self)._initialize()