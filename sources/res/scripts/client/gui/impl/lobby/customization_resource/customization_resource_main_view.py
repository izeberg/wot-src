import BigWorld, logging
from account_helpers import AccountSettings
from account_helpers.AccountSettings import SHOWN_CUSTOMIZATION_RESOURCE_INTRO
from adisp import adisp_process
from frameworks.wulf import ViewFlags, ViewSettings, WindowFlags
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.Scaleform.Waiting import Waiting
from gui.impl.backport import createTooltipData
from gui.shared.gui_items.customization import CustomizationTooltipContext
from gui.customization_resource.customization_resource_exchange import CustomizationResourceExchangeProcessor
from gui.customization_resource import customization_resource_notifications as notifications
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.customization_resource.customization_resource_exchange_item_model import CustomizationResourceExchangeItemModel
from gui.impl.gen.view_models.views.lobby.customization_resource.customization_resource_exchange_tab_model import CustomizationResourceExchangeTabModel
from gui.impl.gen.view_models.views.lobby.customization_resource.customization_resource_main_view_model import CustomizationResourceMainViewModel
from gui.impl.gui_decorators import args2params
from gui.impl.lobby.common.view_wrappers import createBackportTooltipDecorator
from gui.impl.lobby.customization_resource.customization_resource_exchange_confirmation import ExchangeCaptchaState, buildConfirmationSummary, getCaptchaState
from gui.impl.lobby.customization_resource.customization_resource_exchange_data_provider import CustomizationResourceExchangeDataProvider
from gui.impl.lobby.customization_resource.customization_resource_exchange_filters import CustomizationResourceExchangeFilters
from gui.impl.lobby.customization_resource.customization_resource_exchange_selection import CustomizationResourceExchangeSelection
from gui.impl.lobby.customization_resource.dialogs import showCustomizationResourceExitConfirmDialog
from gui.impl.lobby.customization_resource.shared import CustomizationTabs, getTabItemTypeName, splitByChunks, mergeResults, closeWindowHandler
from gui.impl.lobby.customization_resource.tooltips.category_tooltip_view import CategoryTooltipView
from gui.impl.lobby.customization_resource.tooltips.customization_resource_currency_tooltip_view import CustomizationResourceCurrencyTooltipView
from gui.impl.pub import ViewImpl
from gui.impl.pub.lobby_window import LobbyWindow
from gui.shared.event_dispatcher import showCustomizationResourceFilterPopoverWindow, showCustomizationResourceVideoRewardWindow, showCustomizationResourceRewardWindow, showCustomizationResourceIntroPageWindow
from helpers import dependency
from skeletons.gui.game_control import ICustomizationResourceController
from skeletons.gui.shared import IItemsCache
from th_async import th_async, th_await
_logger = logging.getLogger(__name__)

