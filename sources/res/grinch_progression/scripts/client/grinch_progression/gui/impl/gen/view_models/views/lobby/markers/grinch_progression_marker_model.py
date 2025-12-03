from enum import Enum
from frameworks.wulf import ViewModel

class MarkerState(Enum):
    LOCK = 'lock'
    ACTIVE = 'active'
    PAUSED = 'paused'
    DONE = 'done'


class GrinchProgressionMarkerModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=10, commands=0):
        super(GrinchProgressionMarkerModel, self).__init__(properties=properties, commands=commands)

    def getCountdown(self):
        return self._getNumber(0)

    def setCountdown(self, value):
        self._setNumber(0, value)

    def getPoints(self):
        return self._getNumber(1)

    def setPoints(self, value):
        self._setNumber(1, value)

    def getMaxPoints(self):
        return self._getNumber(2)

    def setMaxPoints(self, value):
        self._setNumber(2, value)

    def getPrevPoints(self):
        return self._getNumber(3)

    def setPrevPoints(self, value):
        self._setNumber(3, value)

    def getIsVisible(self):
        return self._getBool(4)

    def setIsVisible(self, value):
        self._setBool(4, value)

    def getIsPostProgression(self):
        return self._getBool(5)

    def setIsPostProgression(self, value):
        self._setBool(5, value)

    def getNumberOfRewardsToClaim(self):
        return self._getNumber(6)

    def setNumberOfRewardsToClaim(self, value):
        self._setNumber(6, value)

    def getPrevNumberOfRewardsToClaim(self):
        return self._getNumber(7)

    def setPrevNumberOfRewardsToClaim(self, value):
        self._setNumber(7, value)

    def getMarkerState(self):
        return MarkerState(self._getString(8))

    def setMarkerState(self, value):
        self._setString(8, value.value)

    def getSyncInitiator(self):
        return self._getNumber(9)

    def setSyncInitiator(self, value):
        self._setNumber(9, value)

    def _initialize(self):
        super(GrinchProgressionMarkerModel, self)._initialize()
        self._addNumberProperty('countdown', 0)
        self._addNumberProperty('points', 0)
        self._addNumberProperty('maxPoints', 0)
        self._addNumberProperty('prevPoints', 0)
        self._addBoolProperty('isVisible', True)
        self._addBoolProperty('isPostProgression', False)
        self._addNumberProperty('numberOfRewardsToClaim', 0)
        self._addNumberProperty('prevNumberOfRewardsToClaim', 0)
        self._addStringProperty('markerState', MarkerState.LOCK.value)
        self._addNumberProperty('syncInitiator', 0)