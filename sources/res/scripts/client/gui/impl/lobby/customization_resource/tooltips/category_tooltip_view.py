from frameworks.wulf import ViewSettings
from gui.impl.lobby.customization_resource.shared import getTabItemTypeName
from gui.impl.gen.view_models.views.lobby.customization_resource.customization_resource_exchange_item_model import CustomizationResourceExchangeItemModel
from gui.impl.gen.view_models.views.lobby.customization_resource.tooltips.category_tooltip_view_model import CategoryTooltipViewModel
from gui.impl.gen import R
from gui.impl.pub import ViewImpl
MAX_ITEMS_LIMIT = 5

class CategoryTooltipView(ViewImpl):
    __slots__ = ('__activeItems', '__selection', '__tabId')

    def __init__(self, activeItems, selection, tabId):
        settings = ViewSettings(R.views.lobby.customization_resource.tooltips.CategoryTooltipView())
        settings.model = CategoryTooltipViewModel()
        self.__activeItems = activeItems
        self.__selection = selection
        self.__tabId = tabId
        super(CategoryTooltipView, self).__init__(settings)

    @property
    def viewModel(self):
        return super(CategoryTooltipView, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        super(CategoryTooltipView, self)._onLoading()
        self.__fillModel()

    def __fillModel(self):
        selectedItems = tuple(item for item in self.__activeItems if self.__selection.getSelectedCount(item))
        with self.viewModel.transaction() as (model):
            model.setItemType(getTabItemTypeName(self.__tabId))
            model.setSelectedCount(self.__selection.getSelectedCountForTab(self.__activeItems))
            itemsModel = model.getItems()
            itemsModel.clear()
            for index, item in enumerate(selectedItems):
                if index == MAX_ITEMS_LIMIT:
                    model.setOtherCount(len(selectedItems) - MAX_ITEMS_LIMIT)
                    break
                itemModel = CustomizationResourceExchangeItemModel()
                itemModel.setIntCD(item.intCD)
                itemModel.setVehicleCD(item.vehicleCD)
                itemModel.setName(item.name)
                itemModel.setIcon(item.icon)
                itemModel.setIsWide(bool(item.isWide))
                itemModel.setSelectedCount(self.__selection.getSelectedCount(item))
                itemsModel.addViewModel(itemModel)

            itemsModel.invalidate()