from enum import IntEnum
from frameworks.wulf import ViewModel

class OptionalDevicesAssistantPresetTypeEnum(IntEnum):
    COMMON = 0
    LEGENDARY = 1


class OptionalDevicesAssistantPresetModelType(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(OptionalDevicesAssistantPresetModelType, self).__init__(properties=properties, commands=commands)

    def getMType(self):
        return OptionalDevicesAssistantPresetTypeEnum(self._getNumber(0))

    def setMType(self, value):
        self._setNumber(0, value.value)

    def _initialize(self):
        super(OptionalDevicesAssistantPresetModelType, self)._initialize()
        self._addNumberProperty('mType')