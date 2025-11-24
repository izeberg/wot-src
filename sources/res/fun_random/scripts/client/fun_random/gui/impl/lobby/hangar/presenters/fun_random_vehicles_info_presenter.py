from __future__ import absolute_import
from gui.impl.lobby.common.presenters.vehicles_info_presenter import VehiclesInfoPresenter
from gui.shared.gui_items.Vehicle import Vehicle

class FunRandomVehiclesInfoPresenter(VehiclesInfoPresenter):

    def _toModelItem(self, vehicle):
        modelItem = super(FunRandomVehiclesInfoPresenter, self)._toModelItem(vehicle)
        modelItem['isSuitableVehicle'] = vehicle.getCustomState() != Vehicle.VEHICLE_STATE.UNSUITABLE_TO_QUEUE
        return modelItem