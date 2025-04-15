from frameworks.wulf import ViewModel

class SortingDropdownTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(SortingDropdownTooltipModel, self).__init__(properties=properties, commands=commands)

    def getShowSortingSelectionWarning(self):
        return self._getBool(0)

    def setShowSortingSelectionWarning(self, value):
        self._setBool(0, value)

    def getIsSortingDisabled(self):
        return self._getBool(1)

    def setIsSortingDisabled(self, value):
        self._setBool(1, value)

    def _initialize(self):
        super(SortingDropdownTooltipModel, self)._initialize()
        self._addBoolProperty('showSortingSelectionWarning', False)
        self._addBoolProperty('isSortingDisabled', False)