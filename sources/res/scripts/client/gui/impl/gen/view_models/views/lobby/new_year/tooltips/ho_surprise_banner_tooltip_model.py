from frameworks.wulf import ViewModel

class HoSurpriseBannerTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(HoSurpriseBannerTooltipModel, self).__init__(properties=properties, commands=commands)

    def getIsActiveState(self):
        return self._getBool(0)

    def setIsActiveState(self, value):
        self._setBool(0, value)

    def _initialize(self):
        super(HoSurpriseBannerTooltipModel, self)._initialize()
        self._addBoolProperty('isActiveState', False)