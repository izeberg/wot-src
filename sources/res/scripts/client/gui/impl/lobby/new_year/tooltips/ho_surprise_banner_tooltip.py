from frameworks.wulf import ViewSettings, ViewModel
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.new_year.tooltips.ho_surprise_banner_tooltip_model import HoSurpriseBannerTooltipModel
from gui.impl.pub import ViewImpl

class HOSurpriseBannerTooltip(ViewImpl):

    def __init__(self, isActiveState):
        settings = ViewSettings(R.views.mono.holiday_ops.tooltips.ho_surprise_banner_tooltip())
        settings.model = HoSurpriseBannerTooltipModel()
        self.__isActiveState = isActiveState
        super(HOSurpriseBannerTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        return super(HOSurpriseBannerTooltip, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        super(HOSurpriseBannerTooltip, self)._onLoading()
        with self.viewModel.transaction() as (model):
            model.setIsActiveState(self.__isActiveState)