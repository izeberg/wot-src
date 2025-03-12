from frameworks.wulf import ViewFlags, ViewSettings
from gui_lootboxes.gui.impl.gen.view_models.views.lobby.gui_lootboxes.tooltips.lootbox_tooltip_extended_model import LootboxTooltipExtendedModel
from gui.impl.pub import ViewImpl

class LootboxTooltipExtended(ViewImpl):
    __slots__ = ()

    def __init__(self, layoutID):
        settings = ViewSettings(layoutID)
        settings.flags = ViewFlags.LOBBY_SUB_VIEW
        settings.model = LootboxTooltipExtendedModel()
        super(LootboxTooltipExtended, self).__init__(settings)

    @property
    def viewModel(self):
        return super(LootboxTooltipExtended, self).getViewModel()