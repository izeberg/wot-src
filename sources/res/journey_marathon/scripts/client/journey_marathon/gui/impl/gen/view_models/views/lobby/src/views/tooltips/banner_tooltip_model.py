from frameworks.wulf import ViewModel

class BannerTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(BannerTooltipModel, self).__init__(properties=properties, commands=commands)

    def getTimeLeft(self):
        return self._getNumber(0)

    def setTimeLeft(self, value):
        self._setNumber(0, value)

    def getBannerState(self):
        return self._getString(1)

    def setBannerState(self, value):
        self._setString(1, value)

    def _initialize(self):
        super(BannerTooltipModel, self)._initialize()
        self._addNumberProperty('timeLeft', 0)
        self._addStringProperty('bannerState', '')