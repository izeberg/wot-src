from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.new_year.components.ny_economic_bonus_model import NyEconomicBonusModel

class HoEconomicBonusPopoverModel(ViewModel):
    __slots__ = ('onSelectBonus', )

    def __init__(self, properties=3, commands=1):
        super(HoEconomicBonusPopoverModel, self).__init__(properties=properties, commands=commands)

    def getSelectedBonusName(self):
        return self._getString(0)

    def setSelectedBonusName(self, value):
        self._setString(0, value)

    def getBonusError(self):
        return self._getBool(1)

    def setBonusError(self, value):
        self._setBool(1, value)

    def getEconomicBonuses(self):
        return self._getArray(2)

    def setEconomicBonuses(self, value):
        self._setArray(2, value)

    @staticmethod
    def getEconomicBonusesType():
        return NyEconomicBonusModel

    def _initialize(self):
        super(HoEconomicBonusPopoverModel, self)._initialize()
        self._addStringProperty('selectedBonusName', '')
        self._addBoolProperty('bonusError', False)
        self._addArrayProperty('economicBonuses', Array())
        self.onSelectBonus = self._addCommand('onSelectBonus')