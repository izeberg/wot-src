from enum import Enum
from frameworks.wulf import Array, ViewModel
from grinch.gui.impl.gen.view_models.views.battle.grinch_base_capture_model import GrinchBaseCaptureModel
from grinch.gui.impl.gen.view_models.views.battle.grinch_damage_indicator_model import GrinchDamageIndicatorModel
from grinch.gui.impl.gen.view_models.views.battle.grinch_hud.ability_model import AbilityModel
from grinch.gui.impl.gen.view_models.views.battle.grinch_hud.missile_hud_model import MissileHudModel
from grinch.gui.impl.gen.view_models.views.battle.grinch_hud.tank_panel_model import TankPanelModel
from grinch.gui.impl.gen.view_models.views.battle.grinch_marker_model import GrinchMarkerModel
from grinch.gui.impl.gen.view_models.views.battle.team_players_model import TeamPlayersModel
from grinch.gui.impl.gen.view_models.views.battle.team_score_model import TeamScoreModel
from grinch.gui.impl.gen.view_models.views.battle.update_markers_counter_model import UpdateMarkersCounterModel

class AnnouncementIconEnum(Enum):
    NONE = ''
    GIFT = 'gift'
    BIGGIFT = 'bigGift'
    FIRST = 'first'
    SECOND = 'second'
    THIRD = 'third'
    BASES = 'bases'
    SOMEONEISCAPTURING = 'someone_is_capturing'
    YOUARECAPTURING = 'you_are_capturing'
    BASECAPTUREDA = 'base_captured_a'
    BASECAPTUREDB = 'base_captured_b'
    BASECAPTUREDC = 'base_captured_c'


