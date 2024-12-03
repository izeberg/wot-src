import CGF
from GenericComponents import EntityGOSync

def getCmpByTypeInTopMostParent(spaceID, gameObject, clazz):
    hierarchy = CGF.HierarchyManager(spaceID)
    rootGameObject = hierarchy.getTopMostParent(gameObject)
    return rootGameObject.findComponentByType(clazz)


def getVehicleFromGO(spaceID, gameObject):
    goSyncComponent = getCmpByTypeInTopMostParent(spaceID, gameObject, EntityGOSync)
    if goSyncComponent:
        return goSyncComponent.entity
    else:
        return