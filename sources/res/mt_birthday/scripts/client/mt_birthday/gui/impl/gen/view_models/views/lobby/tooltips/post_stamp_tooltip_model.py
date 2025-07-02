from frameworks.wulf import ViewModel

class PostStampTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(PostStampTooltipModel, self).__init__(properties=properties, commands=commands)

    def getCurrencyCount(self):
        return self._getNumber(0)

    def setCurrencyCount(self, value):
        self._setNumber(0, value)

    def _initialize(self):
        super(PostStampTooltipModel, self)._initialize()
        self._addNumberProperty('currencyCount', 0)