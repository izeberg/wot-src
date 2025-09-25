import typing
from gui.impl.lobby.tooltips.carousel_vehicle_tooltip import CarouselVehicleTooltipView
if typing.TYPE_CHECKING:
    from gui.shared.gui_items.Vehicle import Vehicle

class FLCarouselVehicleTooltipView(CarouselVehicleTooltipView):

    def _getDailyXPFactor(self, vehicle):
        return -1

    def _getBpProgression(self, vehicleIntCD):
        bpPoints, _ = self._battlePass.getVehicleProgression(vehicleIntCD)
        return (bpPoints, 0)

    def _getIsBpEntityValid(self):
        return False