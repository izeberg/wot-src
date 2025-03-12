from frameworks.wulf import ViewFlags, ViewSettings
from cosmic_event.gui.impl.gen.view_models.views.lobby.tooltips.cosmic_simple_tooltip_model import CosmicSimpleTooltipModel
from gui.impl.pub import ViewImpl

class CosmicSimpleTooltip(ViewImpl):
    __slots__ = ()

    def __init__(self, layoutID):
        settings = ViewSettings(layoutID)
        settings.flags = ViewFlags.LOBBY_SUB_VIEW
        settings.model = CosmicSimpleTooltipModel()
        super(CosmicSimpleTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        return super(CosmicSimpleTooltip, self).getViewModel()