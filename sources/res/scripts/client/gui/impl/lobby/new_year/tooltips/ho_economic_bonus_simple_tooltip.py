from gui.impl.gen import R
from frameworks.wulf import ViewSettings
from gui.impl.gen.view_models.views.lobby.new_year.tooltips.ho_economic_bonus_simple_tooltip_model import HoEconomicBonusSimpleTooltipModel
from gui.impl.pub import ViewImpl

class HOEconomicBonusSimpleTooltip(ViewImpl):

    def __init__(self, header, body):
        settings = ViewSettings(R.views.mono.holiday_ops.tooltips.ho_economic_bonus_simple_tooltip())
        settings.model = HoEconomicBonusSimpleTooltipModel()
        self.__header = header
        self.__body = body
        super(HOEconomicBonusSimpleTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        return super(HOEconomicBonusSimpleTooltip, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        super(HOEconomicBonusSimpleTooltip, self)._onLoading()
        with self.viewModel.transaction() as (model):
            model.setHeader(self.__header)
            model.setBody(self.__body)