from enum import IntEnum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.customization_resource.customization_resource_exchange_item_model import CustomizationResourceExchangeItemModel
from gui.impl.gen.view_models.views.lobby.customization_resource.customization_resource_exchange_tab_model import CustomizationResourceExchangeTabModel

class ExchangeCaptchaState(IntEnum):
    EMPTY = 0
    INVALID = 1
    VALID = 2


class CustomizationResourceMainViewModel(ViewModel):
    __slots__ = ('onTabChange', 'onAdd', 'onReduce', 'onSelectAll', 'changeFilter',
                 'clearFilter', 'onExchange', 'onShowExchangeConfirmation', 'onCloseExchangeConfirmation',
                 'onCaptchaChange', 'onConfirmExchange', 'onShowInfo', 'onClose',
                 'onLoadCards')

    def __init__(self, properties=19, commands=14):
        super(CustomizationResourceMainViewModel, self).__init__(properties=properties, commands=commands)

    def getActiveTabId(self):
        return self._getNumber(0)

    def setActiveTabId(self, value):
        self._setNumber(0, value)

    def getTabs(self):
        return self._getArray(1)

    def setTabs(self, value):
        self._setArray(1, value)

    @staticmethod
    def getTabsType():
        return CustomizationResourceExchangeTabModel

    def getItems(self):
        return self._getArray(2)

    def setItems(self, value):
        self._setArray(2, value)

    @staticmethod
    def getItemsType():
        return CustomizationResourceExchangeItemModel

    def getConfirmationTabs(self):
        return self._getArray(3)

    def setConfirmationTabs(self, value):
        self._setArray(3, value)

    @staticmethod
    def getConfirmationTabsType():
        return CustomizationResourceExchangeTabModel

    def getLimit(self):
        return self._getNumber(4)

    def setLimit(self, value):
        self._setNumber(4, value)

    def getCurrencyCode(self):
        return self._getString(5)

    def setCurrencyCode(self, value):
        self._setString(5, value)

    def getCurrencyBalance(self):
        return self._getNumber(6)

    def setCurrencyBalance(self, value):
        self._setNumber(6, value)

    def getSelectedCount(self):
        return self._getNumber(7)

    def setSelectedCount(self, value):
        self._setNumber(7, value)

    def getIsAllSelected(self):
        return self._getBool(8)

    def setIsAllSelected(self, value):
        self._setBool(8, value)

    def getIsLimitReached(self):
        return self._getBool(9)

    def setIsLimitReached(self, value):
        self._setBool(9, value)

    def getNoAvailableItems(self):
        return self._getBool(10)

    def setNoAvailableItems(self, value):
        self._setBool(10, value)

    def getIsAllItemsHiddenByFilter(self):
        return self._getBool(11)

    def setIsAllItemsHiddenByFilter(self, value):
        self._setBool(11, value)

    def getIsExchangeConfirmationVisible(self):
        return self._getBool(12)

    def setIsExchangeConfirmationVisible(self, value):
        self._setBool(12, value)

    def getExchangeItemsCount(self):
        return self._getNumber(13)

    def setExchangeItemsCount(self, value):
        self._setNumber(13, value)

    def getExchangeReward(self):
        return self._getNumber(14)

    def setExchangeReward(self, value):
        self._setNumber(14, value)

    def getCaptchaState(self):
        return ExchangeCaptchaState(self._getNumber(15))

    def setCaptchaState(self, value):
        self._setNumber(15, value.value)

    def getAllItemsCounter(self):
        return self._getNumber(16)

    def setAllItemsCounter(self, value):
        self._setNumber(16, value)

    def getFilteredItemsCounter(self):
        return self._getNumber(17)

    def setFilteredItemsCounter(self, value):
        self._setNumber(17, value)

    def getIsFilteringActive(self):
        return self._getBool(18)

    def setIsFilteringActive(self, value):
        self._setBool(18, value)

    def _initialize(self):
        super(CustomizationResourceMainViewModel, self)._initialize()
        self._addNumberProperty('activeTabId', -1)
        self._addArrayProperty('tabs', Array())
        self._addArrayProperty('items', Array())
        self._addArrayProperty('confirmationTabs', Array())
        self._addNumberProperty('limit', 0)
        self._addStringProperty('currencyCode', '')
        self._addNumberProperty('currencyBalance', 0)
        self._addNumberProperty('selectedCount', 0)
        self._addBoolProperty('isAllSelected', False)
        self._addBoolProperty('isLimitReached', False)
        self._addBoolProperty('noAvailableItems', False)
        self._addBoolProperty('isAllItemsHiddenByFilter', False)
        self._addBoolProperty('isExchangeConfirmationVisible', False)
        self._addNumberProperty('exchangeItemsCount', 0)
        self._addNumberProperty('exchangeReward', 0)
        self._addNumberProperty('captchaState', ExchangeCaptchaState.EMPTY.value)
        self._addNumberProperty('allItemsCounter', 0)
        self._addNumberProperty('filteredItemsCounter', 0)
        self._addBoolProperty('isFilteringActive', False)
        self.onTabChange = self._addCommand('onTabChange')
        self.onAdd = self._addCommand('onAdd')
        self.onReduce = self._addCommand('onReduce')
        self.onSelectAll = self._addCommand('onSelectAll')
        self.changeFilter = self._addCommand('changeFilter')
        self.clearFilter = self._addCommand('clearFilter')
        self.onExchange = self._addCommand('onExchange')
        self.onShowExchangeConfirmation = self._addCommand('onShowExchangeConfirmation')
        self.onCloseExchangeConfirmation = self._addCommand('onCloseExchangeConfirmation')
        self.onCaptchaChange = self._addCommand('onCaptchaChange')
        self.onConfirmExchange = self._addCommand('onConfirmExchange')
        self.onShowInfo = self._addCommand('onShowInfo')
        self.onClose = self._addCommand('onClose')
        self.onLoadCards = self._addCommand('onLoadCards')