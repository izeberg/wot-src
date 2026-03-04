from frameworks.wulf import ViewModel

class RetireUndertrainedTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(RetireUndertrainedTooltipViewModel, self).__init__(properties=properties, commands=commands)

    def getHasUndertrainedCrewMembers(self):
        return self._getBool(0)

    def setHasUndertrainedCrewMembers(self, value):
        self._setBool(0, value)

    def _initialize(self):
        super(RetireUndertrainedTooltipViewModel, self)._initialize()
        self._addBoolProperty('hasUndertrainedCrewMembers', False)