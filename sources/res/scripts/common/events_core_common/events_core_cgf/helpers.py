from typing import Optional
import CGF
from constants import IS_CELLAPP, IS_EDITOR
if IS_EDITOR:

    class Vehicle(object):
        pass


else:
    from Vehicle import Vehicle

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