from enum import Enum
from frameworks.wulf import ViewModel

class StatusEnum(Enum):
    ACTIVE = 'active'
    ENDING = 'ending'
    DISABLED = 'disabled'


class CustomizationResourceEntryPointViewModel(ViewModel):
    __slots__ = ('toCustomizationResourceEvent', )

    def __init__(self, properties=4, commands=1):
        super(CustomizationResourceEntryPointViewModel, self).__init__(properties=properties, commands=commands)

    def getIsAloneBanner(self):
        return self._getBool(0)

    def setIsAloneBanner(self, value):
        self._setBool(0, value)

    def getTimer(self):
        return self._getNumber(1)

    def setTimer(self, value):
        self._setNumber(1, value)

    def getStatus(self):
        return StatusEnum(self._getString(2))

    def setStatus(self, value):
        self._setString(2, value.value)

    def getIsLimitsUpdated(self):
        return self._getBool(3)

    def setIsLimitsUpdated(self, value):
        self._setBool(3, value)

    def _initialize(self):
        super(CustomizationResourceEntryPointViewModel, self)._initialize()
        self._addBoolProperty('isAloneBanner', False)
        self._addNumberProperty('timer', 123456789)
        self._addStringProperty('status', StatusEnum.ACTIVE.value)
        self._addBoolProperty('isLimitsUpdated', False)
        self.toCustomizationResourceEvent = self._addCommand('toCustomizationResourceEvent')