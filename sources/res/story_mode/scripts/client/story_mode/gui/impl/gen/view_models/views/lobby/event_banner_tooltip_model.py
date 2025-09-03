from frameworks.wulf import ViewModel

class EventBannerTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(EventBannerTooltipModel, self).__init__(properties=properties, commands=commands)

    def getTimerValue(self):
        return self._getNumber(0)

    def setTimerValue(self, value):
        self._setNumber(0, value)

    def _initialize(self):
        super(EventBannerTooltipModel, self)._initialize()
        self._addNumberProperty('timerValue', 0)