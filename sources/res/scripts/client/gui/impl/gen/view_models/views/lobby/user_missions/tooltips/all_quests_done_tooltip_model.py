from frameworks.wulf import ViewModel

class AllQuestsDoneTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(AllQuestsDoneTooltipModel, self).__init__(properties=properties, commands=commands)

    def getCountdown(self):
        return self._getNumber(0)

    def setCountdown(self, value):
        self._setNumber(0, value)

    def _initialize(self):
        super(AllQuestsDoneTooltipModel, self)._initialize()
        self._addNumberProperty('countdown', 0)