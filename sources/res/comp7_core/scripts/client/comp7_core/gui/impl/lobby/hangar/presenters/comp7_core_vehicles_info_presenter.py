import typing
from gui.impl.lobby.common.presenters.vehicles_info_presenter import VehiclesInfoPresenter
if typing.TYPE_CHECKING:
    from gui.shared.gui_items import Vehicle

class Comp7CoreVehiclesInfoPresenter(VehiclesInfoPresenter):

    @property
    def _modeController(self):
        return NotImplementedError

    def _toModelItem(self, vehicle):
        modelItem = super(Comp7CoreVehiclesInfoPresenter, self)._toModelItem(vehicle)
        modelItem['isSuitableVehicle'] = self._modeController.isSuitableVehicle(vehicle) is None
        return modelItem