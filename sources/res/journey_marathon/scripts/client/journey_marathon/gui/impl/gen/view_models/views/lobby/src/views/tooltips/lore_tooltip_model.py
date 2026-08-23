from frameworks.wulf import ViewModel

class LoreTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(LoreTooltipModel, self).__init__(properties=properties, commands=commands)

    def getIsUnlocked(self):
        return self._getBool(0)

    def setIsUnlocked(self, value):
        self._setBool(0, value)

    def _initialize(self):
        super(LoreTooltipModel, self)._initialize()
        self._addBoolProperty('isUnlocked', False)