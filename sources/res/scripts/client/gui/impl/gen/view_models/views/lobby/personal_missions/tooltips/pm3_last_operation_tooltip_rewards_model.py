from frameworks.wulf import ViewModel

class Pm3LastOperationTooltipRewardsModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(Pm3LastOperationTooltipRewardsModel, self).__init__(properties=properties, commands=commands)

    def getName(self):
        return self._getString(0)

    def setName(self, value):
        self._setString(0, value)

    def getIcon(self):
        return self._getString(1)

    def setIcon(self, value):
        self._setString(1, value)

    def _initialize(self):
        super(Pm3LastOperationTooltipRewardsModel, self)._initialize()
        self._addStringProperty('name', '')
        self._addStringProperty('icon', '')