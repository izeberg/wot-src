from frameworks.wulf import Array
from gui.impl.gen.view_models.common.vehicle_info_model import VehicleInfoModel
from gui.impl.gen.view_models.views.lobby.personal_missions.pm3_reward_item_model import Pm3RewardItemModel

class NyVideoRewardViewModel(VehicleInfoModel):
    __slots__ = ('onClose', 'onError', 'onShowVehicle', 'onVideoStarted')

    def __init__(self, properties=17, commands=4):
        super(NyVideoRewardViewModel, self).__init__(properties=properties, commands=commands)

    def getIsWindowAccessible(self):
        return self._getBool(10)

    def setIsWindowAccessible(self, value):
        self._setBool(10, value)

    def getIsFocused(self):
        return self._getBool(11)

    def setIsFocused(self, value):
        self._setBool(11, value)

    def getStage(self):
        return self._getNumber(12)

    def setStage(self, value):
        self._setNumber(12, value)

    def getPosition(self):
        return self._getNumber(13)

    def setPosition(self, value):
        self._setNumber(13, value)

    def getHasExtraRewards(self):
        return self._getBool(14)

    def setHasExtraRewards(self, value):
        self._setBool(14, value)

    def getBadgeTop(self):
        return self._getNumber(15)

    def setBadgeTop(self, value):
        self._setNumber(15, value)

    def getRewards(self):
        return self._getArray(16)

    def setRewards(self, value):
        self._setArray(16, value)

    @staticmethod
    def getRewardsType():
        return Pm3RewardItemModel

    def _initialize(self):
        super(NyVideoRewardViewModel, self)._initialize()
        self._addBoolProperty('isWindowAccessible', True)
        self._addBoolProperty('isFocused', True)
        self._addNumberProperty('stage', 0)
        self._addNumberProperty('position', 0)
        self._addBoolProperty('hasExtraRewards', False)
        self._addNumberProperty('badgeTop', 0)
        self._addArrayProperty('rewards', Array())
        self.onClose = self._addCommand('onClose')
        self.onError = self._addCommand('onError')
        self.onShowVehicle = self._addCommand('onShowVehicle')
        self.onVideoStarted = self._addCommand('onVideoStarted')