from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.customization_resource.customization_resource_currency_tooltip_view_model import CustomizationResourceCurrencyTooltipViewModel
from gui.impl.pub import ViewImpl
from helpers import dependency
from skeletons.gui.game_control import ICustomizationResourceController

class CustomizationResourceCurrencyTooltipView(ViewImpl):
    __slots__ = ()
    __customizationResourceController = dependency.descriptor(ICustomizationResourceController)

    def __init__(self):
        settings = ViewSettings(R.views.lobby.customization_resource.tooltips.CustomizationResourceCurrencyTooltipView())
        settings.model = CustomizationResourceCurrencyTooltipViewModel()
        super(CustomizationResourceCurrencyTooltipView, self).__init__(settings)

    @property
    def viewModel(self):
        return super(CustomizationResourceCurrencyTooltipView, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        super(CustomizationResourceCurrencyTooltipView, self)._onLoading()
        with self.viewModel.transaction() as (tx):
            tx.setBalance(self.__customizationResourceController.getCurrencyBalance())
            tx.setStartTimestamp(self.__customizationResourceController.getStartTime() or 0)
            tx.setEndTimestamp(self.__customizationResourceController.getExpiryTime() or 0)