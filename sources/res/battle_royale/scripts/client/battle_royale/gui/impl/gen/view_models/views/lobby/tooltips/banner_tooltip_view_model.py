from enum import Enum
from frameworks.wulf import ViewModel

class PerformanceRisk(Enum):
    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'


class BannerTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(BannerTooltipViewModel, self).__init__(properties=properties, commands=commands)

    def getTime(self):
        return self._getNumber(0)

    def setTime(self, value):
        self._setNumber(0, value)

    def getModeState(self):
        return self._getString(1)

    def setModeState(self, value):
        self._setString(1, value)

    def getPerformanceRisk(self):
        return PerformanceRisk(self._getString(2))

    def setPerformanceRisk(self, value):
        self._setString(2, value.value)

    def _initialize(self):
        super(BannerTooltipViewModel, self)._initialize()
        self._addNumberProperty('time', 0)
        self._addStringProperty('modeState', '')
        self._addStringProperty('performanceRisk', PerformanceRisk.HIGH.value)