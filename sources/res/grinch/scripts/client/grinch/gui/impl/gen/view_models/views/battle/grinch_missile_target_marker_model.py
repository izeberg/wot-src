from enum import Enum
from frameworks.wulf import ViewModel

class TargetingStatus(Enum):
    TARGETING = 'targeting'
    LOCKED = 'locked'


class GrinchMissileTargetMarkerModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(GrinchMissileTargetMarkerModel, self).__init__(properties=properties, commands=commands)

    def getPosx(self):
        return self._getReal(0)

    def setPosx(self, value):
        self._setReal(0, value)

    def getPosy(self):
        return self._getReal(1)

    def setPosy(self, value):
        self._setReal(1, value)

    def getScale(self):
        return self._getReal(2)

    def setScale(self, value):
        self._setReal(2, value)

    def getIsEnabled(self):
        return self._getBool(3)

    def setIsEnabled(self, value):
        self._setBool(3, value)

    def getTargetID(self):
        return self._getNumber(4)

    def setTargetID(self, value):
        self._setNumber(4, value)

    def getTargetingStatus(self):
        return TargetingStatus(self._getString(5))

    def setTargetingStatus(self, value):
        self._setString(5, value.value)

    def getRemainingLockTime(self):
        return self._getReal(6)

    def setRemainingLockTime(self, value):
        self._setReal(6, value)

    def _initialize(self):
        super(GrinchMissileTargetMarkerModel, self)._initialize()
        self._addRealProperty('posx', 0.0)
        self._addRealProperty('posy', 0.0)
        self._addRealProperty('scale', 1.0)
        self._addBoolProperty('isEnabled', False)
        self._addNumberProperty('targetID', 0)
        self._addStringProperty('targetingStatus')
        self._addRealProperty('remainingLockTime', 0.0)