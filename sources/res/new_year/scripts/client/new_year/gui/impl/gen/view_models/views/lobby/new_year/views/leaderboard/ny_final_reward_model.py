from gui.impl.wrappers.user_list_model import UserListModel
from gui.impl.gen.view_models.common.vehicle_info_model import VehicleInfoModel
from new_year.gui.impl.gen.view_models.views.lobby.new_year.components.reward_item_model import RewardItemModel

class NyFinalRewardModel(VehicleInfoModel):
    __slots__ = ()

    def __init__(self, properties=14, commands=0):
        super(NyFinalRewardModel, self).__init__(properties=properties, commands=commands)

    @property
    def badges(self):
        return self._getViewModel(10)

    @staticmethod
    def getBadgesType():
        return RewardItemModel

    def getIsRewarded(self):
        return self._getBool(11)

    def setIsRewarded(self, value):
        self._setBool(11, value)

    def getRoleName(self):
        return self._getString(12)

    def setRoleName(self, value):
        self._setString(12, value)

    def getClaimedBadgeIndex(self):
        return self._getNumber(13)

    def setClaimedBadgeIndex(self, value):
        self._setNumber(13, value)

    def _initialize(self):
        super(NyFinalRewardModel, self)._initialize()
        self._addViewModelProperty('badges', UserListModel())
        self._addBoolProperty('isRewarded', False)
        self._addStringProperty('roleName', '')
        self._addNumberProperty('claimedBadgeIndex', -1)