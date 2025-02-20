from frameworks.wulf import ViewFlags, ViewSettings
from cosmic_event.gui.impl.gen.view_models.views.lobby.tooltips.vehicle_shell_tooltip_model import VehicleShellTooltipModel
from gui.impl.pub import ViewImpl

class VehicleShellTooltip(ViewImpl):
    __slots__ = ()

    def __init__(self, layoutID):
        settings = ViewSettings(layoutID)
        settings.flags = ViewFlags.LOBBY_SUB_VIEW
        settings.model = VehicleShellTooltipModel()
        super(VehicleShellTooltip, self).__init__(settings)

    @property
    def viewModel(self):
        return super(VehicleShellTooltip, self).getViewModel()