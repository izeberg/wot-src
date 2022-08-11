from frameworks.wulf import ViewModel

class ChinaLootBoxesWelcomeScreenModel(ViewModel):
    __slots__ = ('onBuy', 'onClose')

    def __init__(self, properties=5, commands=2):
        super(ChinaLootBoxesWelcomeScreenModel, self).__init__(properties=properties, commands=commands)

    def getTimeLeft(self):
        return self._getNumber(0)

    def setTimeLeft(self, value):
        self._setNumber(0, value)

    def getDailyBoxesCount(self):
        return self._getNumber(1)

    def setDailyBoxesCount(self, value):
        self._setNumber(1, value)

    def getGuaranteedLimit(self):
        return self._getNumber(2)

    def setGuaranteedLimit(self, value):
        self._setNumber(2, value)

    def getEndDate(self):
        return self._getNumber(3)

    def setEndDate(self, value):
        self._setNumber(3, value)

    def getIsBuyAvailable(self):
        return self._getBool(4)

    def setIsBuyAvailable(self, value):
        self._setBool(4, value)

    def _initialize(self):
        super(ChinaLootBoxesWelcomeScreenModel, self)._initialize()
        self._addNumberProperty('timeLeft', 0)
        self._addNumberProperty('dailyBoxesCount', 0)
        self._addNumberProperty('guaranteedLimit', 0)
        self._addNumberProperty('endDate', 0)
        self._addBoolProperty('isBuyAvailable', True)
        self.onBuy = self._addCommand('onBuy')
        self.onClose = self._addCommand('onClose')