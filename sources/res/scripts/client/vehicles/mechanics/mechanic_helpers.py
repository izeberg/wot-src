import typing, BigWorld
from vehicles.mechanics.mechanic_constants import VEHICLE_MECHANIC_DYN_COMPONENT_NAMES as _DYN_COMPONENTS_NAMES, VEHICLE_MECHANIC_TO_PARAMS
if typing.TYPE_CHECKING:
    from items.vehicles import VehicleDescriptor
    from Vehicle import Vehicle
    from vehicles.mechanics.mechanic_constants import VehicleMechanic

def getVehicleMechanic(mechanic, vehicle):
    if vehicle is not None:
        return vehicle.dynamicComponents.get(_DYN_COMPONENTS_NAMES[mechanic], None)
    else:
        return


def getPlayerVehicleMechanic(mechanic):
    vehicle = BigWorld.player().getVehicleAttached()
    if vehicle is not None and vehicle.isPlayerVehicle and vehicle.isAlive():
        return vehicle.dynamicComponents.get(_DYN_COMPONENTS_NAMES[mechanic], None)
    else:
        return


def getVehicleMechanicParams(mechanic, descr):
    return descr.mechanicsParams.get(VEHICLE_MECHANIC_TO_PARAMS[mechanic])