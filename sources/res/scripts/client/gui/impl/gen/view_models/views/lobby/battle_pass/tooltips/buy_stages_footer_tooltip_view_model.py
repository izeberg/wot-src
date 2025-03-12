from frameworks.wulf import ViewModel

class BuyStagesFooterTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(BuyStagesFooterTooltipViewModel, self).__init__(properties=properties, commands=commands)

    def getIsActive(self):
        return self._getBool(0)

    def setIsActive(self, value):
        self._setBool(0, value)

    def _initialize(self):
        super(BuyStagesFooterTooltipViewModel, self)._initialize()
        self._addBoolProperty('isActive', False)