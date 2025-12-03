from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.new_year.views.marketplace.card_model import CardModel

class CardGroupsModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(CardGroupsModel, self).__init__(properties=properties, commands=commands)

    def getYearName(self):
        return self._getString(0)

    def setYearName(self, value):
        self._setString(0, value)

    def getCards(self):
        return self._getArray(1)

    def setCards(self, value):
        self._setArray(1, value)

    @staticmethod
    def getCardsType():
        return CardModel

    def _initialize(self):
        super(CardGroupsModel, self)._initialize()
        self._addStringProperty('yearName', '')
        self._addArrayProperty('cards', Array())