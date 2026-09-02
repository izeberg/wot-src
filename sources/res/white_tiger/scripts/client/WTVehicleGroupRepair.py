import CGF, functools, GenericComponents, Math
from items import vehicles
from script_component.DynamicScriptComponent import DynamicScriptComponent

class WTVehicleGroupRepair(DynamicScriptComponent):

    def onActivate(self, duration):
        equipment = vehicles.g_cache.equipments().get(self.equipmentID)
        CGF.loadGameObjectIntoHierarchy(equipment.usagePrefab, self.entity.entityGameObject, Math.Vector3(0, 0, 0), functools.partial(self.__onEffectLoaded, duration))

    def __onEffectLoaded(self, duration, go):
        go.createComponent(GenericComponents.RemoveGoDelayedComponent, duration)