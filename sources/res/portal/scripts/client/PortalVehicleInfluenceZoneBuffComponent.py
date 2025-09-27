import BigWorld, CGF, Math
from items import vehicles

class PortalVehicleInfluenceZoneBuffComponent(BigWorld.DynamicScriptComponent):

    def __init__(self):
        super(PortalVehicleInfluenceZoneBuffComponent, self).__init__()
        self.__prefab = None
        return

    def set_isActive(self, prev):
        if prev == self.isActive:
            return
        else:
            if self.isActive:
                equipment = vehicles.g_cache.equipments()[self.equipmentID]
                usagePrefab = equipment.params['usagePrefab']
                CGF.loadGameObjectIntoHierarchy(usagePrefab, self.entity.entityGameObject, Math.Vector3(), self.__onPrefabLoaded)
            elif self.__prefab is not None and self.__prefab.isValid():
                CGF.removeGameObject(self.__prefab)
                self.__prefab = None
            return

    def __onPrefabLoaded(self, prefab):
        if not self.isActive:
            CGF.removeGameObject(prefab)
            return
        self.__prefab = prefab