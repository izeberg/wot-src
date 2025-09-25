from frameworks.wulf import ViewModel

class BasicMissionsTabModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(BasicMissionsTabModel, self).__init__(properties=properties, commands=commands)

    def getIsDailySectionAvailable(self):
        return self._getBool(0)

    def setIsDailySectionAvailable(self, value):
        self._setBool(0, value)

    def getIsWeeklySectionAvailable(self):
        return self._getBool(1)

    def setIsWeeklySectionAvailable(self, value):
        self._setBool(1, value)

    def getIsPMSectionAvailable(self):
        return self._getBool(2)

    def setIsPMSectionAvailable(self, value):
        self._setBool(2, value)

    def _initialize(self):
        super(BasicMissionsTabModel, self)._initialize()
        self._addBoolProperty('isDailySectionAvailable', False)
        self._addBoolProperty('isWeeklySectionAvailable', False)
        self._addBoolProperty('isPMSectionAvailable', False)