from frameworks.wulf import ViewModel

class EventBannerTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(EventBannerTooltipModel, self).__init__(properties=properties, commands=commands)

    def getBundleType(self):
        return self._getString(0)

    def setBundleType(self, value):
        self._setString(0, value)

    def getTimeLeft(self):
        return self._getNumber(1)

    def setTimeLeft(self, value):
        self._setNumber(1, value)

    def _initialize(self):
        super(EventBannerTooltipModel, self)._initialize()
        self._addStringProperty('bundleType', '')
        self._addNumberProperty('timeLeft', 0)