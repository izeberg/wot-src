from frameworks.wulf import ViewModel

class NyMarketLackTheResTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(NyMarketLackTheResTooltipModel, self).__init__(properties=properties, commands=commands)

    def getResourceType(self):
        return self._getString(0)

    def setResourceType(self, value):
        self._setString(0, value)

    def getShortageValue(self):
        return self._getNumber(1)

    def setShortageValue(self, value):
        self._setNumber(1, value)

    def _initialize(self):
        super(NyMarketLackTheResTooltipModel, self)._initialize()
        self._addStringProperty('resourceType', '')
        self._addNumberProperty('shortageValue', 0)