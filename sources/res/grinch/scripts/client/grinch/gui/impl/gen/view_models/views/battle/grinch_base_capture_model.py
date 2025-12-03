from enum import Enum
from frameworks.wulf import ViewModel
from grinch.gui.impl.gen.view_models.views.battle.grinch_capturable_point_marker_model import GrinchCapturablePointMarkerModel

class BaseNameEnum(Enum):
    A = 'A'
    B = 'B'
    C = 'C'


class TeamColorEnum(Enum):
    YELLOW = 'yellow'
    BLUE = 'blue'
    MAGENTA = 'magenta'
    NEUTRAL = 'neutral'


class GrinchBaseCaptureModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=9, commands=0):
        super(GrinchBaseCaptureModel, self).__init__(properties=properties, commands=commands)

    @property
    def marker(self):
        return self._getViewModel(0)

    @staticmethod
    def getMarkerType():
        return GrinchCapturablePointMarkerModel

    def getName(self):
        return BaseNameEnum(self._getString(1))

    def setName(self, value):
        self._setString(1, value.value)

    def getOwnerTeamColor(self):
        return TeamColorEnum(self._getString(2))

    def setOwnerTeamColor(self, value):
        self._setString(2, value.value)

    def getCapturingTeamColor(self):
        return TeamColorEnum(self._getString(3))

    def setCapturingTeamColor(self, value):
        self._setString(3, value.value)

    def getActivePlayers(self):
        return self._getNumber(4)

    def setActivePlayers(self, value):
        self._setNumber(4, value)

    def getCapturePercentage(self):
        return self._getNumber(5)

    def setCapturePercentage(self, value):
        self._setNumber(5, value)

    def getIsContestedByEnemy(self):
        return self._getBool(6)

    def setIsContestedByEnemy(self, value):
        self._setBool(6, value)

    def getIsContestedByTurret(self):
        return self._getBool(7)

    def setIsContestedByTurret(self, value):
        self._setBool(7, value)

    def getEstSecondsLeft(self):
        return self._getNumber(8)

    def setEstSecondsLeft(self, value):
        self._setNumber(8, value)

    def _initialize(self):
        super(GrinchBaseCaptureModel, self)._initialize()
        self._addViewModelProperty('marker', GrinchCapturablePointMarkerModel())
        self._addStringProperty('name', BaseNameEnum.A.value)
        self._addStringProperty('ownerTeamColor', TeamColorEnum.NEUTRAL.value)
        self._addStringProperty('capturingTeamColor', TeamColorEnum.NEUTRAL.value)
        self._addNumberProperty('activePlayers', 0)
        self._addNumberProperty('capturePercentage', 0)
        self._addBoolProperty('isContestedByEnemy', False)
        self._addBoolProperty('isContestedByTurret', False)
        self._addNumberProperty('estSecondsLeft', -1)