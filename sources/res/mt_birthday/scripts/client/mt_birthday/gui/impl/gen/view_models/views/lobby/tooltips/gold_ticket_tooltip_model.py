from frameworks.wulf import ViewModel

class GoldTicketTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(GoldTicketTooltipModel, self).__init__(properties=properties, commands=commands)

    def getCurrencyCount(self):
        return self._getNumber(0)

    def setCurrencyCount(self, value):
        self._setNumber(0, value)

    def _initialize(self):
        super(GoldTicketTooltipModel, self)._initialize()
        self._addNumberProperty('currencyCount', 0)