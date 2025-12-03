from frameworks.wulf import ViewModel

class OtgQuestTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(OtgQuestTooltipViewModel, self).__init__(properties=properties, commands=commands)

    def getExpireTime(self):
        return self._getNumber(0)

    def setExpireTime(self, value):
        self._setNumber(0, value)

    def _initialize(self):
        super(OtgQuestTooltipViewModel, self)._initialize()
        self._addNumberProperty('expireTime', 0)