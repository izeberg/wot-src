from gui.shared import g_eventBus, events as events_constants
from ho_notification import HONotification
from gui.impl.gen.view_models.views.lobby.new_year.notifications.ny_sack_rare_loot_model import NySackRareLootModel
from gui.shared.gui_items import GUI_ITEM_TYPE, GUI_ITEM_TYPE_INDICES
from helpers import dependency
from skeletons.gui.customization import ICustomizationService
from skeletons.gui.shared import IItemsCache

class HOSackRareLoot(HONotification):
    __itemsCache = dependency.descriptor(IItemsCache)
    __c11n = dependency.descriptor(ICustomizationService)

    def __init__(self, resId, *args, **kwargs):
        model = NySackRareLootModel()
        self.__customizationItem = None
        super(HOSackRareLoot, self).__init__(resId, model, *args, **kwargs)
        return

    @property
    def viewModel(self):
        return super(HOSackRareLoot, self).getViewModel()

    def _getEvents(self):
        events = super(HOSackRareLoot, self)._getEvents()
        return events + (
         (
          self.viewModel.onClick, self.__onClick),)

    def _canNavigate(self):
        return super(HOSackRareLoot, self)._canNavigate() and self._canShowStyle()

    def _update(self):
        self.__customizationItem = self.__getCustomizationItem()
        with self.viewModel.transaction() as (model):
            model.setIsButtonDisabled(not self._canNavigate())
            model.setIsPopUp(self._isPopUp)
            model.setUserName(self.__customizationItem.userName)
            model.setItemType(self.__customizationItem.itemTypeName)
            model.setIconName(('_').join([self.__customizationItem.itemFullTypeName, str(self.__customizationItem.id)]))
            model.setAmount(self._getPayload()['value'])

    def _finalize(self):
        self.__customizationItem = None
        super(HOSackRareLoot, self)._finalize()
        return

    def __onClick(self):
        if self.__customizationItem.itemTypeName == 'style':
            g_eventBus.handleEvent(events_constants.HidePopoverEvent(events_constants.HidePopoverEvent.HIDE_POPOVER))
            self._showStylePreview(self.__customizationItem)

    def __getCustomizationItem(self):
        data = self._getPayload()
        itemType = data['custType']
        itemTypeID = self.__getItemTypeID(itemType)
        item = self.__c11n.getItemByID(itemTypeID, data['id'])
        custItem = self.__itemsCache.items.getItemByCD(item.intCD)
        return custItem

    @staticmethod
    def __getItemTypeID(itemTypeName):
        if itemTypeName == 'projection_decal':
            itemTypeID = GUI_ITEM_TYPE.PROJECTION_DECAL
        elif itemTypeName == 'personal_number':
            itemTypeID = GUI_ITEM_TYPE.PERSONAL_NUMBER
        else:
            itemTypeID = GUI_ITEM_TYPE_INDICES.get(itemTypeName)
        return itemTypeID