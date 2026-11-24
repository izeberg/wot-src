from enum import Enum
from frameworks.wulf import Array, ViewModel
from advent_calendar.gui.impl.gen.view_models.views.lobby.components.advent_calendar_events import AdventCalendarEvents
from advent_calendar.gui.impl.gen.view_models.views.lobby.door_view_model import DoorViewModel
from advent_calendar.gui.impl.gen.view_models.views.lobby.progression_rewards_view_model import ProgressionRewardsViewModel

class StatePhase(Enum):
    ACTIVE_PHASE = 'activePhase'
    POST_ACTIVE_PHASE = 'postActivePhase'


class TooltipConstants(Enum):
    NOT_ENOUGH = 'notEnough'
    LOOTBOX = 'lootbox'


class MainViewModel(ViewModel):
    __slots__ = ('onClose', 'onOpenDoorAnimStarted', 'onOpenDoorAnimEnded', 'onShowPurchaseDialog',
                 'onAnimationCompleted', 'onOpenDownloadLink', 'onInfoClick')

    def __init__(self, properties=20, commands=7):
        super(MainViewModel, self).__init__(properties=properties, commands=commands)

    @property
    def progressionRewards(self):
        return self._getViewModel(0)

    @staticmethod
    def getProgressionRewardsType():
        return ProgressionRewardsViewModel

    @property
    def event(self):
        return self._getViewModel(1)

    @staticmethod
    def getEventType():
        return AdventCalendarEvents

    def getStatePhase(self):
        return StatePhase(self._getString(2))

    def setStatePhase(self, value):
        self._setString(2, value.value)

    def getStartTime(self):
        return self._getNumber(3)

    def setStartTime(self, value):
        self._setNumber(3, value)

    def getShowBlur(self):
        return self._getBool(4)

    def setShowBlur(self, value):
        self._setBool(4, value)

    def getPostEventStartDate(self):
        return self._getNumber(5)

    def setPostEventStartDate(self, value):
        self._setNumber(5, value)

    def getPostEventEndDate(self):
        return self._getNumber(6)

    def setPostEventEndDate(self, value):
        self._setNumber(6, value)

    def getDoors(self):
        return self._getArray(7)

    def setDoors(self, value):
        self._setArray(7, value)

    @staticmethod
    def getDoorsType():
        return DoorViewModel

    def getDoorOpenBlocked(self):
        return self._getBool(8)

    def setDoorOpenBlocked(self, value):
        self._setBool(8, value)

    def getCurrencyName(self):
        return self._getString(9)

    def setCurrencyName(self, value):
        self._setString(9, value)

    def getBalanceCurrencyValue(self):
        return self._getNumber(10)

    def setBalanceCurrencyValue(self, value):
        self._setNumber(10, value)

    def getCurrencyIcon(self):
        return self._getString(11)

    def setCurrencyIcon(self, value):
        self._setString(11, value)

    def getIsAnimationEnabled(self):
        return self._getBool(12)

    def setIsAnimationEnabled(self, value):
        self._setBool(12, value)

    def getIsCalendarCompleted(self):
        return self._getBool(13)

    def setIsCalendarCompleted(self, value):
        self._setBool(13, value)

    def getIsIntroScreenVisible(self):
        return self._getBool(14)

    def setIsIntroScreenVisible(self, value):
        self._setBool(14, value)

    def getIsWalletAvailable(self):
        return self._getBool(15)

    def setIsWalletAvailable(self, value):
        self._setBool(15, value)

    def getBalancePluginPath(self):
        return self._getString(16)

    def setBalancePluginPath(self, value):
        self._setString(16, value)

    def getIsBalancePanelVisible(self):
        return self._getBool(17)

    def setIsBalancePanelVisible(self, value):
        self._setBool(17, value)

    def getSubTitle(self):
        return self._getString(18)

    def setSubTitle(self, value):
        self._setString(18, value)

    def getCurrencyTooltipId(self):
        return self._getString(19)

    def setCurrencyTooltipId(self, value):
        self._setString(19, value)

    def _initialize(self):
        super(MainViewModel, self)._initialize()
        self._addViewModelProperty('progressionRewards', ProgressionRewardsViewModel())
        self._addViewModelProperty('event', AdventCalendarEvents())
        self._addStringProperty('statePhase', StatePhase.ACTIVE_PHASE.value)
        self._addNumberProperty('startTime', 0)
        self._addBoolProperty('showBlur', False)
        self._addNumberProperty('postEventStartDate', 0)
        self._addNumberProperty('postEventEndDate', 0)
        self._addArrayProperty('doors', Array())
        self._addBoolProperty('doorOpenBlocked', False)
        self._addStringProperty('currencyName', '')
        self._addNumberProperty('balanceCurrencyValue', 0)
        self._addStringProperty('currencyIcon', '')
        self._addBoolProperty('isAnimationEnabled', False)
        self._addBoolProperty('isCalendarCompleted', False)
        self._addBoolProperty('isIntroScreenVisible', False)
        self._addBoolProperty('isWalletAvailable', True)
        self._addStringProperty('balancePluginPath', '')
        self._addBoolProperty('isBalancePanelVisible', True)
        self._addStringProperty('subTitle', '')
        self._addStringProperty('currencyTooltipId', '')
        self.onClose = self._addCommand('onClose')
        self.onOpenDoorAnimStarted = self._addCommand('onOpenDoorAnimStarted')
        self.onOpenDoorAnimEnded = self._addCommand('onOpenDoorAnimEnded')
        self.onShowPurchaseDialog = self._addCommand('onShowPurchaseDialog')
        self.onAnimationCompleted = self._addCommand('onAnimationCompleted')
        self.onOpenDownloadLink = self._addCommand('onOpenDownloadLink')
        self.onInfoClick = self._addCommand('onInfoClick')