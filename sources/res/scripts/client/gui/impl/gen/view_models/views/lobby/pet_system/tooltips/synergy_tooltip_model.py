from frameworks.wulf import ViewModel

class SynergyTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(SynergyTooltipModel, self).__init__(properties=properties, commands=commands)

    def getProgress(self):
        return self._getNumber(0)

    def setProgress(self, value):
        self._setNumber(0, value)

    def _initialize(self):
        super(SynergyTooltipModel, self)._initialize()
        self._addNumberProperty('progress', 0)