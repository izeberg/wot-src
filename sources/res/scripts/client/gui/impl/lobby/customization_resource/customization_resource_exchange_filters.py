from gui.impl.lobby.customization.filter_types import AvailabilityFilterState, CarouselFilterTypes
from gui.impl.lobby.customization.shared import CustomizationTabs
from items.components.c11n_constants import CustomizationDisplayType, ProjectionDecalFormTags
_BOOLEAN_FILTERS = (
 CarouselFilterTypes.APPLIED,
 CarouselFilterTypes.INVENTORY,
 CarouselFilterTypes.FAVORITE,
 CarouselFilterTypes.HISTORIC,
 CarouselFilterTypes.NON_HISTORIC,
 CarouselFilterTypes.FANTASTICAL,
 CarouselFilterTypes.ONLY_PROGRESSION_DECALS,
 CarouselFilterTypes.ONLY_EDITABLE_STYLES,
 CarouselFilterTypes.ONLY_NON_EDITABLE_STYLES,
 CarouselFilterTypes.ONLY_PROGRESSION_STYLES,
 CarouselFilterTypes.FORMFACTOR_SQUARE,
 CarouselFilterTypes.FORMFACTOR_RECT1X2,
 CarouselFilterTypes.FORMFACTOR_RECT1X3,
 CarouselFilterTypes.FORMFACTOR_RECT1X4,
 CarouselFilterTypes.FORMFACTOR_RECT1X6)
_HISTORIC_FILTERS = {CarouselFilterTypes.HISTORIC: CustomizationDisplayType.HISTORICAL, 
   CarouselFilterTypes.NON_HISTORIC: CustomizationDisplayType.NON_HISTORICAL, 
   CarouselFilterTypes.FANTASTICAL: CustomizationDisplayType.FANTASTICAL}
_FORMFACTOR_FILTERS = {CarouselFilterTypes.FORMFACTOR_SQUARE: ProjectionDecalFormTags.SQUARE, 
   CarouselFilterTypes.FORMFACTOR_RECT1X2: ProjectionDecalFormTags.RECT1X2, 
   CarouselFilterTypes.FORMFACTOR_RECT1X3: ProjectionDecalFormTags.RECT1X3, 
   CarouselFilterTypes.FORMFACTOR_RECT1X4: ProjectionDecalFormTags.RECT1X4, 
   CarouselFilterTypes.FORMFACTOR_RECT1X6: ProjectionDecalFormTags.RECT1X6}
_FILTER_STRUCTURE_BASE = ('availability', 'special', 'historic')

