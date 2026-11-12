from gui.impl.gen.view_models.views.lobby.hangar.header_widget_view_model import HeaderWidgetViewModel

class TankAcademyEntryPointViewModel(HeaderWidgetViewModel):
    __slots__ = ('onClick', )

    def __init__(self, properties=9, commands=2):
        super(TankAcademyEntryPointViewModel, self).__init__(properties=properties, commands=commands)

    def getIsSecondaryEntry(self):
        return self._getBool(0)

    def setIsSecondaryEntry(self, value):
        self._setBool(0, value)

    def getIsMainViewVisited(self):
        return self._getBool(1)

    def setIsMainViewVisited(self, value):
        self._setBool(1, value)

    def getCurrentProgress(self):
        return self._getNumber(2)

    def setCurrentProgress(self, value):
        self._setNumber(2, value)

    def getMaxProgress(self):
        return self._getNumber(3)

    def setMaxProgress(self, value):
        self._setNumber(3, value)

    def getQuestNumber(self):
        return self._getNumber(4)

    def setQuestNumber(self, value):
        self._setNumber(4, value)

    def getIsCompleted(self):
        return self._getBool(5)

    def setIsCompleted(self, value):
        self._setBool(5, value)

    def getIsPaused(self):
        return self._getBool(6)

    def setIsPaused(self, value):
        self._setBool(6, value)

    def getUnobtainedVehiclesCount(self):
        return self._getNumber(7)

    def setUnobtainedVehiclesCount(self, value):
        self._setNumber(7, value)

    def getEndDate(self):
        return self._getNumber(8)

    def setEndDate(self, value):
        self._setNumber(8, value)

    def _initialize(self):
        super(TankAcademyEntryPointViewModel, self)._initialize()
        self._addBoolProperty('isSecondaryEntry', False)
        self._addBoolProperty('isMainViewVisited', False)
        self._addNumberProperty('currentProgress', 0)
        self._addNumberProperty('maxProgress', 0)
        self._addNumberProperty('questNumber', 0)
        self._addBoolProperty('isCompleted', False)
        self._addBoolProperty('isPaused', False)
        self._addNumberProperty('unobtainedVehiclesCount', 0)
        self._addNumberProperty('endDate', 0)
        self.onClick = self._addCommand('onClick')