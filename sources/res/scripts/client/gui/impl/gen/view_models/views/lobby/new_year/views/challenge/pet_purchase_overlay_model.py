from gui.impl.gen.view_models.views.lobby.new_year.components.ny_purchase_model import NyPurchaseModel
from gui.impl.gen.view_models.views.lobby.new_year.views.challenge.ho_mastery_progression_model import HoMasteryProgressionModel

class PetPurchaseOverlayModel(NyPurchaseModel):
    __slots__ = ('onGoToVillage', 'onGoToPetDen')

    def __init__(self, properties=10, commands=4):
        super(PetPurchaseOverlayModel, self).__init__(properties=properties, commands=commands)

    @property
    def masteryProgression(self):
        return self._getViewModel(5)

    @staticmethod
    def getMasteryProgressionType():
        return HoMasteryProgressionModel

    def getIsPetAvailable(self):
        return self._getBool(6)

    def setIsPetAvailable(self, value):
        self._setBool(6, value)

    def getIsPetSystemEnabled(self):
        return self._getBool(7)

    def setIsPetSystemEnabled(self, value):
        self._setBool(7, value)

    def getPriceWithDiscount(self):
        return self._getNumber(8)

    def setPriceWithDiscount(self, value):
        self._setNumber(8, value)

    def getDiscountPercent(self):
        return self._getNumber(9)

    def setDiscountPercent(self, value):
        self._setNumber(9, value)

    def _initialize(self):
        super(PetPurchaseOverlayModel, self)._initialize()
        self._addViewModelProperty('masteryProgression', HoMasteryProgressionModel())
        self._addBoolProperty('isPetAvailable', False)
        self._addBoolProperty('isPetSystemEnabled', True)
        self._addNumberProperty('priceWithDiscount', 0)
        self._addNumberProperty('discountPercent', 0)
        self.onGoToVillage = self._addCommand('onGoToVillage')
        self.onGoToPetDen = self._addCommand('onGoToPetDen')