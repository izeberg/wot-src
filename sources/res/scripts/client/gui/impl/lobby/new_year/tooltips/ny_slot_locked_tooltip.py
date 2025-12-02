from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.new_year.tooltips.ny_slot_locked_tooltip_model import NySlotLockedTooltipModel
from gui.impl.pub import ViewImpl

class NySlotLockedTooltip(ViewImpl):

    def __init__(self, *args, **kwargs):
        settings = ViewSettings(R.views.mono.holiday_ops.tooltips.ho_slot_locked_tooltip())
        settings.model = NySlotLockedTooltipModel()
        settings.args = args
        settings.kwargs = kwargs
        super(NySlotLockedTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        return super(NySlotLockedTooltip, self).getViewModel()

    def _onLoading(self, level):
        super(NySlotLockedTooltip, self)._onLoading()
        with self.viewModel.transaction() as (model):
            model.setLevel(level)