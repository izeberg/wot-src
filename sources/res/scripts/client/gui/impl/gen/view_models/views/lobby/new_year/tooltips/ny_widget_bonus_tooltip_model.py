from enum import Enum
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.new_year.components.ny_economic_bonus_model import NyEconomicBonusModel

class TooltipState(Enum):
    NORMAL = 'normal'
    LEVELERROR = 'levelError'
    VEHICLEERROR = 'vehicleError'


class NyWidgetBonusTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(NyWidgetBonusTooltipModel, self).__init__(properties=properties, commands=commands)

    def getTooltipState(self):
        return TooltipState(self._getString(0))

    def setTooltipState(self, value):
        self._setString(0, value.value)

    def getLevel(self):
        return self._getNumber(1)

    def setLevel(self, value):
        self._setNumber(1, value)

    def getSelectedBonusName(self):
        return self._getString(2)

    def setSelectedBonusName(self, value):
        self._setString(2, value)

    def getSelectedBonusValue(self):
        return self._getReal(3)

    def setSelectedBonusValue(self, value):
        self._setReal(3, value)

    def getEconomicBonuses(self):
        return self._getArray(4)

    def setEconomicBonuses(self, value):
        self._setArray(4, value)

    @staticmethod
    def getEconomicBonusesType():
        return NyEconomicBonusModel

    def _initialize(self):
        super(NyWidgetBonusTooltipModel, self)._initialize()
        self._addStringProperty('tooltipState', TooltipState.NORMAL.value)
        self._addNumberProperty('level', 1)
        self._addStringProperty('selectedBonusName', '')
        self._addRealProperty('selectedBonusValue', 0.0)
        self._addArrayProperty('economicBonuses', Array())