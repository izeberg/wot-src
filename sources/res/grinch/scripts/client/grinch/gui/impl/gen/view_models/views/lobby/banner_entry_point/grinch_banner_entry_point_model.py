from enum import Enum
from frameworks.wulf import ViewModel

class State(Enum):
    INTRO = 'intro'
    INPROGRESS = 'inProgress'
    COMPLETED = 'completed'
    FROZEN = 'frozen'
    BATTLESFINISHED = 'battlesFinished'


class PerformanceRiskEnum(Enum):
    LOWRISK = 'lowRisk'
    MEDIUMRISK = 'mediumRisk'
    HIGHRISK = 'highRisk'


class GrinchBannerEntryPointModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=8, commands=0):
        super(GrinchBannerEntryPointModel, self).__init__(properties=properties, commands=commands)

    def getDate(self):
        return self._getNumber(0)

    def setDate(self, value):
        self._setNumber(0, value)

    def getEndDate(self):
        return self._getNumber(1)

    def setEndDate(self, value):
        self._setNumber(1, value)

    def getPerformanceRisk(self):
        return PerformanceRiskEnum(self._getString(2))

    def setPerformanceRisk(self, value):
        self._setString(2, value.value)

    def getMaxProgressionStep(self):
        return self._getNumber(3)

    def setMaxProgressionStep(self, value):
        self._setNumber(3, value)

    def getFinishedLevelsCount(self):
        return self._getNumber(4)

    def setFinishedLevelsCount(self, value):
        self._setNumber(4, value)

    def getNextTimeEnable(self):
        return self._getNumber(5)

    def setNextTimeEnable(self, value):
        self._setNumber(5, value)

    def getState(self):
        return State(self._getString(6))

    def setState(self, value):
        self._setString(6, value.value)

    def getShowClaimableRewards(self):
        return self._getBool(7)

    def setShowClaimableRewards(self, value):
        self._setBool(7, value)

    def _initialize(self):
        super(GrinchBannerEntryPointModel, self)._initialize()
        self._addNumberProperty('date', 0)
        self._addNumberProperty('endDate', 0)
        self._addStringProperty('performanceRisk')
        self._addNumberProperty('maxProgressionStep', 1)
        self._addNumberProperty('finishedLevelsCount', 0)
        self._addNumberProperty('nextTimeEnable', 0)
        self._addStringProperty('state')
        self._addBoolProperty('showClaimableRewards', False)