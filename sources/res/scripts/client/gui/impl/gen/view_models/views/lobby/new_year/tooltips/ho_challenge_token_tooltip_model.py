from enum import Enum
from frameworks.wulf import ViewModel

class TokenType(Enum):
    MASTERY = 'ho_mastery_challenge_token'
    SIMPLE = 'ho_simple_challenge_token'


class HoChallengeTokenTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(HoChallengeTokenTooltipModel, self).__init__(properties=properties, commands=commands)

    def getTokenType(self):
        return TokenType(self._getString(0))

    def setTokenType(self, value):
        self._setString(0, value.value)

    def getMissionsAmount(self):
        return self._getNumber(1)

    def setMissionsAmount(self, value):
        self._setNumber(1, value)

    def _initialize(self):
        super(HoChallengeTokenTooltipModel, self)._initialize()
        self._addStringProperty('tokenType')
        self._addNumberProperty('missionsAmount', 0)