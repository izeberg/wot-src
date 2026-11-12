from frameworks.wulf import ViewModel
from gui.impl.wrappers.user_list_model import UserListModel
from new_year.gui.impl.gen.view_models.views.lobby.new_year.components.reward_item_model import RewardItemModel

class NyPetRaidRewardViewModel(ViewModel):
    __slots__ = ('onClose', 'onGoToMachine', 'onGoToLootbox', 'onGotoPet', 'onShowInHangar')

    def __init__(self, properties=4, commands=5):
        super(NyPetRaidRewardViewModel, self).__init__(properties=properties, commands=commands)

    @property
    def rewards(self):
        return self._getViewModel(0)

    @staticmethod
    def getRewardsType():
        return RewardItemModel

    def getIsPetAvailable(self):
        return self._getBool(1)

    def setIsPetAvailable(self, value):
        self._setBool(1, value)

    def getIsMachineAvailable(self):
        return self._getBool(2)

    def setIsMachineAvailable(self, value):
        self._setBool(2, value)

    def getHasVehicle(self):
        return self._getBool(3)

    def setHasVehicle(self, value):
        self._setBool(3, value)

    def _initialize(self):
        super(NyPetRaidRewardViewModel, self)._initialize()
        self._addViewModelProperty('rewards', UserListModel())
        self._addBoolProperty('isPetAvailable', True)
        self._addBoolProperty('isMachineAvailable', True)
        self._addBoolProperty('hasVehicle', False)
        self.onClose = self._addCommand('onClose')
        self.onGoToMachine = self._addCommand('onGoToMachine')
        self.onGoToLootbox = self._addCommand('onGoToLootbox')
        self.onGotoPet = self._addCommand('onGotoPet')
        self.onShowInHangar = self._addCommand('onShowInHangar')