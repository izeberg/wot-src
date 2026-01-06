from frameworks.wulf import ViewFlags, ViewSettings
from frontline.gui.impl.gen.view_models.views.lobby.tooltips.unlock_conditions_tooltip_model import UnlockConditionsTooltipModel
from gui.impl.pub import ViewImpl
from gui.impl.gen import R

class UnlockConditionsTooltip(ViewImpl):
    __slots__ = ('__supplyName', )

    def __init__(self, layoutID=R.views.frontline.lobby.tooltips.UnlockConditionsTooltip(), supplyName=None):
        settings = ViewSettings(layoutID)
        settings.flags = ViewFlags.VIEW
        settings.model = UnlockConditionsTooltipModel()
        self.__supplyName = supplyName
        super(UnlockConditionsTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        return super(UnlockConditionsTooltip, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        super(UnlockConditionsTooltip, self)._onLoading(*args, **kwargs)
        with self.viewModel.transaction() as (vm):
            vm.setObject(self.__supplyName)