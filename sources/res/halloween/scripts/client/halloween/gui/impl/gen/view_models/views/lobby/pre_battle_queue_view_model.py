from gui.impl.gen.view_models.views.selectable_view_model import SelectableViewModel

class PreBattleQueueViewModel(SelectableViewModel):
    __slots__ = ('onExitBattle', 'onEscape')

    def __init__(self, properties=5, commands=4):
        super(PreBattleQueueViewModel, self).__init__(properties=properties, commands=commands)

    def getSelectedDifficultyLevel(self):
        return self._getNumber(0)

    def setSelectedDifficultyLevel(self, value):
        self._setNumber(0, value)

    def getIsExitButtonAvailable(self):
        return self._getBool(1)

    def setIsExitButtonAvailable(self, value):
        self._setBool(1, value)

    def getVehicleType(self):
        return self._getString(2)

    def setVehicleType(self, value):
        self._setString(2, value)

    def getVehicleName(self):
        return self._getString(3)

    def setVehicleName(self, value):
        self._setString(3, value)

    def getTimerStartTime(self):
        return self._getNumber(4)

    def setTimerStartTime(self, value):
        self._setNumber(4, value)

    def _initialize(self):
        super(PreBattleQueueViewModel, self)._initialize()
        self._addNumberProperty('selectedDifficultyLevel', 0)
        self._addBoolProperty('isExitButtonAvailable', False)
        self._addStringProperty('vehicleType', '')
        self._addStringProperty('vehicleName', '')
        self._addNumberProperty('timerStartTime', 0)
        self.onExitBattle = self._addCommand('onExitBattle')
        self.onEscape = self._addCommand('onEscape')