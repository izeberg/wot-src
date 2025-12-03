from enum import Enum
from frameworks.wulf import Array, ViewModel

class MenuTriggerHints(Enum):
    GUESTA = 'guestA'
    TOURNAMENT = 'tournament'
    DECORATIONZONES = 'DecorationZones'
    NONE = 'none'


class NyTriggerHintTabsModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(NyTriggerHintTabsModel, self).__init__(properties=properties, commands=commands)

    def getActiveTabs(self):
        return self._getArray(0)

    def setActiveTabs(self, value):
        self._setArray(0, value)

    @staticmethod
    def getActiveTabsType():
        return unicode

    def getTriggerHintType(self):
        return MenuTriggerHints(self._getString(1))

    def setTriggerHintType(self, value):
        self._setString(1, value.value)

    def _initialize(self):
        super(NyTriggerHintTabsModel, self)._initialize()
        self._addArrayProperty('activeTabs', Array())
        self._addStringProperty('triggerHintType')