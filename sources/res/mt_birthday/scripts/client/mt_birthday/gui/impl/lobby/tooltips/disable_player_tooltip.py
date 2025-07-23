from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from mt_birthday.gui.impl.gen.view_models.views.lobby.tooltips.disable_player_tooltip_model import DisablePlayerTooltipModel
from gui.impl.pub import ViewImpl

class DisablePlayerTooltip(ViewImpl):
    __slots__ = ('__cooldown', )

    def __init__(self, cooldown):
        settings = ViewSettings(R.views.mt_birthday.lobby.tooltips.DisablePlayerTooltip(), model=DisablePlayerTooltipModel())
        self.__cooldown = cooldown
        super(DisablePlayerTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        return super(DisablePlayerTooltip, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        with self.viewModel.transaction() as (vm):
            vm.setTime(self.__cooldown)