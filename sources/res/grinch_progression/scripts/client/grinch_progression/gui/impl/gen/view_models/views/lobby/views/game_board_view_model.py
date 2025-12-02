from grinch_progression.gui.impl.gen.view_models.views.lobby.views.enums import HintState
from frameworks.wulf import Array, ViewModel
from grinch_progression.gui.impl.gen.view_models.views.lobby.views.mission_model import MissionModel
from grinch_progression.gui.impl.gen.view_models.views.lobby.views.rewards_model import RewardsModel
from grinch_progression.gui.impl.gen.view_models.views.lobby.views.tank_card_model import TankCardModel

class GameBoardViewModel(ViewModel):
    __slots__ = ('onClaimReward', 'onClose', 'onOpenLobbyMenu', 'onSetHeaderFooterVisibility',
                 'onCompletedMissionShown', 'onChangeTank', 'onShowGameBoardInfo',
                 'onViewLoaded')

    def __init__(self, properties=15, commands=8):
        super(GameBoardViewModel, self).__init__(properties=properties, commands=commands)

    def getSelectedVehicleIntCD(self):
        return self._getNumber(0)

    def setSelectedVehicleIntCD(self, value):
        self._setNumber(0, value)

    def getIsTabSwitching(self):
        return self._getBool(1)

    def setIsTabSwitching(self, value):
        self._setBool(1, value)

    def getEventStartDate(self):
        return self._getNumber(2)

    def setEventStartDate(self, value):
        self._setNumber(2, value)

    def getEventEndDate(self):
        return self._getNumber(3)

    def setEventEndDate(self, value):
        self._setNumber(3, value)

    def getMissionRefreshTime(self):
        return self._getNumber(4)

    def setMissionRefreshTime(self, value):
        self._setNumber(4, value)

    def getPrevPoints(self):
        return self._getNumber(5)

    def setPrevPoints(self, value):
        self._setNumber(5, value)

    def getTankProgression(self):
        return self._getNumber(6)

    def setTankProgression(self, value):
        self._setNumber(6, value)

    def getPoints(self):
        return self._getNumber(7)

    def setPoints(self, value):
        self._setNumber(7, value)

    def getMaxPoints(self):
        return self._getNumber(8)

    def setMaxPoints(self, value):
        self._setNumber(8, value)

    def getIsLastDay(self):
        return self._getBool(9)

    def setIsLastDay(self, value):
        self._setBool(9, value)

    def getMissions(self):
        return self._getArray(10)

    def setMissions(self, value):
        self._setArray(10, value)

    @staticmethod
    def getMissionsType():
        return MissionModel

    def getRewards(self):
        return self._getArray(11)

    def setRewards(self, value):
        self._setArray(11, value)

    @staticmethod
    def getRewardsType():
        return RewardsModel

    def getTankCards(self):
        return self._getArray(12)

    def setTankCards(self, value):
        self._setArray(12, value)

    @staticmethod
    def getTankCardsType():
        return TankCardModel

    def getHintState(self):
        return HintState(self._getString(13))

    def setHintState(self, value):
        self._setString(13, value.value)

    def getIsHintVisible(self):
        return self._getBool(14)

    def setIsHintVisible(self, value):
        self._setBool(14, value)

    def _initialize(self):
        super(GameBoardViewModel, self)._initialize()
        self._addNumberProperty('selectedVehicleIntCD', 0)
        self._addBoolProperty('isTabSwitching', False)
        self._addNumberProperty('eventStartDate', 0)
        self._addNumberProperty('eventEndDate', 0)
        self._addNumberProperty('missionRefreshTime', 0)
        self._addNumberProperty('prevPoints', 0)
        self._addNumberProperty('tankProgression', 0)
        self._addNumberProperty('points', 0)
        self._addNumberProperty('maxPoints', 1000)
        self._addBoolProperty('isLastDay', False)
        self._addArrayProperty('missions', Array())
        self._addArrayProperty('rewards', Array())
        self._addArrayProperty('tankCards', Array())
        self._addStringProperty('hintState', HintState.NONE.value)
        self._addBoolProperty('isHintVisible', False)
        self.onClaimReward = self._addCommand('onClaimReward')
        self.onClose = self._addCommand('onClose')
        self.onOpenLobbyMenu = self._addCommand('onOpenLobbyMenu')
        self.onSetHeaderFooterVisibility = self._addCommand('onSetHeaderFooterVisibility')
        self.onCompletedMissionShown = self._addCommand('onCompletedMissionShown')
        self.onChangeTank = self._addCommand('onChangeTank')
        self.onShowGameBoardInfo = self._addCommand('onShowGameBoardInfo')
        self.onViewLoaded = self._addCommand('onViewLoaded')