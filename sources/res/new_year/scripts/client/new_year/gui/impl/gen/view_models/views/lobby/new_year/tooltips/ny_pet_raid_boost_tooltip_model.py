from frameworks.wulf import ViewModel

class NyPetRaidBoostTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(NyPetRaidBoostTooltipModel, self).__init__(properties=properties, commands=commands)

    def getBoostAmount(self):
        return self._getNumber(0)

    def setBoostAmount(self, value):
        self._setNumber(0, value)

    def getMaxBoostLimit(self):
        return self._getNumber(1)

    def setMaxBoostLimit(self, value):
        self._setNumber(1, value)

    def getBoostTime(self):
        return self._getNumber(2)

    def setBoostTime(self, value):
        self._setNumber(2, value)

    def getBoostsToAdd(self):
        return self._getNumber(3)

    def setBoostsToAdd(self, value):
        self._setNumber(3, value)

    def getBoostAccrualTime(self):
        return self._getNumber(4)

    def setBoostAccrualTime(self, value):
        self._setNumber(4, value)

    def _initialize(self):
        super(NyPetRaidBoostTooltipModel, self)._initialize()
        self._addNumberProperty('boostAmount', 0)
        self._addNumberProperty('maxBoostLimit', 0)
        self._addNumberProperty('boostTime', 0)
        self._addNumberProperty('boostsToAdd', 0)
        self._addNumberProperty('boostAccrualTime', 0)