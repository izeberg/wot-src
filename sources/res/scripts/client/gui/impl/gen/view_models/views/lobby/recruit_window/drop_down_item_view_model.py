from frameworks.wulf import ViewModel

class DropDownItemViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(DropDownItemViewModel, self).__init__(properties=properties, commands=commands)

    def getId(self):
        return self._getString(0)

    def setId(self, value):
        self._setString(0, value)

    def getLabel(self):
        return self._getString(1)

    def setLabel(self, value):
        self._setString(1, value)

    def _initialize(self):
        super(DropDownItemViewModel, self)._initialize()
        self._addStringProperty('id', '')
        self._addStringProperty('label', '')