from __future__ import absolute_import
from typing import Any, Callable, Dict, Optional, Tuple, TYPE_CHECKING
from future.utils import viewvalues
import BigWorld
from items.vehicle_mechanics_types import VehicleMechanicKey
from vehicles.mechanics.common import IMechanicComponentLogic
from vehicles.mechanics.mechanic_constants import VEHICLE_MECHANIC_DYN_COMPONENT_NAMES as _DYN_COMPONENTS_NAMES, VEHICLE_MECHANIC_TAGS, TRACKABLE_VEHICLE_MECHANICS
if TYPE_CHECKING:
    from items.components.shared_components import MechanicsParams
    from items.vehicles import VehicleDescriptor
    from Vehicle import Vehicle
    from vehicles.mechanics.common import IMechanicComponent

def isValidMechanicComponent(component):
    return isinstance(component, IMechanicComponentLogic) and component.isValid


def isVehicleMechanicComponent(component, mechanicKey):
    return isValidMechanicComponent(component) and component.vehicleMechanicKey == mechanicKey


def hasVehicleMechanicComponent(vehicle, mechanicKey):
    return getVehicleMechanicComponent(vehicle, mechanicKey) is not None


def getVehicleMechanicComponent(vehicle, mechanicKey):
    if vehicle is not None:
        return findVehicleMechanicDynamicComponent(vehicle.dynamicComponents, mechanicKey)
    else:
        return


def getVehicleMechanicsComponents(vehicle, criteria=isValidMechanicComponent):
    return {component.vehicleMechanicKey:component for component in viewvalues(vehicle.dynamicComponents if vehicle is not None else {}) if criteria(component)}


def getPlayerVehicleMechanicComponent(mechanicKey):
    vehicle = BigWorld.player().getVehicleAttached()
    if vehicle is not None and vehicle.isPlayerVehicle and vehicle.isAlive():
        return findVehicleMechanicDynamicComponent(vehicle.dynamicComponents, mechanicKey)
    else:
        return


def findVehicleMechanicDynamicComponent(dynamicComponents, mechanicKey):
    component = dynamicComponents.get(_DYN_COMPONENTS_NAMES[mechanicKey.mechanic])
    if isVehicleMechanicComponent(component, mechanicKey):
        return component
    else:
        return


def hasVehicleDescrMechanic(vehicleDescriptor, mechanicKey):
    mechanic = mechanicKey.mechanic
    if mechanic in VEHICLE_MECHANIC_TAGS:
        return vehicleDescriptor.hasTag(VEHICLE_MECHANIC_TAGS[mechanic])
    return mechanic.value in vehicleDescriptor.mechanicsParams


def getVehicleDescrMechanics(vehicleDescriptor):
    return tuple(mechanic for mechanic in TRACKABLE_VEHICLE_MECHANICS if hasVehicleDescrMechanic(vehicleDescriptor, mechanic))


def getVehicleDescrMechanicParams(vehicleDescriptor, mechanicKey):
    return vehicleDescriptor.mechanicsParams.get(mechanicKey.mechanic.value)


def isMechanicInMechanicsParams(mechanicParams, mechanicKey):
    return getMechanicFromMechanicsParams(mechanicParams, mechanicKey) is not None


def getMechanicFromMechanicsParams(mechanicParams, mechanicKey):
    return mechanicParams.get(mechanicKey.mechanic.value)