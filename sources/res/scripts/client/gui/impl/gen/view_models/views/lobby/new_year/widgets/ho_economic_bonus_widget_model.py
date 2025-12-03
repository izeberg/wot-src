from frameworks.wulf import ViewModel

class HoEconomicBonusWidgetModel(ViewModel):
    __slots__ = ('onGoToAssignments', )

    def __init__(self, properties=3, commands=1):
        super(HoEconomicBonusWidgetModel, self).__init__(properties=properties, commands=commands)

    def getSelectedBonusName(self):
        return self._getString(0)

    def setSelectedBonusName(self, value):
        self._setString(0, value)

    def getSelectedBonusValue(self):
        return self._getReal(1)

    def setSelectedBonusValue(self, value):
        self._setReal(1, value)

    def getBonusError(self):
        return self._getBool(2)

    def setBonusError(self, value):
        self._setBool(2, value)

    def _initialize(self):
        super(HoEconomicBonusWidgetModel, self)._initialize()
        self._addStringProperty('selectedBonusName', '')
        self._addRealProperty('selectedBonusValue', 0.0)
        self._addBoolProperty('bonusError', False)
        self.onGoToAssignments = self._addCommand('onGoToAssignments')