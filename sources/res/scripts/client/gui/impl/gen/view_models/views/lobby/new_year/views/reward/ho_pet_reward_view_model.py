from frameworks.wulf import Array, ViewModel

class HoPetRewardViewModel(ViewModel):
    __slots__ = ('onGoToPetDen', 'onVideoStarted', 'onVideoStopped')

    def __init__(self, properties=6, commands=3):
        super(HoPetRewardViewModel, self).__init__(properties=properties, commands=commands)

    def getPetNameID(self):
        return self._getNumber(0)

    def setPetNameID(self, value):
        self._setNumber(0, value)

    def getBreedName(self):
        return self._getString(1)

    def setBreedName(self, value):
        self._setString(1, value)

    def getIsViewAccessible(self):
        return self._getBool(2)

    def setIsViewAccessible(self, value):
        self._setBool(2, value)

    def getIsPetDenAvailable(self):
        return self._getBool(3)

    def setIsPetDenAvailable(self, value):
        self._setBool(3, value)

    def getIsDayHangar(self):
        return self._getBool(4)

    def setIsDayHangar(self, value):
        self._setBool(4, value)

    def getPromotionBonuses(self):
        return self._getArray(5)

    def setPromotionBonuses(self, value):
        self._setArray(5, value)

    @staticmethod
    def getPromotionBonusesType():
        return unicode

    def _initialize(self):
        super(HoPetRewardViewModel, self)._initialize()
        self._addNumberProperty('petNameID', 0)
        self._addStringProperty('breedName', '')
        self._addBoolProperty('isViewAccessible', True)
        self._addBoolProperty('isPetDenAvailable', True)
        self._addBoolProperty('isDayHangar', False)
        self._addArrayProperty('promotionBonuses', Array())
        self.onGoToPetDen = self._addCommand('onGoToPetDen')
        self.onVideoStarted = self._addCommand('onVideoStarted')
        self.onVideoStopped = self._addCommand('onVideoStopped')