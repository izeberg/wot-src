from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.customization_resource.customization_resource_exchange_item_model import CustomizationResourceExchangeItemModel

class CategoryTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(CategoryTooltipViewModel, self).__init__(properties=properties, commands=commands)

    def getItemType(self):
        return self._getString(0)

    def setItemType(self, value):
        self._setString(0, value)

    def getSelectedCount(self):
        return self._getNumber(1)

    def setSelectedCount(self, value):
        self._setNumber(1, value)

    def getOtherCount(self):
        return self._getNumber(2)

    def setOtherCount(self, value):
        self._setNumber(2, value)

    def getItems(self):
        return self._getArray(3)

    def setItems(self, value):
        self._setArray(3, value)

    @staticmethod
    def getItemsType():
        return CustomizationResourceExchangeItemModel

    def _initialize(self):
        super(CategoryTooltipViewModel, self)._initialize()
        self._addStringProperty('itemType', '')
        self._addNumberProperty('selectedCount', 0)
        self._addNumberProperty('otherCount', 0)
        self._addArrayProperty('items', Array())