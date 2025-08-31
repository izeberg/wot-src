from enum import Enum
from frameworks.wulf import ViewModel

class State(Enum):
    NONE = 'none'
    NOVEHICLES = 'noVehicles'
    CEASEFIREAVAILABLE = 'ceasefireAvailable'
    CEASEFIREUNAVAILABLE = 'ceasefireUnavailable'
    MODEOFFLINE = 'modeOffline'


class AlertMessageModel(ViewModel):
    __slots__ = ('onClick', )

    def __init__(self, properties=1, commands=1):
        super(AlertMessageModel, self).__init__(properties=properties, commands=commands)

    def getState(self):
        return State(self._getString(0))

    def setState(self, value):
        self._setString(0, value.value)

    def _initialize(self):
        super(AlertMessageModel, self)._initialize()
        self._addStringProperty('state')
        self.onClick = self._addCommand('onClick')