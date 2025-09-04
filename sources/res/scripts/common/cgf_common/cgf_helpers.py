import typing, CGF
from constants import IS_EDITOR, IS_CGF_DUMP
if IS_EDITOR or IS_CGF_DUMP:

    class Vehicle(object):
        pass


else:
    from Vehicle import Vehicle

def getVehicleEntityByGameObject(gameObject):
    return getParentComponentByGameObject(gameObject, Vehicle)


def getVehicleEntityByVehicleGameObject(vehicleGameObject):
    return vehicleGameObject.findComponentByType(Vehicle)


def getVehicleGameObjectByGameObject(gameObject):
    hierarchy = CGF.HierarchyManager(gameObject.spaceID)
    findResult = hierarchy.findComponentInParent(gameObject, Vehicle)
    if findResult is not None:
        return findResult[0]
    else:
        return


def getParentComponentByGameObject(gameObject, componentType):
    hierarchy = CGF.HierarchyManager(gameObject.spaceID)
    findResult = hierarchy.findComponentInParent(gameObject, componentType)
    if findResult is not None:
        return findResult[1]
    else:
        return


def getParentGameObjectByComponent(gameObject, componentType):
    hierarchy = CGF.HierarchyManager(gameObject.spaceID)
    findResult = hierarchy.findComponentInParent(gameObject, componentType)
    if findResult is not None:
        return findResult[0]
    else:
        return