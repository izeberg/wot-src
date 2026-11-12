from enum import Enum, IntEnum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.lootboxes.loot_box_entry_point_model import LootBoxEntryPointModel
from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.pet.ny_pet_indicator_model import NyPetIndicatorModel
from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.pet.pet_shop.ny_pet_shop import NyPetShop

class State(Enum):
    UNKNOWN = ''
    SAD = 'sad'
    NORMAL = 'normal'
    FUN = 'fun'
    RAID = 'raid'
    LOOT = 'loot'


class IndicatorType(Enum):
    FOOD = 'food'
    FUN = 'fun'
    ACTIVITY = 'activity'
    RAID = 'raid'


class SingleTipType(IntEnum):
    EMPTY = -1
    FUNOPENED = 2
    ACTIVITYOPENED = 3
    LEADERBOARD = 4
    RAIDAVAILABLE = 5
    RAIDINDICATORLOW = 6


class NyPetModel(ViewModel):
    __slots__ = ('onLootBoxEntryPointClick', 'onOnboardingFinish', 'onOnboardingRestart',
                 'onResetWasOverflowed', 'onProgressFillSound', 'onDeleteItemLeaderboardPoint',
                 'onCloseSingleTip', 'onPetStateAnimationsChange', 'onShopClick',
                 'onRaid', 'onRaidSpeedup', 'onItemClick')

    def __init__(self, properties=27, commands=12):
        super(NyPetModel, self).__init__(properties=properties, commands=commands)

    @property
    def lootBox(self):
        return self._getViewModel(0)

    @staticmethod
    def getLootBoxType():
        return LootBoxEntryPointModel

    @property
    def shop(self):
        return self._getViewModel(1)

    @staticmethod
    def getShopType():
        return NyPetShop

    @property
    def foodIndicator(self):
        return self._getViewModel(2)

    @staticmethod
    def getFoodIndicatorType():
        return NyPetIndicatorModel

    @property
    def funIndicator(self):
        return self._getViewModel(3)

    @staticmethod
    def getFunIndicatorType():
        return NyPetIndicatorModel

    @property
    def activityIndicator(self):
        return self._getViewModel(4)

    @staticmethod
    def getActivityIndicatorType():
        return NyPetIndicatorModel

    def getPetNeeds(self):
        return self._getArray(5)

    def setPetNeeds(self, value):
        self._setArray(5, value)

    @staticmethod
    def getPetNeedsType():
        return IndicatorType

    def getHasPetAnimations(self):
        return self._getBool(6)

    def setHasPetAnimations(self, value):
        self._setBool(6, value)

    def getWasLeaderboardFinished(self):
        return self._getBool(7)

    def setWasLeaderboardFinished(self, value):
        self._setBool(7, value)

    def getIsOnboarding(self):
        return self._getBool(8)

    def setIsOnboarding(self, value):
        self._setBool(8, value)

    def getIsRestartedOnboarding(self):
        return self._getBool(9)

    def setIsRestartedOnboarding(self, value):
        self._setBool(9, value)

    def getSingleTip(self):
        return SingleTipType(self._getNumber(10))

    def setSingleTip(self, value):
        self._setNumber(10, value.value)

    def getNeedToCloseSingleTip(self):
        return self._getBool(11)

    def setNeedToCloseSingleTip(self, value):
        self._setBool(11, value)

    def getIsSingleTipCloseOnOutside(self):
        return self._getBool(12)

    def setIsSingleTipCloseOnOutside(self, value):
        self._setBool(12, value)

    def getIsPopoverOpened(self):
        return self._getBool(13)

    def setIsPopoverOpened(self, value):
        self._setBool(13, value)

    def getIsGuiLootBoxesVisible(self):
        return self._getBool(14)

    def setIsGuiLootBoxesVisible(self, value):
        self._setBool(14, value)

    def getMaxBonus(self):
        return self._getNumber(15)

    def setMaxBonus(self, value):
        self._setNumber(15, value)

    def getCurBonus(self):
        return self._getNumber(16)

    def setCurBonus(self, value):
        self._setNumber(16, value)

    def getState(self):
        return State(self._getString(17))

    def setState(self, value):
        self._setString(17, value.value)

    def getIsRaidReady(self):
        return self._getBool(18)

    def setIsRaidReady(self, value):
        self._setBool(18, value)

    def getRaidRemainingTime(self):
        return self._getNumber(19)

    def setRaidRemainingTime(self, value):
        self._setNumber(19, value)

    def getCanUseRaidSpeedup(self):
        return self._getBool(20)

    def setCanUseRaidSpeedup(self, value):
        self._setBool(20, value)

    def getIsPetRaidEnabled(self):
        return self._getBool(21)

    def setIsPetRaidEnabled(self, value):
        self._setBool(21, value)

    def getBoostAmount(self):
        return self._getNumber(22)

    def setBoostAmount(self, value):
        self._setNumber(22, value)

    def getMaxBoostLimit(self):
        return self._getNumber(23)

    def setMaxBoostLimit(self, value):
        self._setNumber(23, value)

    def getRaidViewEnabled(self):
        return self._getBool(24)

    def setRaidViewEnabled(self, value):
        self._setBool(24, value)

    def getBoostAccrualTime(self):
        return self._getNumber(25)

    def setBoostAccrualTime(self, value):
        self._setNumber(25, value)

    def getBoostsToAdd(self):
        return self._getNumber(26)

    def setBoostsToAdd(self, value):
        self._setNumber(26, value)

    def _initialize(self):
        super(NyPetModel, self)._initialize()
        self._addViewModelProperty('lootBox', LootBoxEntryPointModel())
        self._addViewModelProperty('shop', NyPetShop())
        self._addViewModelProperty('foodIndicator', NyPetIndicatorModel())
        self._addViewModelProperty('funIndicator', NyPetIndicatorModel())
        self._addViewModelProperty('activityIndicator', NyPetIndicatorModel())
        self._addArrayProperty('petNeeds', Array())
        self._addBoolProperty('hasPetAnimations', True)
        self._addBoolProperty('wasLeaderboardFinished', False)
        self._addBoolProperty('isOnboarding', False)
        self._addBoolProperty('isRestartedOnboarding', False)
        self._addNumberProperty('singleTip', SingleTipType.EMPTY.value)
        self._addBoolProperty('needToCloseSingleTip', False)
        self._addBoolProperty('isSingleTipCloseOnOutside', False)
        self._addBoolProperty('isPopoverOpened', False)
        self._addBoolProperty('isGuiLootBoxesVisible', False)
        self._addNumberProperty('maxBonus', 0)
        self._addNumberProperty('curBonus', 0)
        self._addStringProperty('state')
        self._addBoolProperty('isRaidReady', False)
        self._addNumberProperty('raidRemainingTime', 0)
        self._addBoolProperty('canUseRaidSpeedup', False)
        self._addBoolProperty('isPetRaidEnabled', False)
        self._addNumberProperty('boostAmount', 0)
        self._addNumberProperty('maxBoostLimit', 0)
        self._addBoolProperty('raidViewEnabled', False)
        self._addNumberProperty('boostAccrualTime', 0)
        self._addNumberProperty('boostsToAdd', 0)
        self.onLootBoxEntryPointClick = self._addCommand('onLootBoxEntryPointClick')
        self.onOnboardingFinish = self._addCommand('onOnboardingFinish')
        self.onOnboardingRestart = self._addCommand('onOnboardingRestart')
        self.onResetWasOverflowed = self._addCommand('onResetWasOverflowed')
        self.onProgressFillSound = self._addCommand('onProgressFillSound')
        self.onDeleteItemLeaderboardPoint = self._addCommand('onDeleteItemLeaderboardPoint')
        self.onCloseSingleTip = self._addCommand('onCloseSingleTip')
        self.onPetStateAnimationsChange = self._addCommand('onPetStateAnimationsChange')
        self.onShopClick = self._addCommand('onShopClick')
        self.onRaid = self._addCommand('onRaid')
        self.onRaidSpeedup = self._addCommand('onRaidSpeedup')
        self.onItemClick = self._addCommand('onItemClick')