from frameworks.wulf import ViewModel

class DisablePlayerTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(DisablePlayerTooltipModel, self).__init__(properties=properties, commands=commands)

    def getTime(self):
        return self._getNumber(0)

    def setTime(self, value):
        self._setNumber(0, value)

    def _initialize(self):
        super(DisablePlayerTooltipModel, self)._initialize()
        self._addNumberProperty('time', 0)