from typing import Optional
import CGF
from Vehicle import Vehicle
from constants import IS_CELLAPP

def getVehicleFromGO(vehicleGO, spaceID):
    hierarchyManager = CGF.HierarchyManager(spaceID)
    if not hierarchyManager:
        return None
    else:
        parentGO = hierarchyManager.getTopMostParent(vehicleGO)
        vehicle = parentGO.findComponentByType(Vehicle)
        if not vehicle or IS_CELLAPP and vehicle.status < 0:
            return None
        return vehicle