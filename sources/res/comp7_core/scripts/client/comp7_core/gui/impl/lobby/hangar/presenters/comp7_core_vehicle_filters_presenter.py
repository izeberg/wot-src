import typing
from gui.filters.carousel_filter import FILTER_KEYS
from gui.impl.lobby.hangar.presenters.vehicle_filters_presenter import VehicleFiltersDataProvider
if typing.TYPE_CHECKING:
    from typing import List

class Comp7CoreVehicleFiltersDataProvider(VehicleFiltersDataProvider):

    @classmethod
    def _getBaseSpecialSection(cls):
        specialSection = super(Comp7CoreVehicleFiltersDataProvider, cls)._getBaseSpecialSection()
        specialSection.append(FILTER_KEYS.EVENT)
        return specialSection