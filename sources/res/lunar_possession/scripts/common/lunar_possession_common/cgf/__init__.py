import CGF
from constants import IS_EDITOR
if IS_EDITOR:

    class Vehicle(object):
        pass


else:
    from Vehicle import Vehicle
    from typing import Optional

def getVehicleFromParent(go):
    hierarchyManager = CGF.HierarchyManager(go.spaceID)
    if not hierarchyManager:
        return
    else:
        result = hierarchyManager.findComponentInParent(go, Vehicle)
        if result:
            return result[1]
        return