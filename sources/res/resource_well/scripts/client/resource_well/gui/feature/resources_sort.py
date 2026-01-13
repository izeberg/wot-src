from __future__ import absolute_import
import typing
from gui import GUI_NATIONS, NONE_NATION_NAME
from gui.Scaleform.genConsts.CURRENCIES_CONSTANTS import CURRENCIES_CONSTANTS
from gui.shared.money import Currency
from resource_well.gui.feature.constants import ResourceType
_NO_NATION_INDEX = 0
_NATIONS_ORDER = {name:idx for idx, name in enumerate(GUI_NATIONS, 1)}
_NATIONS_ORDER[NONE_NATION_NAME] = _NO_NATION_INDEX
_CURRENCY_ORDER = {name:idx for idx, name in enumerate(Currency.GUI_ALL + (CURRENCIES_CONSTANTS.FREE_XP,))}
_RESOURCE_TYPE_ORDER = (
 ResourceType.CURRENCY,
 ResourceType.BLUEPRINTS)

def sortCurrencyResource(resource):
    return _CURRENCY_ORDER.get(resource.guiName, len(_CURRENCY_ORDER))


def sortBlueprintsResource(resource):
    return _NATIONS_ORDER.get(resource.nation, len(_NATIONS_ORDER))


_RESOURCE_SORTERS = {ResourceType.BLUEPRINTS: sortBlueprintsResource, 
   ResourceType.CURRENCY: sortCurrencyResource}

def getSorterByResourceType(resourceType):
    return _RESOURCE_SORTERS.get(resourceType)


def sortAnyResource(resource):
    resourceType = ResourceType.getMember(resource.type)
    sorter = getSorterByResourceType(resourceType)
    if resourceType and sorter:
        return (sortByResourceType(resourceType), sorter(resource))
    return (0, 0)


def sortByResourceType(resourceType):
    if resourceType in _RESOURCE_TYPE_ORDER:
        return _RESOURCE_TYPE_ORDER.index(resourceType)
    return len(_RESOURCE_TYPE_ORDER)