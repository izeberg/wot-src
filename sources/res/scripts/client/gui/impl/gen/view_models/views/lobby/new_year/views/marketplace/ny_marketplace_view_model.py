from enum import Enum
from frameworks.wulf import Array
from gui.impl.gen.view_models.views.lobby.new_year.views.base.ny_scene_rotatable_view import NySceneRotatableView
from gui.impl.gen.view_models.views.lobby.new_year.views.marketplace.card_groups_model import CardGroupsModel
from gui.impl.gen.view_models.views.lobby.new_year.views.marketplace.ny_marketplace_kit_model import NyMarketplaceKitModel

class KitState(Enum):
    RECEIVED = 'received'
    AVAILABLE = 'available'
    UNAVAILABLE = 'unavailable'


class VehicleState(Enum):
    DEFAULT = 'default'
    NOT_IN_INVENTORY = 'notInInventory'
    BROKEN = 'broken'
    IN_BATTLE = 'inBattle'
    IN_UNIT = 'inUnit'
    CUSTOMIZATION_UNAVAILABLE = 'customizationUnavailable'


class NyMarketplaceViewModel(NySceneRotatableView):
    __slots__ = ('onSwitchKit', )

    def __init__(self, properties=12, commands=3):
        super(NyMarketplaceViewModel, self).__init__(properties=properties, commands=commands)

    @property
    def kit(self):
        return self._getViewModel(1)

    @staticmethod
    def getKitType():
        return NyMarketplaceKitModel

    def getCurrentTabName(self):
        return self._getString(2)

    def setCurrentTabName(self, value):
        self._setString(2, value)

    def getCurrentYear(self):
        return self._getString(3)

    def setCurrentYear(self, value):
        self._setString(3, value)

    def getKitState(self):
        return KitState(self._getString(4))

    def setKitState(self, value):
        self._setString(4, value.value)

    def getCurrentKitName(self):
        return self._getString(5)

    def setCurrentKitName(self, value):
        self._setString(5, value)

    def getIsInteractive(self):
        return self._getBool(6)

    def setIsInteractive(self, value):
        self._setBool(6, value)

    def getIsVehicleCustomizationEnabled(self):
        return self._getBool(7)

    def setIsVehicleCustomizationEnabled(self, value):
        self._setBool(7, value)

    def getVehicleState(self):
        return VehicleState(self._getString(8))

    def setVehicleState(self, value):
        self._setString(8, value.value)

    def getCardGroups(self):
        return self._getArray(9)

    def setCardGroups(self, value):
        self._setArray(9, value)

    @staticmethod
    def getCardGroupsType():
        return CardGroupsModel

    def getIsWalletAvailable(self):
        return self._getBool(10)

    def setIsWalletAvailable(self, value):
        self._setBool(10, value)

    def getPrevNYLevel(self):
        return self._getNumber(11)

    def setPrevNYLevel(self, value):
        self._setNumber(11, value)

    def _initialize(self):
        super(NyMarketplaceViewModel, self)._initialize()
        self._addViewModelProperty('kit', NyMarketplaceKitModel())
        self._addStringProperty('currentTabName', 'ny22')
        self._addStringProperty('currentYear', '')
        self._addStringProperty('kitState')
        self._addStringProperty('currentKitName', '')
        self._addBoolProperty('isInteractive', True)
        self._addBoolProperty('isVehicleCustomizationEnabled', True)
        self._addStringProperty('vehicleState')
        self._addArrayProperty('cardGroups', Array())
        self._addBoolProperty('isWalletAvailable', False)
        self._addNumberProperty('prevNYLevel', 0)
        self.onSwitchKit = self._addCommand('onSwitchKit')