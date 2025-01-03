from enum import Enum
from frameworks.wulf import ViewModel

class HelpTooltipType(Enum):
    TYPE1 = '1'
    TYPE2 = '2'
    TYPE3 = '3'
    TYPE4 = '4'
    TYPE5 = '5'
    TYPE6 = '6'
    TYPE7 = '7'
    TYPE8 = '8'
    TYPE9 = '9'
    TYPE10 = '10'
    TYPE11 = '11'
    TYPE20 = '20'
    TYPE21 = '21'
    TYPE22 = '22'
    TYPE23 = '23'
    TYPE24 = '24'
    TYPE25 = '25'


class PersonalMissionsQuestInfoTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(PersonalMissionsQuestInfoTooltipModel, self).__init__(properties=properties, commands=commands)

    def getType(self):
        return HelpTooltipType(self._getString(0))

    def setType(self, value):
        self._setString(0, value.value)

    def _initialize(self):
        super(PersonalMissionsQuestInfoTooltipModel, self)._initialize()
        self._addStringProperty('type')