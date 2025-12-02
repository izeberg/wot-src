from enum import Enum
from frameworks.wulf import ViewModel

class MapTypeEnum(Enum):
    GIFTDEFEND = '227_gift_defend'
    LASTGIFTSTANDING = '228_last_gift_standing'


class GrinchHelpViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(GrinchHelpViewModel, self).__init__(properties=properties, commands=commands)

    def getType(self):
        return MapTypeEnum(self._getString(0))

    def setType(self, value):
        self._setString(0, value.value)

    def _initialize(self):
        super(GrinchHelpViewModel, self)._initialize()
        self._addStringProperty('type', MapTypeEnum.GIFTDEFEND.value)