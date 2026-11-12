from itertools import islice
from new_year.gui.impl.gen.view_models.views.lobby.new_year.receipt_model import ReceiptState
from new_year.gui.impl.gen.view_models.views.lobby.new_year.receipts_panel import TabId
from new_year_common.items.components.ny_constants import RaidState
from new_year.helpers.ny_helpers import collectRaidReservedResources, isRaidComponentEnabled, subtractRaidReservedResources
_TAB_CONFIG = {TabId.PUBLIC: ('public', 'getKnownReceipts'), 
   TabId.SECRET: ('secret', 'getDiscoveredReceipts')}
DEFAULT_FIRST_DISABLED_INDEX = -1

def getTabData(tab, raidMetaData, viewModel):
    disclosedReceipts = raidMetaData.get('disclosedReceipts', {})
    receiptLimits = raidMetaData.get('receiptLimits', {})
    if tab == TabId.HISTORY:
        return _buildHistoryTabData(raidMetaData, disclosedReceipts, receiptLimits, viewModel)
    else:
        config = _TAB_CONFIG.get(tab)
        if config is None:
            return
        sourceKey, modelGetter = config
        return _buildReceiptTabData(disclosedReceipts, receiptLimits, viewModel, sourceKey, modelGetter)


def _buildHistoryTabData(raidMetaData, disclosedReceipts, receiptLimits, viewModel):
    return {'raidStatistics': raidMetaData.get('raidStatistics', {}), 
       'disclosedReceipts': disclosedReceipts, 
       'receiptLimits': receiptLimits, 
       'model': viewModel.receiptsPanel.getReceiptHistory()}


def _buildReceiptTabData(disclosedReceipts, receiptLimits, viewModel, sourceKey, modelGetter):
    return {'receipts': disclosedReceipts.get(sourceKey, {}), 
       'receiptLimits': receiptLimits, 
       'model': getattr(viewModel.receiptsPanel, modelGetter)()}


def prepareReceiptStates(receipts, receiptLimits, isRaidReady, raidState, componentsConfig):
    for receiptId, receiptData in receipts.iteritems():
        if receiptData.get('hidden', False):
            continue
        slotIDs = receiptData.get('slots', ())
        limit = receiptData.get('limit')
        usageCount = receiptLimits.get(receiptId, 0)
        receiptData['state'] = calcReceiptState(isRaidReady, raidState, slotIDs, limit, usageCount, componentsConfig)


def calcReceiptState(isRaidReady, raidState, slotIDs, limit, usageCount, componentsConfig):
    if not isRaidReady:
        return ReceiptState.TAMAGOTCHI_STATS
    else:
        if not slotIDs:
            return ReceiptState.AVAILABLE
        if limit is not None and usageCount >= limit:
            return ReceiptState.LIMIT_REACHED
        if not hasEnoughResourcesForComponents(componentsConfig, slotIDs):
            return ReceiptState.NOT_ENOUGH_RESOURCES
        if raidState != RaidState.NOT_ACTIVE:
            return ReceiptState.TAMAGOTCHI_RAID
        return ReceiptState.AVAILABLE


def hasEnoughResourcesForComponents(componentsConfig, selectedIDs):
    reservedResources = collectRaidReservedResources(componentsConfig, selectedIDs)
    for componentId in selectedIDs:
        componentData = componentsConfig.get(componentId)
        if componentData is None:
            return False
        bonus = componentData.get('bonus', componentData)
        availableReservedResources = dict(reservedResources)
        subtractRaidReservedResources(availableReservedResources, bonus)
        if not isRaidComponentEnabled(bonus, reservedResources=availableReservedResources):
            return False

    return True


def getReceiptSortKey(item):
    receiptId, receiptData = item
    state = receiptData.get('state')
    if receiptData.get('disabled', False):
        priority = 2
    elif state in (ReceiptState.AVAILABLE, ReceiptState.TAMAGOTCHI_RAID):
        priority = 0
    else:
        priority = 1
    return (priority, -receiptData.get('weight', 0.0), receiptId)


def getVisibleReceipts(currentTab, receiptData, offset, limit):
    totalItems = receiptData.get('totalItems', 0)
    startIdx, endIdx = offset, min(offset + limit, totalItems)
    items = list(islice(_getReceiptIterator(currentTab, receiptData), startIdx, endIdx))
    return (items, endIdx)


def getFirstDisabledIndex(items, currentTab):
    for index, receiptItem in enumerate(items):
        if currentTab == TabId.HISTORY:
            receiptDataItem = receiptItem
        else:
            _, receiptDataItem = receiptItem
        if receiptDataItem.get('state') not in (ReceiptState.AVAILABLE, ReceiptState.TAMAGOTCHI_RAID):
            return index

    return DEFAULT_FIRST_DISABLED_INDEX


def getTotalItemsCount(currentTab, receiptData):
    if currentTab == TabId.HISTORY:
        return len(receiptData.get('raidStatistics', {}))
    receipts = receiptData.get('receipts', {})
    if currentTab == TabId.PUBLIC:
        return sum(1 for r in receipts.values() if not r.get('hidden', False))
    return len(receipts)


def _getReceiptIterator(currentTab, receiptData):
    if currentTab == TabId.HISTORY:
        for _, receiptDataItem in sorted(receiptData.get('raidStatistics', {}).iteritems(), key=lambda item: item[1].get('startTime', 0), reverse=True):
            yield receiptDataItem

    else:
        receipts = receiptData.get('receipts', {})
        sortedReceipts = sorted(receipts.iteritems(), key=getReceiptSortKey)
        for receiptId, receiptDataItem in sortedReceipts:
            if receiptDataItem.get('hidden', False):
                continue
            yield (
             receiptId, receiptDataItem)