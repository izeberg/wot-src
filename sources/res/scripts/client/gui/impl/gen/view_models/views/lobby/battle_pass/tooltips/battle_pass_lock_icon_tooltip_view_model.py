from frameworks.wulf import ViewModel

class BattlePassLockIconTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(BattlePassLockIconTooltipViewModel, self).__init__(properties=properties, commands=commands)

    def getIsHoliday(self):
        return self._getBool(0)

    def setIsHoliday(self, value):
        self._setBool(0, value)

    def _initialize(self):
        super(BattlePassLockIconTooltipViewModel, self)._initialize()
        self._addBoolProperty('isHoliday', False)