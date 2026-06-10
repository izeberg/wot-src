import typing, CGF
from constants import IS_CLIENT
if IS_CLIENT:
    from Vehicle import Vehicle
    from debug_utils import LOG_ERROR

def getVehicleFromGO(vehicleGO, spaceID):
    hierarchyManager = CGF.HierarchyManager(spaceID)
    if hierarchyManager is None:
        LOG_ERROR('unable to extract vehicle, hierarchyManager is None')
        return
    else:
        parentGO = hierarchyManager.getTopMostParent(vehicleGO)
        vehicle = parentGO.findComponentByType(Vehicle)
        if not vehicle and vehicle.status < 0:
            LOG_ERROR('unable to extract vehicle component')
            return
        return vehicle