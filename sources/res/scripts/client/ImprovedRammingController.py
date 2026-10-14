from __future__ import absolute_import
from gui.shared.utils.decorators import ReprInjector
from items.vehicle_mechanics_types import VehicleMechanicKey, VehicleMechanicKeys
from vehicles.components.vehicle_component import VehicleDynamicComponent
from vehicles.mechanics.common import IMechanicComponent

@ReprInjector.withParent()
class ImprovedRammingController(VehicleDynamicComponent, IMechanicComponent):

    def __init__(self):
        super(ImprovedRammingController, self).__init__()
        self._initComponent()

    @property
    def vehicleMechanicKey(self):
        return VehicleMechanicKeys.IMPROVED_RAMMING