from enum import Enum
from frameworks.wulf import ViewModel

class HudDisplay(Enum):
    ALL = 'all'
    NONE = 'none'


class HudViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(HudViewModel, self).__init__(properties=properties, commands=commands)

    def getDisplay(self):
        return HudDisplay(self._getString(0))

    def setDisplay(self, value):
        self._setString(0, value.value)

    def _initialize(self):
        super(HudViewModel, self)._initialize()
        self._addStringProperty('display', HudDisplay.ALL.value)