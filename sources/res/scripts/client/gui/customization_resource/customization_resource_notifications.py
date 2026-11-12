from account_helpers import AccountSettings
from account_helpers.AccountSettings import CUSTOMIZATION_RESOURCE_EXCHANGE_PENDING
from gui import SystemMessages
from gui.impl import backport
from gui.impl.gen import R
from gui.impl.lobby.customization.shared import CustomizationTabs
from gui.shared.notifications import NotificationPriorityLevel
_CATEGORY_RESOURCES = (
 (
  CustomizationTabs.PAINTS, 'paints'),
 (
  CustomizationTabs.INSCRIPTIONS, 'inscriptions'),
 (
  CustomizationTabs.EMBLEMS, 'emblems'),
 (
  CustomizationTabs.CAMOUFLAGES, 'camouflages'),
 (
  CustomizationTabs.PROJECTION_DECALS, 'projectionDecals'),
 (
  CustomizationTabs.MODIFICATIONS, 'modifications'),
 (
  CustomizationTabs.STYLED_2D, 'styles2D'),
 (
  CustomizationTabs.STYLED_3D, 'styles3D'))

def markExchangePending():
    AccountSettings.setSettings(CUSTOMIZATION_RESOURCE_EXCHANGE_PENDING, True)


def clearExchangePending():
    AccountSettings.setSettings(CUSTOMIZATION_RESOURCE_EXCHANGE_PENDING, False)


def isExchangePending():
    return AccountSettings.getSettings(CUSTOMIZATION_RESOURCE_EXCHANGE_PENDING)


def formatExchangedItems(categoryCounts):
    texts = R.strings.system_messages.customizationResource
    result = []
    for tabId, resourceKey in _CATEGORY_RESOURCES:
        count = int(categoryCounts.get(tabId, 0))
        if count <= 0:
            continue
        result.append(backport.text(texts.exchange.categoryItem(), name=backport.text(texts.categories.dyn(resourceKey)()), count=count))

    return (', ').join(result)


def getCategoryCounts(items, categoryMap):
    result = {}
    for itemCD, _, count in items:
        category = categoryMap.get(itemCD)
        if category is not None:
            result[category] = result.get(category, 0) + count

    return result


def pushExchangeSuccess(categoryCounts, reward):
    texts = R.strings.system_messages.customizationResource.exchange.success
    SystemMessages.pushMessage(text=backport.text(texts.body(), items=formatExchangedItems(categoryCounts), reward=reward), type=SystemMessages.SM_TYPE.CustomizationResource, priority=NotificationPriorityLevel.LOW, messageData={'header': backport.text(texts.title())})


def pushExchangeError():
    texts = R.strings.system_messages.customizationResource.exchange.error
    SystemMessages.pushMessage(text=backport.text(texts.body()), type=SystemMessages.SM_TYPE.ErrorHeader, priority=NotificationPriorityLevel.HIGH, messageData={'header': backport.text(texts.title())})