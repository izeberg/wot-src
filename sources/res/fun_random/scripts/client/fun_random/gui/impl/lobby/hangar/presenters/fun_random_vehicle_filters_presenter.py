from __future__ import absolute_import
from gui.impl.lobby.hangar.presenters.vehicle_filters_presenter import VehicleFiltersDataProvider

class FunRandomVehicleFiltersDataProvider(VehicleFiltersDataProvider):

    @classmethod
    def _getBaseSpecialSection(cls):
        return super(FunRandomVehicleFiltersDataProvider, cls)._getBaseSpecialSection() + ['funRandom']