class CustomizationResourceExchangeFilters(object):
    __slots__ = ('__filters', '__groupByTab')

    def __init__(self):
        self.__filters = {key:False for key in _BOOLEAN_FILTERS}
        self.__groupByTab = {}

    def clear(self):
        for key in self.__filters:
            self.__filters[key] = False

        self.__groupByTab.clear()

    def change(self, key, value, tabId, groups):
        if key == CarouselFilterTypes.GROUP:
            self.__changeGroup(value, tabId, groups)
        elif key == CarouselFilterTypes.AVAILABILITY:
            self.__filters[CarouselFilterTypes.INVENTORY] = value == AvailabilityFilterState.INVENTORY
        elif key in self.__filters:
            self.__filters[key] = bool(value)

    def apply(self, items, tabId):
        return tuple(item for item in items if self.__matches(item, tabId))

    def hasAppliedFilter(self, tabId, groups):
        if self.__groupByTab.get(tabId) in groups:
            return True
        keys = (
         CarouselFilterTypes.APPLIED,
         CarouselFilterTypes.INVENTORY,
         CarouselFilterTypes.FAVORITE,
         CarouselFilterTypes.HISTORIC,
         CarouselFilterTypes.NON_HISTORIC,
         CarouselFilterTypes.FANTASTICAL)
        if tabId == CustomizationTabs.PROJECTION_DECALS:
            keys += (
             CarouselFilterTypes.ONLY_PROGRESSION_DECALS,
             CarouselFilterTypes.FORMFACTOR_SQUARE,
             CarouselFilterTypes.FORMFACTOR_RECT1X2,
             CarouselFilterTypes.FORMFACTOR_RECT1X3,
             CarouselFilterTypes.FORMFACTOR_RECT1X4,
             CarouselFilterTypes.FORMFACTOR_RECT1X6)
        elif tabId in CustomizationTabs.STYLES_ALL:
            keys += (
             CarouselFilterTypes.ONLY_EDITABLE_STYLES,
             CarouselFilterTypes.ONLY_NON_EDITABLE_STYLES,
             CarouselFilterTypes.ONLY_PROGRESSION_STYLES)
        return any(self.__filters[key] for key in keys)

    def getFilterData(self):
        result = dict(self.__filters)
        result[CarouselFilterTypes.AVAILABILITY] = AvailabilityFilterState.INVENTORY if self.__filters[CarouselFilterTypes.INVENTORY] else AvailabilityFilterState.ALL
        return result

    def isAnyFiltersApplied(self):
        return any(self.__filters.values())

    def getSelectedGroup(self, tabId, groups):
        selectedGroup = self.__groupByTab.get(tabId)
        if selectedGroup not in groups:
            self.__groupByTab.pop(tabId, None)
            return -1
        else:
            return groups.index(selectedGroup)

    @staticmethod
    def getGroups(items, tabId):
        if tabId == CustomizationTabs.MODIFICATIONS:
            return ()
        return tuple(sorted(set(item.groupName for item in items if item.groupName)))

    @staticmethod
    def getStructure(items, tabId, groups):
        structure = list(_FILTER_STRUCTURE_BASE)
        if groups:
            structure.append('groups')
        if tabId == CustomizationTabs.PROJECTION_DECALS:
            structure.append('formfactor')
            if any(item.isProgressive for item in items):
                structure.append('progressionDecals')
        elif tabId in CustomizationTabs.STYLES_ALL:
            structure.append('editable')
        return tuple(structure)

    def __matches(self, item, tabId):
        if self.__filters[CarouselFilterTypes.INVENTORY] and item.inventoryCount <= 0:
            return False
        else:
            if self.__filters[CarouselFilterTypes.APPLIED] and item.installedCount <= 0:
                return False
            if self.__filters[CarouselFilterTypes.FAVORITE] and not item.isFavorite:
                return False
            selectedGroup = self.__groupByTab.get(tabId)
            if selectedGroup is not None and item.groupName != selectedGroup:
                return False
            displayTypes = tuple(displayType for key, displayType in _HISTORIC_FILTERS.iteritems() if self.__filters[key])
            if displayTypes and item.displayType not in displayTypes:
                return False
            if tabId == CustomizationTabs.PROJECTION_DECALS:
                if self.__filters[CarouselFilterTypes.ONLY_PROGRESSION_DECALS] and not item.isProgressive:
                    return False
                formfactors = tuple(formfactor for key, formfactor in _FORMFACTOR_FILTERS.iteritems() if self.__filters[key])
                if formfactors and item.formfactor not in formfactors:
                    return False
            if tabId in CustomizationTabs.STYLES_ALL:
                stylePredicates = []
                if self.__filters[CarouselFilterTypes.ONLY_EDITABLE_STYLES]:
                    stylePredicates.append(item.isEditable)
                if self.__filters[CarouselFilterTypes.ONLY_NON_EDITABLE_STYLES]:
                    stylePredicates.append(not item.isEditable)
                if self.__filters[CarouselFilterTypes.ONLY_PROGRESSION_STYLES]:
                    stylePredicates.append(item.isProgressive)
                if stylePredicates and not any(stylePredicates):
                    return False
            return True

    def __changeGroup(self, value, tabId, groups):
        try:
            groupIndex = int(value)
        except (TypeError, ValueError):
            groupIndex = -1

        if 0 <= groupIndex < len(groups):
            self.__groupByTab[tabId] = groups[groupIndex]
        else:
            self.__groupByTab.pop(tabId, None)
        return