from frameworks.wulf import ViewModel

class SetupTabTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(SetupTabTooltipViewModel, self).__init__(properties=properties, commands=commands)

    def getName(self):
        return self._getString(0)

    def setName(self, value):
        self._setString(0, value)

    def _initialize(self):
        super(SetupTabTooltipViewModel, self)._initialize()
        self._addStringProperty('name', '')