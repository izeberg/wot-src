from __future__ import absolute_import
from gui.impl.lobby.hangar.presenters.hangar_vehicle_params_presenter import HangarVehicleParamsPresenter
from helpers import dependency
from skeletons.gui.shared import IItemsCache

class LSVehicleParamsPresenter(HangarVehicleParamsPresenter):
    __itemsCache = dependency.descriptor(IItemsCache)

    def _getVehicle(self):
        vehicle = super(LSVehicleParamsPresenter, self)._getVehicle()
        if vehicle:
            return self._removeConsumables(vehicle)
        else:
            return

    def _getDefaultVehicle(self):
        vehicle = super(LSVehicleParamsPresenter, self)._getVehicle()
        if vehicle:
            return self._removeConsumables(vehicle)
        else:
            return

    def _removeConsumables(self, vehicle):
        vehicle = self.__itemsCache.items.getLayoutsVehicleCopy(vehicle)
        vehicle.consumables.setLayout(*([None] * len(vehicle.consumables.layout)))
        vehicle.consumables.setInstalled(*([None] * len(vehicle.consumables.installed)))
        return vehicle