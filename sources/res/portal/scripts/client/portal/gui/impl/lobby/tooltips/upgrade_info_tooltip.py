from frameworks.wulf import ViewSettings
from portal.gui.impl.gen.view_models.views.lobby.tooltips.upgrade_info_tooltip_model import UpgradeInfoTooltipModel
from gui.impl.pub import ViewImpl
from gui.impl.gen import R

class UpgradeInfoTooltip(ViewImpl):
    __slots__ = ()

    def __init__(self):
        settings = ViewSettings(R.views.portal.lobby.tooltips.UpgradeInfoTooltip())
        settings.model = UpgradeInfoTooltipModel()
        super(UpgradeInfoTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        return super(UpgradeInfoTooltip, self).getViewModel()