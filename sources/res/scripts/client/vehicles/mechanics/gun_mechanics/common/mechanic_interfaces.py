from __future__ import absolute_import
from vehicles.components.component_interfaces import IVehicleGunSlotComponent
from vehicles.mechanics.common import IMechanicComponentLogic

class IGunMechanicComponent(IVehicleGunSlotComponent, IMechanicComponentLogic):
    pass