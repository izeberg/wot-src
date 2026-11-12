from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui_lootboxes.gui.impl.gen.view_models.views.lobby.gui_lootboxes.reward_video_model import RewardVideoModel
from gui_lootboxes.gui.impl.gen.view_models.views.lobby.gui_lootboxes.vehicle_bonus_model import VehicleBonusModel

class LootboxOpenBySelectionViewModel(ViewModel):
    __slots__ = ('onCardSelect', 'onSkip', 'onAnimationFinished', 'onClose', 'onVideoStarted',
                 'onVideoEnded', 'onPreview')

    def __init__(self, properties=8, commands=7):
        super(LootboxOpenBySelectionViewModel, self).__init__(properties=properties, commands=commands)

    def getCards(self):
        return self._getArray(0)

    def setCards(self, value):
        self._setArray(0, value)

    @staticmethod
    def getCardsType():
        return int

    def getIsLoading(self):
        return self._getBool(1)

    def setIsLoading(self, value):
        self._setBool(1, value)

    def getRewards(self):
        return self._getArray(2)

    def setRewards(self, value):
        self._setArray(2, value)

    @staticmethod
    def getRewardsType():
        return VehicleBonusModel

    def getRewardVideos(self):
        return self._getArray(3)

    def setRewardVideos(self, value):
        self._setArray(3, value)

    @staticmethod
    def getRewardVideosType():
        return RewardVideoModel

    def getIsWindowAccessible(self):
        return self._getBool(4)

    def setIsWindowAccessible(self, value):
        self._setBool(4, value)

    def getIsGuaranteedReward(self):
        return self._getBool(5)

    def setIsGuaranteedReward(self, value):
        self._setBool(5, value)

    def getHasVideoFooter(self):
        return self._getBool(6)

    def setHasVideoFooter(self, value):
        self._setBool(6, value)

    def getLootBoxIconName(self):
        return self._getString(7)

    def setLootBoxIconName(self, value):
        self._setString(7, value)

    def _initialize(self):
        super(LootboxOpenBySelectionViewModel, self)._initialize()
        self._addArrayProperty('cards', Array())
        self._addBoolProperty('isLoading', False)
        self._addArrayProperty('rewards', Array())
        self._addArrayProperty('rewardVideos', Array())
        self._addBoolProperty('isWindowAccessible', True)
        self._addBoolProperty('isGuaranteedReward', False)
        self._addBoolProperty('hasVideoFooter', False)
        self._addStringProperty('lootBoxIconName', '')
        self.onCardSelect = self._addCommand('onCardSelect')
        self.onSkip = self._addCommand('onSkip')
        self.onAnimationFinished = self._addCommand('onAnimationFinished')
        self.onClose = self._addCommand('onClose')
        self.onVideoStarted = self._addCommand('onVideoStarted')
        self.onVideoEnded = self._addCommand('onVideoEnded')
        self.onPreview = self._addCommand('onPreview')