from frameworks.wulf import ViewModel

class VignetteModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(VignetteModel, self).__init__(properties=properties, commands=commands)

    def getIsHolidayOpsHangarActive(self):
        return self._getBool(0)

    def setIsHolidayOpsHangarActive(self, value):
        self._setBool(0, value)

    def _initialize(self):
        super(VignetteModel, self)._initialize()
        self._addBoolProperty('isHolidayOpsHangarActive', False)