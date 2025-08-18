from frameworks.wulf import ViewModel

class CinematicTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(CinematicTooltipModel, self).__init__(properties=properties, commands=commands)

    def getIsOutroTooltip(self):
        return self._getBool(0)

    def setIsOutroTooltip(self, value):
        self._setBool(0, value)

    def getIsProgressionCompleted(self):
        return self._getBool(1)

    def setIsProgressionCompleted(self, value):
        self._setBool(1, value)

    def _initialize(self):
        super(CinematicTooltipModel, self)._initialize()
        self._addBoolProperty('isOutroTooltip', False)
        self._addBoolProperty('isProgressionCompleted', False)