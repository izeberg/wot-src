import typing
from gui.impl.lobby.hangar.presenters.vehicle_statistics_presenter import VehiclesStatisticsPresenter
if typing.TYPE_CHECKING:
    from gui.shared.gui_items.Vehicle import Vehicle

class FLVehiclesStatisticsPresenter(VehiclesStatisticsPresenter):

    def _getDailyXPFactor(self, vehicle):
        return -1

    def _getMaxBpScore(self, vehicle):
        return (0, 0)