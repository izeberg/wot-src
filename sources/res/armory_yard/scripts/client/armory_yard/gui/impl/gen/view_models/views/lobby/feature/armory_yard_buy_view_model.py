from enum import Enum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.item_bonus_model import ItemBonusModel
from gui.impl.gen.view_models.common.price_model import PriceModel
from armory_yard.gui.impl.gen.view_models.views.lobby.feature.armory_yard_buy_step_config import ArmoryYardBuyStepConfig
from armory_yard.gui.impl.gen.view_models.views.lobby.feature.armory_yard_rewards_vehicle_model import ArmoryYardRewardsVehicleModel

class ParentAlias(Enum):
    MAINVIEW = 'mainView'
    VEHICLEPREVIEW = 'vehiclePreview'


class ArmoryYardBuyViewModel(ViewModel):
    __slots__ = ('onChangeSelectedStep', 'onBuySteps', 'onCancel', 'onBack', 'onShowVehiclePreview',
                 'onShowStylePreview')
    STEP_VEHICLE_TOOLTIP_TYPE = 'stepVehicle'
    FINAL_REWARD_TOOLTIP_TYPE = 'finalReward'
    MERGED_REWARD_TOOLTIP_TYPE = 'mergedReward'
    MAX_VISIBLE_REWARDS = 10

    def __init__(self, properties=12, commands=6):
        super(ArmoryYardBuyViewModel, self).__init__(properties=properties, commands=commands)

    @property
    def finalRewardMain(self):
        return self._getViewModel(0)

    @staticmethod
    def getFinalRewardMainType():
        return ArmoryYardRewardsVehicleModel

    @property
    def finalRewardPostProgression(self):
        return self._getViewModel(1)

    @staticmethod
    def getFinalRewardPostProgressionType():
        return ArmoryYardRewardsVehicleModel

    def getStartStep(self):
        return self._getNumber(2)

    def setStartStep(self, value):
        self._setNumber(2, value)

    def getFinishStep(self):
        return self._getNumber(3)

    def setFinishStep(self, value):
        self._setNumber(3, value)

    def getStepSelected(self):
        return self._getNumber(4)

    def setStepSelected(self, value):
        self._setNumber(4, value)

    def getStepsPassed(self):
        return self._getNumber(5)

    def setStepsPassed(self, value):
        self._setNumber(5, value)

    def getParentAlias(self):
        return ParentAlias(self._getString(6))

    def setParentAlias(self, value):
        self._setString(6, value.value)

    def getRewards(self):
        return self._getArray(7)

    def setRewards(self, value):
        self._setArray(7, value)

    @staticmethod
    def getRewardsType():
        return ItemBonusModel

    def getSteps(self):
        return self._getArray(8)

    def setSteps(self, value):
        self._setArray(8, value)

    @staticmethod
    def getStepsType():
        return ArmoryYardBuyStepConfig

    def getIsWalletAvailable(self):
        return self._getBool(9)

    def setIsWalletAvailable(self, value):
        self._setBool(9, value)

    def getIsBlurEnabled(self):
        return self._getBool(10)

    def setIsBlurEnabled(self, value):
        self._setBool(10, value)

    def getPrices(self):
        return self._getArray(11)

    def setPrices(self, value):
        self._setArray(11, value)

    @staticmethod
    def getPricesType():
        return PriceModel

    def _initialize(self):
        super(ArmoryYardBuyViewModel, self)._initialize()
        self._addViewModelProperty('finalRewardMain', ArmoryYardRewardsVehicleModel())
        self._addViewModelProperty('finalRewardPostProgression', ArmoryYardRewardsVehicleModel())
        self._addNumberProperty('startStep', 0)
        self._addNumberProperty('finishStep', 0)
        self._addNumberProperty('stepSelected', 0)
        self._addNumberProperty('stepsPassed', 0)
        self._addStringProperty('parentAlias')
        self._addArrayProperty('rewards', Array())
        self._addArrayProperty('steps', Array())
        self._addBoolProperty('isWalletAvailable', True)
        self._addBoolProperty('isBlurEnabled', False)
        self._addArrayProperty('prices', Array())
        self.onChangeSelectedStep = self._addCommand('onChangeSelectedStep')
        self.onBuySteps = self._addCommand('onBuySteps')
        self.onCancel = self._addCommand('onCancel')
        self.onBack = self._addCommand('onBack')
        self.onShowVehiclePreview = self._addCommand('onShowVehiclePreview')
        self.onShowStylePreview = self._addCommand('onShowStylePreview')