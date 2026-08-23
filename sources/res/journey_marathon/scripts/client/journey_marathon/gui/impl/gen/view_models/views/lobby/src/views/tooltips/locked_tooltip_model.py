from frameworks.wulf import ViewModel

class LockedTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(LockedTooltipModel, self).__init__(properties=properties, commands=commands)

    def getKeyName(self):
        return self._getString(0)

    def setKeyName(self, value):
        self._setString(0, value)

    def getIsUnlocked(self):
        return self._getBool(1)

    def setIsUnlocked(self, value):
        self._setBool(1, value)

    def _initialize(self):
        super(LockedTooltipModel, self)._initialize()
        self._addStringProperty('keyName', '')
        self._addBoolProperty('isUnlocked', False)