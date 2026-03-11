from frameworks.wulf import ViewModel

class ParagonsCarouselPointsTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(ParagonsCarouselPointsTooltipModel, self).__init__(properties=properties, commands=commands)

    def getIsNeedWin(self):
        return self._getBool(0)

    def setIsNeedWin(self, value):
        self._setBool(0, value)

    def getIsNextVehUnlocked(self):
        return self._getBool(1)

    def setIsNextVehUnlocked(self, value):
        self._setBool(1, value)

    def _initialize(self):
        super(ParagonsCarouselPointsTooltipModel, self)._initialize()
        self._addBoolProperty('isNeedWin', True)
        self._addBoolProperty('isNextVehUnlocked', False)