from account_helpers.AccountSettings import CUSTOMIZATION_RESOURCE_LIMIT_UPDATED, CUSTOMIZATION_RESOURCE_LAST_CLICK_WEEK, AccountSettings
from gui.Scaleform.daapi.view.lobby.store.browser.shop_helpers import getCustomizationResourceUrl
from gui.impl.lobby.customization.shared import CustomizationTabs
from gui.shared.event_dispatcher import showShop, showHangar
from gui.shared.gui_items import GUI_ITEM_TYPE_NAMES
from helpers import dependency, time_utils
from skeletons.gui.game_control import ICustomizationResourceController

@dependency.replace_none_kwargs(customizationResourceController=ICustomizationResourceController)
def getCustomizationResourceLimitUpdated(customizationResourceController=None):
    isLimitUpdated = AccountSettings.getSettings(CUSTOMIZATION_RESOURCE_LIMIT_UPDATED)
    startTime = customizationResourceController.getStartTime()
    if startTime and not isLimitUpdated:
        currentTime = int(time_utils.getServerUTCTime())
        weeksElapsed = (currentTime - startTime) // time_utils.ONE_WEEK
        lastClickWeek = AccountSettings.getSettings(CUSTOMIZATION_RESOURCE_LAST_CLICK_WEEK)
        if weeksElapsed > lastClickWeek:
            isLimitUpdated = True
            AccountSettings.setSettings(CUSTOMIZATION_RESOURCE_LIMIT_UPDATED, True)
    return isLimitUpdated


@dependency.replace_none_kwargs(customizationResourceController=ICustomizationResourceController)
def setCustomizationResourceLimitFlags(customizationResourceController=None):
    startTime = customizationResourceController.getStartTime()
    if startTime:
        currentTime = int(time_utils.getServerUTCTime())
        weeksElapsed = (currentTime - startTime) // time_utils.ONE_WEEK
        AccountSettings.setSettings(CUSTOMIZATION_RESOURCE_LAST_CLICK_WEEK, weeksElapsed)
    AccountSettings.setSettings(CUSTOMIZATION_RESOURCE_LIMIT_UPDATED, False)


def getTabItemTypeName(tabId):
    itemTypeName = GUI_ITEM_TYPE_NAMES[CustomizationTabs.SLOT_TYPES[tabId]]
    if tabId == CustomizationTabs.STYLED_3D:
        itemTypeName = ('{}_{}').format(itemTypeName, CustomizationTabs.STYLE_PREFIX[tabId])
    return itemTypeName


@dependency.replace_none_kwargs(customizationResourceController=ICustomizationResourceController)
def closeWindowHandler(view, customizationResourceController=None):
    if not customizationResourceController.isEnabled():
        showHangar()
        view.destroyWindow()
    elif not customizationResourceController.isExchangeEnabled():
        showShop(getCustomizationResourceUrl())
        view.destroyWindow()


def splitByChunks(data, chunkSize):
    for i in xrange(0, len(data), chunkSize):
        yield data[i:i + chunkSize]


def mergeResults(allResults):
    mainResult = {'success': True, 
       'items': [], 'reward': {'currencies': {}}}
    for result in allResults:
        if not result.success or result.auxData is None:
            mainResult['success'] = False
            break
        mainResult['items'].extend(result.auxData.items)
        reward = result.auxData.reward or {}
        currencies = reward.get('currencies', {})
        for currencyName, currencyData in currencies.iteritems():
            count = currencyData.get('count', 0)
            if currencyName not in mainResult['reward']['currencies']:
                mainResult['reward']['currencies'][currencyName] = {'count': 0}
            mainResult['reward']['currencies'][currencyName]['count'] += count

    return mainResult