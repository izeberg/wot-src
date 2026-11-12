from gui.impl.lobby.customization_resource.customization_resource_exchange_data_provider import getExchangeItemKey

class CustomizationResourceExchangeSelection(object):
    __slots__ = ('__selected', )

    def __init__(self):
        self.__selected = {}

    def clear(self):
        self.__selected.clear()

    def isEmpty(self):
        return not self.__selected

    def getTotalCount(self):
        return sum(self.__selected.itervalues())

    def getPayload(self):
        return tuple((itemCD, vehicleCD, count) for (itemCD, vehicleCD), count in sorted(self.__selected.iteritems()))

    def getSelectedCount(self, item):
        return self.__selected.get(getExchangeItemKey(item), 0)

    def getSelectedCountForTab(self, items):
        return sum(self.getSelectedCount(item) for item in items)

    def setSelectedCount(self, item, count):
        count = max(0, min(int(count), item.availableCount))
        key = getExchangeItemKey(item)
        if count:
            self.__selected[key] = count
        else:
            self.__selected.pop(key, None)
        return count

    def add(self, item):
        return self.setSelectedCount(item, self.getSelectedCount(item) + 1)

    def reduce(self, item):
        return self.setSelectedCount(item, self.getSelectedCount(item) - 1)

    def setSelectedCounts(self, itemsWithCounts):
        for item, count in itemsWithCounts:
            self.setSelectedCount(item, count)

    def deselectAll(self, items):
        for item, _ in items:
            self.setSelectedCount(item, 0)

    def isAllSelected(self, items):
        selectableItems = [ item for item in items if item.availableCount > 0 ]
        return bool(selectableItems) and all(self.getSelectedCount(item) == item.availableCount for item in selectableItems)

    def isAllSelectedWithLimit(self, items, limit):
        selectableItems = [ item for item in items if item.availableCount > 0 ]
        if not selectableItems:
            return False
        selectedInCategory = self.getSelectedCountForTab(selectableItems)
        selectedOutsideCategory = self.getTotalCount() - selectedInCategory
        maxSelectableInCategory = max(0, limit - selectedOutsideCategory)
        totalAvailableInCategory = sum(item.availableCount for item in selectableItems)
        targetSelectedInCategory = min(totalAvailableInCategory, maxSelectableInCategory)
        return selectedInCategory == targetSelectedInCategory

    def reconcile(self, dataProvider):
        for key, selectedCount in self.__selected.items():
            item = dataProvider.getItem(key)
            if item is None:
                self.__selected.pop(key, None)
            else:
                self.setSelectedCount(item, selectedCount)

        return