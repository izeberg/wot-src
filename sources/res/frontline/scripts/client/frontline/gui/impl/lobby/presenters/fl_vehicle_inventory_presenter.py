from frontline.gui.impl.lobby.tooltips.carousel_vehicle_tooltip import FLCarouselVehicleTooltipView
from gui.impl.lobby.hangar.presenters.vehicle_inventory_presenter import VehicleInventoryPresenter
from gui.impl.gen import R

class FLVehicleInventoryPresenter(VehicleInventoryPresenter):

    def _getIsBpEntityValid(self):
        return False

    def createToolTipContent(self, event, contentID):
        if contentID == R.views.mono.hangar.vehicle_tooltip():
            return FLCarouselVehicleTooltipView(event.getArgument('inventoryId'))
        return super(FLVehicleInventoryPresenter, self).createToolTipContent(event=event, contentID=contentID)