class CustomizationResourceMainView(ViewImpl):
    __customizationResourceController = dependency.descriptor(ICustomizationResourceController)
    __itemsCache = dependency.descriptor(IItemsCache)
    __slots__ = ('__activeTabId', '__captchaState', '__captchaTarget', '__dataProvider',
                 '__exchangeCategoryMap', '__exchangePending', '__isExchangeConfirmationVisible',
                 '__selection', '__filters')

    def __init__(self, layoutID):
        settings = ViewSettings(layoutID)
        settings.flags = ViewFlags.VIEW
        settings.model = CustomizationResourceMainViewModel()
        super(CustomizationResourceMainView, self).__init__(settings)
        self.__activeTabId = CustomizationTabs.DEFAULT
        self.__captchaState = ExchangeCaptchaState.EMPTY
        self.__captchaTarget = 0
        self.__dataProvider = None
        self.__exchangeCategoryMap = {}
        self.__exchangePending = False
        self.__isExchangeConfirmationVisible = False
        self.__selection = CustomizationResourceExchangeSelection()
        self.__filters = CustomizationResourceExchangeFilters()
        return

    @property
    def viewModel(self):
        return super(CustomizationResourceMainView, self).getViewModel()

    def createPopOver(self, event):
        if event.contentID == R.views.lobby.customization_resource.CustomizationResourceFilterPopoverView():
            return showCustomizationResourceFilterPopoverWindow(event, self.__activeTabId, self.__filters, self.__dataProvider, self.getParentWindow())
        return super(CustomizationResourceMainView, self).createPopOver(event)

    def _onLoading(self, *args, **kwargs):
        super(CustomizationResourceMainView, self)._onLoading(*args, **kwargs)
        BigWorld.worldDrawEnabled(False)
        self.__dataProvider = CustomizationResourceExchangeDataProvider(self.__customizationResourceController.config.blacklist, self.__customizationResourceController.config.priceGroups)
        self.__activeTabId = self.__dataProvider.getFirstNonEmptyTab()
        self.__updateViewModel()

    def _onLoaded(self, *args, **kwargs):
        super(CustomizationResourceMainView, self)._onLoaded(*args, **kwargs)
        if not AccountSettings.getSettings(SHOWN_CUSTOMIZATION_RESOURCE_INTRO):
            showCustomizationResourceIntroPageWindow(parent=self.getWindow())

    def _getEvents(self):
        return (
         (
          self.viewModel.onTabChange, self.__onTabChange),
         (
          self.viewModel.onAdd, self.__onAdd),
         (
          self.viewModel.onReduce, self.__onReduce),
         (
          self.viewModel.onSelectAll, self.__onSelectAll),
         (
          self.viewModel.onExchange, self.__onShowExchangeConfirmation),
         (
          self.viewModel.onShowExchangeConfirmation, self.__onShowExchangeConfirmation),
         (
          self.viewModel.onCloseExchangeConfirmation, self.__onCloseExchangeConfirmation),
         (
          self.viewModel.onCaptchaChange, self.__onCaptchaChange),
         (
          self.viewModel.onConfirmExchange, self.__onConfirmExchange),
         (
          self.viewModel.onShowInfo, self.__onShowInfo),
         (
          self.viewModel.onClose, self.__onClose),
         (
          self.viewModel.onLoadCards, self.__onLoadCards),
         (
          self.viewModel.clearFilter, self.__onClearFilter),
         (
          self.__itemsCache.onSyncCompleted, self.__onItemsSyncCompleted),
         (
          self.__customizationResourceController.onEventSettingsUpdated, self.__onEventSettingsUpdated))

    def _finalize(self):
        self.__resetExchangeConfirmation()
        self.__selection.clear()
        self.__dataProvider = None
        BigWorld.worldDrawEnabled(True)
        super(CustomizationResourceMainView, self)._finalize()
        return

    @createBackportTooltipDecorator()
    def createToolTip(self, event):
        return super(CustomizationResourceMainView, self).createToolTip(event)

    def getTooltipData(self, event):
        tooltipId = event.getArgument('tooltip')
        if not tooltipId:
            return
        else:
            if tooltipId == TOOLTIPS_CONSTANTS.TECH_CUSTOMIZATION_ITEM:
                args = CustomizationTooltipContext(itemCD=int(event.getArgument('intCD')))
            else:
                args = None
            return createTooltipData(isSpecial=True, specialAlias=tooltipId, specialArgs=args)

    def createToolTipContent(self, event, contentID):
        if contentID == R.views.lobby.customization_resource.tooltips.CustomizationResourceCurrencyTooltipView():
            return CustomizationResourceCurrencyTooltipView()
        else:
            if contentID == R.views.lobby.customization_resource.tooltips.CategoryTooltipView():
                tabIdValue = event.getArgument('tabId')
                if tabIdValue is None:
                    return
                tabId = int(tabIdValue)
                if tabId not in self.__dataProvider.getTabs():
                    return
                activeItems = self.__dataProvider.getItems(tabId)
                return CategoryTooltipView(activeItems, self.__selection, tabId)
            return super(CustomizationResourceMainView, self).createToolTipContent(event, contentID)

    def __onTabChange(self, args):
        tabId = int(args.get('tabId', CustomizationTabs.DEFAULT))
        if tabId not in self.__dataProvider.getTabs():
            return
        self.__activeTabId = tabId
        self.__updateViewModel()

    def __onAdd(self, args):
        item = self.__getItemFromArgs(args)
        if item is None:
            return
        else:
            self.__selection.add(item)
            self.__updateViewModel()
            return

    def __onReduce(self, args):
        item = self.__getItemFromArgs(args)
        if item is None:
            return
        else:
            self.__selection.reduce(item)
            self.__updateViewModel()
            return

    def __onSelectAll(self):
        items = self.__dataProvider.getItems(self.__activeTabId)
        limit = self.__customizationResourceController.config.customizationExchangeLimit
        if not items:
            return
        totalSelected = self.__selection.getTotalCount()
        selectedOnTab = self.__selection.getSelectedCountForTab(items)
        selectedOutsideTab = totalSelected - selectedOnTab
        maxSelectableOnTab = max(0, limit - selectedOutsideTab)
        totalAvailableOnTab = sum(item.availableCount for item in items)
        targetSelectedOnTab = min(totalAvailableOnTab, maxSelectableOnTab)
        if selectedOnTab == targetSelectedOnTab:
            self.__selection.deselectAll((item, 0) for item in items)
            self.__updateViewModel()
            return
        remainingToAdd = targetSelectedOnTab - selectedOnTab
        itemsToUpdate = []
        for item in items:
            currentSelected = self.__selection.getSelectedCount(item)
            availableToAdd = item.availableCount - currentSelected
            if remainingToAdd > 0 and availableToAdd > 0:
                addCount = min(availableToAdd, remainingToAdd)
                newCount = currentSelected + addCount
                remainingToAdd -= addCount
            else:
                newCount = currentSelected
            itemsToUpdate.append((item, newCount))

        self.__selection.setSelectedCounts(itemsToUpdate)
        self.__updateViewModel()

    def updateFilterState(self):
        self.__updateViewModel()

    def __onClearFilter(self):
        self.__filters.clear()
        self.__updateViewModel()

    def __onShowExchangeConfirmation(self):
        summary = buildConfirmationSummary(self.__dataProvider, self.__selection)
        if summary.itemsCount <= 0:
            return
        self.__isExchangeConfirmationVisible = True
        self.__captchaState = ExchangeCaptchaState.EMPTY
        self.__captchaTarget = summary.itemsCount
        self.__updateViewModel()

    def __onCloseExchangeConfirmation(self):
        self.__resetExchangeConfirmation()
        self.__updateViewModel()

    def __onCaptchaChange(self, args):
        if not self.__isExchangeConfirmationVisible:
            return
        else:
            value = args.get('value') if args else None
            self.__captchaState = getCaptchaState(value, self.__captchaTarget)
            self.__updateViewModel()
            return

    @adisp_process
    def __onConfirmExchange(self):
        if not self.__isExchangeConfirmationVisible or self.__captchaState != ExchangeCaptchaState.VALID or self.__exchangePending:
            return
        summary = buildConfirmationSummary(self.__dataProvider, self.__selection)
        if summary.itemsCount != self.__captchaTarget:
            self.__captchaState = ExchangeCaptchaState.EMPTY
            self.__captchaTarget = summary.itemsCount
            self.__updateViewModel()
            return
        payload = self.__selection.getPayload()
        if not payload:
            return
        self.__exchangeCategoryMap = self.__dataProvider.getCategoryMap(payload)
        self.__exchangePending = True
        notifications.markExchangePending()
        allResults = []
        Waiting.show('loading')
        for payloadBatch in splitByChunks(payload, self.__customizationResourceController.config.batchLimit):
            processor = CustomizationResourceExchangeProcessor(payloadBatch)
            result = yield processor.request()
            allResults.append(result)

        result = mergeResults(allResults)
        self.__onExchangeResponse(result)

    def __onExchangeResponse(self, result):
        notifications.clearExchangePending()
        categoryMap = self.__exchangeCategoryMap
        self.__exchangeCategoryMap = {}
        if not result.get('success'):
            notifications.pushExchangeError()
            if Waiting.isOpened('loading'):
                Waiting.hide('loading')
            return
        categoryCounts = notifications.getCategoryCounts(result['items'], categoryMap)
        currencyCode = self.__customizationResourceController.getCurrencyCode()
        notifications.pushExchangeSuccess(categoryCounts, result['reward']['currencies'][currencyCode]['count'])
        showCustomizationResourceVideoRewardWindow(closeCallback=lambda : showCustomizationResourceRewardWindow(rewards=result['reward']))

    def __onShowInfo(self):
        if not self.__customizationResourceController.isExchangeEnabled() or not self.__customizationResourceController.isEnabled():
            self.__closeByKillSwitch()
            return
        showCustomizationResourceIntroPageWindow(parent=self.getWindow())

    @th_async()
    def __onClose(self):
        if self.__isExchangeConfirmationVisible:
            self.__onCloseExchangeConfirmation()
            return
        shouldClose = self.__selection.isEmpty()
        if not shouldClose:
            shouldClose = yield th_await(showCustomizationResourceExitConfirmDialog())
        if shouldClose:
            self.__selection.clear()
            self.destroyWindow()

    def __onItemsSyncCompleted(self, *_):
        if not self.__exchangePending:
            self.__dataProvider.rebuild()
            self.__selection.reconcile(self.__dataProvider)
            if self.__activeTabId not in self.__dataProvider.getTabs():
                self.__activeTabId = self.__dataProvider.getFirstNonEmptyTab()
            if self.__isExchangeConfirmationVisible:
                summary = buildConfirmationSummary(self.__dataProvider, self.__selection)
                if summary.itemsCount <= 0:
                    self.__resetExchangeConfirmation()
                elif summary.itemsCount != self.__captchaTarget:
                    self.__captchaState = ExchangeCaptchaState.EMPTY
                    self.__captchaTarget = summary.itemsCount
            self.__updateViewModel()

    def __onEventSettingsUpdated(self):
        if not self.__customizationResourceController.isExchangeEnabled() or not self.__customizationResourceController.isEnabled():
            self.__closeByKillSwitch()
            return
        config = self.__customizationResourceController.config
        self.__dataProvider.updateConfig(config.priceGroups, config.blacklist)
        self.__selection.reconcile(self.__dataProvider)
        if self.__activeTabId not in self.__dataProvider.getTabs():
            self.__activeTabId = self.__dataProvider.getFirstNonEmptyTab()
        self.__updateViewModel()

    def __closeByKillSwitch(self):
        self.__selection.clear()
        closeWindowHandler(self)

    def __updateViewModel(self):
        activeItems = self.__dataProvider.getItems(self.__activeTabId)
        confirmationSummary = buildConfirmationSummary(self.__dataProvider, self.__selection)
        visibleItems = self.__filters.apply(activeItems, self.__activeTabId)
        groups = self.__filters.getGroups(activeItems, self.__activeTabId)
        selectedCount = self.__selection.getTotalCount()
        customizationExchangeLimit = self.__customizationResourceController.config.customizationExchangeLimit
        with self.viewModel.transaction() as (tx):
            tx.setActiveTabId(self.__activeTabId)
            tx.setLimit(customizationExchangeLimit)
            tx.setNoAvailableItems(all(item.availableCount == 0 for item in activeItems))
            tx.setIsLimitReached(selectedCount == customizationExchangeLimit)
            tx.setCurrencyCode(self.__customizationResourceController.getCurrencyCode())
            tx.setCurrencyBalance(self.__customizationResourceController.getCurrencyBalance())
            tx.setSelectedCount(selectedCount)
            tx.setIsExchangeConfirmationVisible(self.__isExchangeConfirmationVisible)
            tx.setExchangeItemsCount(confirmationSummary.itemsCount)
            tx.setExchangeReward(confirmationSummary.reward)
            tx.setCaptchaState(self.__captchaState)
            tx.setIsAllSelected(self.__selection.isAllSelectedWithLimit(activeItems, customizationExchangeLimit))
            tx.setAllItemsCounter(len(activeItems))
            tx.setFilteredItemsCounter(len(visibleItems))
            tx.setIsAllItemsHiddenByFilter(not any(visibleItems) and self.__filters.isAnyFiltersApplied())
            tx.setIsFilteringActive(self.__filters.hasAppliedFilter(self.__activeTabId, groups))
            self.__fillTabs(tx)
            self.__fillConfirmationTabs(tx, confirmationSummary.tabs)
            self.__updateItems(tx, visibleItems)

    def __getVisibleItems(self):
        items = self.__dataProvider.getItems(self.__activeTabId)
        return self.__filters.apply(items, self.__activeTabId)

    def __fillTabs(self, model):
        tabsModel = model.getTabs()
        tabsModel.clear()
        for tabId in self.__dataProvider.getTabs():
            items = self.__dataProvider.getItems(tabId)
            totalCount = self.__dataProvider.getTotalCount(tabId)
            selectedCount = self.__selection.getSelectedCountForTab(items)
            tabModel = CustomizationResourceExchangeTabModel()
            tabModel.setTabId(tabId)
            tabModel.setItemType(getTabItemTypeName(tabId))
            tabModel.setAvailableCount(totalCount)
            tabModel.setSelectedCount(selectedCount)
            tabModel.setIsDone(totalCount > 0 and selectedCount == totalCount)
            tabModel.setIsSelected(tabId == self.__activeTabId)
            tabsModel.addViewModel(tabModel)

        tabsModel.invalidate()

    @staticmethod
    def __fillConfirmationTabs(model, tabs):
        tabsModel = model.getConfirmationTabs()
        tabsModel.clear()
        for tab in tabs:
            tabModel = CustomizationResourceExchangeTabModel()
            tabModel.setTabId(tab.tabId)
            tabModel.setItemType(getTabItemTypeName(tab.tabId))
            tabModel.setSelectedCount(tab.selectedCount)
            tabsModel.addViewModel(tabModel)

        tabsModel.invalidate()

    def __fillItem(self, item, itemModel):
        itemModel.setVehicleCD(item.vehicleCD)
        itemModel.setName(item.name)
        itemModel.setIcon(item.icon)
        itemModel.setVehicleName(item.vehicleName)
        itemModel.setInventoryCount(item.inventoryCount)
        itemModel.setInstalledCount(item.installedCount)
        itemModel.setAvailableCount(item.availableCount)
        itemModel.setSelectedCount(self.__selection.getSelectedCount(item))
        itemModel.setIsWide(item.isWide)
        itemModel.setExchangePrice(item.exchangePrice)

    def __fillItems(self, model, items):
        itemsModel = model.getItems()
        itemsModel.clear()
        for item in items:
            itemModel = CustomizationResourceExchangeItemModel()
            itemModel.setIntCD(item.intCD)
            itemsModel.addViewModel(itemModel)

        itemsModel.invalidate()

    def __updateItems(self, model, items):
        itemsModel = model.getItems()
        if not self.__hasSameItems(itemsModel, items):
            self.__fillItems(model, items)
            return
        needInvalidate = False
        for index, item in enumerate(items):
            itemModel = itemsModel.getValue(index)
            selectedCount = self.__selection.getSelectedCount(item)
            if itemModel.getSelectedCount() != selectedCount:
                self.__fillItem(item, itemModel)
                itemsModel.setViewModel(index, itemModel)
                needInvalidate = True

        if needInvalidate:
            itemsModel.invalidate()

    @staticmethod
    def __hasSameItems(itemsModel, items):
        if len(itemsModel) != len(items):
            return False
        for index, item in enumerate(items):
            if itemsModel.getValue(index).getIntCD() != item.intCD:
                return False

        return True

    def __updateItemsInRange(self, startIndex, endIndex):
        activeItems = self.__dataProvider.getItems(self.__activeTabId)
        visibleItems = self.__filters.apply(activeItems, self.__activeTabId)[startIndex:endIndex + 1]
        if not visibleItems:
            return
        with self.viewModel.transaction() as (model):
            needInvalidate = False
            itemsModel = model.getItems()
            itemsLength = len(itemsModel)
            for index, item in enumerate(visibleItems):
                actualIndex = startIndex + index
                if actualIndex >= itemsLength:
                    break
                itemModel = itemsModel.getValue(actualIndex)
                if not itemModel.getIsFilled():
                    self.__fillItem(item, itemModel)
                    itemModel.setIsFilled(True)
                    itemModel.setTooltip(TOOLTIPS_CONSTANTS.TECH_CUSTOMIZATION_ITEM)
                    itemsModel.setViewModel(actualIndex, itemModel)
                    needInvalidate = True

            if needInvalidate:
                itemsModel.invalidate()

    def __resetExchangeConfirmation(self):
        self.__isExchangeConfirmationVisible = False
        self.__captchaState = ExchangeCaptchaState.EMPTY
        self.__captchaTarget = 0

    def __getItemFromArgs(self, args):
        key = (
         int(args.get('intCD', 0)), int(args.get('vehicleCD', 0)))
        return self.__dataProvider.getItem(key)

    @args2params(int, int)
    def __onLoadCards(self, startIndex, endIndex):
        self.__updateItemsInRange(startIndex, endIndex)


class CustomizationResourceMainViewWindow(LobbyWindow):
    __slots__ = ()

    def __init__(self, parent=None):
        super(CustomizationResourceMainViewWindow, self).__init__(WindowFlags.WINDOW | WindowFlags.WINDOW_FULLSCREEN, content=CustomizationResourceMainView(R.views.lobby.customization_resource.CustomizationResourceMainView()), parent=parent)