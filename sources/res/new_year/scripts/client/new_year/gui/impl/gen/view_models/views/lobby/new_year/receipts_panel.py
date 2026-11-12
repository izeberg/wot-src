from enum import IntEnum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from new_year.gui.impl.gen.view_models.views.lobby.new_year.receipt_model import ReceiptModel

class TabId(IntEnum):
    PUBLIC = 0
    SECRET = 1
    HISTORY = 2


class ReceiptsPanel(ViewModel):
    __slots__ = ('onLoadReceipts', 'onSelectTab')

    def __init__(self, properties=7, commands=2):
        super(ReceiptsPanel, self).__init__(properties=properties, commands=commands)

    def getSelectedTab(self):
        return TabId(self._getNumber(0))

    def setSelectedTab(self, value):
        self._setNumber(0, value.value)

    def getItemsAmount(self):
        return self._getNumber(1)

    def setItemsAmount(self, value):
        self._setNumber(1, value)

    def getItemsOffset(self):
        return self._getNumber(2)

    def setItemsOffset(self, value):
        self._setNumber(2, value)

    def getFirstDisabledReceiptIndex(self):
        return self._getNumber(3)

    def setFirstDisabledReceiptIndex(self, value):
        self._setNumber(3, value)

    def getKnownReceipts(self):
        return self._getArray(4)

    def setKnownReceipts(self, value):
        self._setArray(4, value)

    @staticmethod
    def getKnownReceiptsType():
        return ReceiptModel

    def getDiscoveredReceipts(self):
        return self._getArray(5)

    def setDiscoveredReceipts(self, value):
        self._setArray(5, value)

    @staticmethod
    def getDiscoveredReceiptsType():
        return ReceiptModel

    def getReceiptHistory(self):
        return self._getArray(6)

    def setReceiptHistory(self, value):
        self._setArray(6, value)

    @staticmethod
    def getReceiptHistoryType():
        return ReceiptModel

    def _initialize(self):
        super(ReceiptsPanel, self)._initialize()
        self._addNumberProperty('selectedTab', TabId.PUBLIC.value)
        self._addNumberProperty('itemsAmount', 0)
        self._addNumberProperty('itemsOffset', 0)
        self._addNumberProperty('firstDisabledReceiptIndex', -1)
        self._addArrayProperty('knownReceipts', Array())
        self._addArrayProperty('discoveredReceipts', Array())
        self._addArrayProperty('receiptHistory', Array())
        self.onLoadReceipts = self._addCommand('onLoadReceipts')
        self.onSelectTab = self._addCommand('onSelectTab')