class GrinchHudViewModel(ViewModel):
    __slots__ = ('onMockUpdate', )

    def __init__(self, properties=29, commands=1):
        super(GrinchHudViewModel, self).__init__(properties=properties, commands=commands)

    @property
    def allies(self):
        return self._getViewModel(0)

    @staticmethod
    def getAlliesType():
        return TeamPlayersModel

    @property
    def enemies1(self):
        return self._getViewModel(1)

    @staticmethod
    def getEnemies1Type():
        return TeamPlayersModel

    @property
    def enemies2(self):
        return self._getViewModel(2)

    @staticmethod
    def getEnemies2Type():
        return TeamPlayersModel

    @property
    def tankPanel(self):
        return self._getViewModel(3)

    @staticmethod
    def getTankPanelType():
        return TankPanelModel

    @property
    def missileHud(self):
        return self._getViewModel(4)

    @staticmethod
    def getMissileHudType():
        return MissileHudModel

    @property
    def updateMarkersCounter(self):
        return self._getViewModel(5)

    @staticmethod
    def getUpdateMarkersCounterType():
        return UpdateMarkersCounterModel

    def getIsRespawning(self):
        return self._getBool(6)

    def setIsRespawning(self, value):
        self._setBool(6, value)

    def getIsGameStarting(self):
        return self._getBool(7)

    def setIsGameStarting(self, value):
        self._setBool(7, value)

    def getScoreLimit(self):
        return self._getNumber(8)

    def setScoreLimit(self, value):
        self._setNumber(8, value)

    def getCarryingBigItems(self):
        return self._getNumber(9)

    def setCarryingBigItems(self, value):
        self._setNumber(9, value)

    def getCarryingItems(self):
        return self._getNumber(10)

    def setCarryingItems(self, value):
        self._setNumber(10, value)

    def getItemsLimit(self):
        return self._getNumber(11)

    def setItemsLimit(self, value):
        self._setNumber(11, value)

    def getTeamScore(self):
        return self._getArray(12)

    def setTeamScore(self, value):
        self._setArray(12, value)

    @staticmethod
    def getTeamScoreType():
        return TeamScoreModel

    def getAbilities(self):
        return self._getArray(13)

    def setAbilities(self, value):
        self._setArray(13, value)

    @staticmethod
    def getAbilitiesType():
        return AbilityModel

    def getIsAnnouncementVisible(self):
        return self._getBool(14)

    def setIsAnnouncementVisible(self, value):
        self._setBool(14, value)

    def getAnnouncementCountdownTargetTime(self):
        return self._getReal(15)

    def setAnnouncementCountdownTargetTime(self, value):
        self._setReal(15, value)

    def getAnnouncementHeading(self):
        return self._getString(16)

    def setAnnouncementHeading(self, value):
        self._setString(16, value)

    def getHasHeadingBanner(self):
        return self._getBool(17)

    def setHasHeadingBanner(self, value):
        self._setBool(17, value)

    def getAnnouncementHeadingAbove(self):
        return self._getString(18)

    def setAnnouncementHeadingAbove(self, value):
        self._setString(18, value)

    def getAnnouncementIcon(self):
        return AnnouncementIconEnum(self._getString(19))

    def setAnnouncementIcon(self, value):
        self._setString(19, value.value)

    def getDamageIndicators(self):
        return self._getArray(20)

    def setDamageIndicators(self, value):
        self._setArray(20, value)

    @staticmethod
    def getDamageIndicatorsType():
        return GrinchDamageIndicatorModel

    def getTurretLimit(self):
        return self._getNumber(21)

    def setTurretLimit(self, value):
        self._setNumber(21, value)

    def getDeployedTurrets(self):
        return self._getNumber(22)

    def setDeployedTurrets(self, value):
        self._setNumber(22, value)

    def getTurretsAvailable(self):
        return self._getNumber(23)

    def setTurretsAvailable(self, value):
        self._setNumber(23, value)

    def getTurretStackReloadTimeLeft(self):
        return self._getReal(24)

    def setTurretStackReloadTimeLeft(self, value):
        self._setReal(24, value)

    def getTurretStackReloadTime(self):
        return self._getReal(25)

    def setTurretStackReloadTime(self, value):
        self._setReal(25, value)

    def getBaseMarkers(self):
        return self._getArray(26)

    def setBaseMarkers(self, value):
        self._setArray(26, value)

    @staticmethod
    def getBaseMarkersType():
        return GrinchMarkerModel

    def getBasesCapturing(self):
        return self._getArray(27)

    def setBasesCapturing(self, value):
        self._setArray(27, value)

    @staticmethod
    def getBasesCapturingType():
        return GrinchBaseCaptureModel

    def getShowCapturingBaseIndex(self):
        return self._getNumber(28)

    def setShowCapturingBaseIndex(self, value):
        self._setNumber(28, value)

    def _initialize(self):
        super(GrinchHudViewModel, self)._initialize()
        self._addViewModelProperty('allies', TeamPlayersModel())
        self._addViewModelProperty('enemies1', TeamPlayersModel())
        self._addViewModelProperty('enemies2', TeamPlayersModel())
        self._addViewModelProperty('tankPanel', TankPanelModel())
        self._addViewModelProperty('missileHud', MissileHudModel())
        self._addViewModelProperty('updateMarkersCounter', UpdateMarkersCounterModel())
        self._addBoolProperty('isRespawning', False)
        self._addBoolProperty('isGameStarting', True)
        self._addNumberProperty('scoreLimit', 0)
        self._addNumberProperty('carryingBigItems', 0)
        self._addNumberProperty('carryingItems', 0)
        self._addNumberProperty('itemsLimit', 4)
        self._addArrayProperty('teamScore', Array())
        self._addArrayProperty('abilities', Array())
        self._addBoolProperty('isAnnouncementVisible', False)
        self._addRealProperty('announcementCountdownTargetTime', -1)
        self._addStringProperty('announcementHeading', '')
        self._addBoolProperty('hasHeadingBanner', False)
        self._addStringProperty('announcementHeadingAbove', '')
        self._addStringProperty('announcementIcon', AnnouncementIconEnum.NONE.value)
        self._addArrayProperty('damageIndicators', Array())
        self._addNumberProperty('turretLimit', 0)
        self._addNumberProperty('deployedTurrets', 0)
        self._addNumberProperty('turretsAvailable', -1)
        self._addRealProperty('turretStackReloadTimeLeft', 0.0)
        self._addRealProperty('turretStackReloadTime', 0.0)
        self._addArrayProperty('baseMarkers', Array())
        self._addArrayProperty('basesCapturing', Array())
        self._addNumberProperty('showCapturingBaseIndex', -1)
        self.onMockUpdate = self._addCommand('onMockUpdate')