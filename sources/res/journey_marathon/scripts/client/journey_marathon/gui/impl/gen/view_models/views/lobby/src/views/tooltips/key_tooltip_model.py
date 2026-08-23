from frameworks.wulf import ViewModel

class KeyTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(KeyTooltipModel, self).__init__(properties=properties, commands=commands)

    def getKeyName(self):
        return self._getString(0)

    def setKeyName(self, value):
        self._setString(0, value)

    def _initialize(self):
        super(KeyTooltipModel, self)._initialize()
        self._addStringProperty('keyName', '')