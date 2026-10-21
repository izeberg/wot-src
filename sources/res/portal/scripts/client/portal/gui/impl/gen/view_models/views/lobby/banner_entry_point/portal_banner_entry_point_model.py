from enum import Enum
from frameworks.wulf import ViewModel

class State(Enum):
    ACTIVE = 'active'
    DISABLED = 'disabled'


class PortalBannerEntryPointModel(ViewModel):
    __slots__ = ('onOpen', 'onShowingAnimationFinish')

    def __init__(self, properties=4, commands=2):
        super(PortalBannerEntryPointModel, self).__init__(properties=properties, commands=commands)

    def getState(self):
        return State(self._getString(0))

    def setState(self, value):
        self._setString(0, value.value)

    def getPerformance(self):
        return self._getNumber(1)

    def setPerformance(self, value):
        self._setNumber(1, value)

    def getIsAnimated(self):
        return self._getBool(2)

    def setIsAnimated(self, value):
        self._setBool(2, value)

    def getTimestamp(self):
        return self._getNumber(3)

    def setTimestamp(self, value):
        self._setNumber(3, value)

    def _initialize(self):
        super(PortalBannerEntryPointModel, self)._initialize()
        self._addStringProperty('state')
        self._addNumberProperty('performance', 0)
        self._addBoolProperty('isAnimated', False)
        self._addNumberProperty('timestamp', 0)
        self.onOpen = self._addCommand('onOpen')
        self.onShowingAnimationFinish = self._addCommand('onShowingAnimationFinish')