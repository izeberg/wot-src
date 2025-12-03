from frameworks.wulf import ViewModel

class InfoPageModel(ViewModel):
    __slots__ = ('onClose', )

    def __init__(self, properties=3, commands=1):
        super(InfoPageModel, self).__init__(properties=properties, commands=commands)

    def getRerollInterval(self):
        return self._getNumber(0)

    def setRerollInterval(self, value):
        self._setNumber(0, value)

    def getIsWeeklySectionAvailable(self):
        return self._getBool(1)

    def setIsWeeklySectionAvailable(self, value):
        self._setBool(1, value)

    def getIsHolidayOpsActive(self):
        return self._getBool(2)

    def setIsHolidayOpsActive(self, value):
        self._setBool(2, value)

    def _initialize(self):
        super(InfoPageModel, self)._initialize()
        self._addNumberProperty('rerollInterval', 0)
        self._addBoolProperty('isWeeklySectionAvailable', False)
        self._addBoolProperty('isHolidayOpsActive', False)
        self.onClose = self._addCommand('onClose')