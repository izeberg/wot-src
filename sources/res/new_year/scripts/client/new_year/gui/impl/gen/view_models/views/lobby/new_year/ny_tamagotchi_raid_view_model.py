from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from new_year.gui.impl.gen.view_models.views.lobby.new_year.raid_item_model import RaidItemModel
from new_year.gui.impl.gen.view_models.views.lobby.new_year.receipts_panel import ReceiptsPanel

class NyTamagotchiRaidViewModel(ViewModel):
    __slots__ = ('onOnboardingRestart', 'onRaidStart', 'onUpdateSelected', 'onClose',
                 'onReceiveReward', 'onAccelerationRaid', 'onOpenReceiptsTabs', 'onCloseReceiptsTabs',
                 'onSetOnboardingEnd', 'onRecipiePreview')

    def __init__(self, properties=16, commands=10):
        super(NyTamagotchiRaidViewModel, self).__init__(properties=properties, commands=commands)

    @property
    def receiptsPanel(self):
        return self._getViewModel(0)

    @staticmethod
    def getReceiptsPanelType():
        return ReceiptsPanel

    def getItems(self):
        return self._getArray(1)

    def setItems(self, value):
        self._setArray(1, value)

    @staticmethod
    def getItemsType():
        return RaidItemModel

    def getSelectedItems(self):
        return self._getArray(2)

    def setSelectedItems(self, value):
        self._setArray(2, value)

    @staticmethod
    def getSelectedItemsType():
        return RaidItemModel

    def getTimeLeft(self):
        return self._getNumber(3)

    def setTimeLeft(self, value):
        self._setNumber(3, value)

    def getRemainingTime(self):
        return self._getNumber(4)

    def setRemainingTime(self, value):
        self._setNumber(4, value)

    def getPreviewTime(self):
        return self._getNumber(5)

    def setPreviewTime(self, value):
        self._setNumber(5, value)

    def getIsTamagotchiForRaidReady(self):
        return self._getBool(6)

    def setIsTamagotchiForRaidReady(self, value):
        self._setBool(6, value)

    def getIsHasUnreceivedReward(self):
        return self._getBool(7)

    def setIsHasUnreceivedReward(self, value):
        self._setBool(7, value)

    def getIsBoostMode(self):
        return self._getBool(8)

    def setIsBoostMode(self, value):
        self._setBool(8, value)

    def getIsFirstOnboardingEnter(self):
        return self._getBool(9)

    def setIsFirstOnboardingEnter(self, value):
        self._setBool(9, value)

    def getBoostAmount(self):
        return self._getNumber(10)

    def setBoostAmount(self, value):
        self._setNumber(10, value)

    def getMaxBoostLimit(self):
        return self._getNumber(11)

    def setMaxBoostLimit(self, value):
        self._setNumber(11, value)

    def getBoostTime(self):
        return self._getNumber(12)

    def setBoostTime(self, value):
        self._setNumber(12, value)

    def getIsReceiptsTabsOpened(self):
        return self._getBool(13)

    def setIsReceiptsTabsOpened(self, value):
        self._setBool(13, value)

    def getBoostAccrualTime(self):
        return self._getNumber(14)

    def setBoostAccrualTime(self, value):
        self._setNumber(14, value)

    def getBoostsToAdd(self):
        return self._getNumber(15)

    def setBoostsToAdd(self, value):
        self._setNumber(15, value)

    def _initialize(self):
        super(NyTamagotchiRaidViewModel, self)._initialize()
        self._addViewModelProperty('receiptsPanel', ReceiptsPanel())
        self._addArrayProperty('items', Array())
        self._addArrayProperty('selectedItems', Array())
        self._addNumberProperty('timeLeft', 0)
        self._addNumberProperty('remainingTime', 0)
        self._addNumberProperty('previewTime', 0)
        self._addBoolProperty('isTamagotchiForRaidReady', False)
        self._addBoolProperty('isHasUnreceivedReward', False)
        self._addBoolProperty('isBoostMode', False)
        self._addBoolProperty('isFirstOnboardingEnter', False)
        self._addNumberProperty('boostAmount', 0)
        self._addNumberProperty('maxBoostLimit', 0)
        self._addNumberProperty('boostTime', 0)
        self._addBoolProperty('isReceiptsTabsOpened', False)
        self._addNumberProperty('boostAccrualTime', 0)
        self._addNumberProperty('boostsToAdd', 0)
        self.onOnboardingRestart = self._addCommand('onOnboardingRestart')
        self.onRaidStart = self._addCommand('onRaidStart')
        self.onUpdateSelected = self._addCommand('onUpdateSelected')
        self.onClose = self._addCommand('onClose')
        self.onReceiveReward = self._addCommand('onReceiveReward')
        self.onAccelerationRaid = self._addCommand('onAccelerationRaid')
        self.onOpenReceiptsTabs = self._addCommand('onOpenReceiptsTabs')
        self.onCloseReceiptsTabs = self._addCommand('onCloseReceiptsTabs')
        self.onSetOnboardingEnd = self._addCommand('onSetOnboardingEnd')
        self.onRecipiePreview = self._addCommand('onRecipiePreview')