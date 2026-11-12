from frameworks.wulf import ViewModel

class CustomizationResourceExchangeTabModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(CustomizationResourceExchangeTabModel, self).__init__(properties=properties, commands=commands)

    def getTabId(self):
        return self._getNumber(0)

    def setTabId(self, value):
        self._setNumber(0, value)

    def getItemType(self):
        return self._getString(1)

    def setItemType(self, value):
        self._setString(1, value)

    def getAvailableCount(self):
        return self._getNumber(2)

    def setAvailableCount(self, value):
        self._setNumber(2, value)

    def getSelectedCount(self):
        return self._getNumber(3)

    def setSelectedCount(self, value):
        self._setNumber(3, value)

    def getIsDone(self):
        return self._getBool(4)

    def setIsDone(self, value):
        self._setBool(4, value)

    def getIsSelected(self):
        return self._getBool(5)

    def setIsSelected(self, value):
        self._setBool(5, value)

    def _initialize(self):
        super(CustomizationResourceExchangeTabModel, self)._initialize()
        self._addNumberProperty('tabId', 0)
        self._addStringProperty('itemType', '')
        self._addNumberProperty('availableCount', 0)
        self._addNumberProperty('selectedCount', 0)
        self._addBoolProperty('isDone', False)
        self._addBoolProperty('isSelected', False)