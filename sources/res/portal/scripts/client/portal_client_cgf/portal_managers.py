import CGF, Math
from cgf_script.managers_registrator import onRemovedQuery
from portal_client_cgf.portal_components import SpawnSound3DOnRemove
from portal_common_cgf.portal_helpers import registerPortalManager

@registerPortalManager(CGF.DomainOption.DomainClient)
class SpawnSound3DOnRemoveManager(CGF.ComponentManager):

    @onRemovedQuery(CGF.GameObject, SpawnSound3DOnRemove)
    def onSpawnSound3DOnRemoveRemoved(self, go, spawnSound3DOnRemoveComponent):
        hm = CGF.HierarchyManager(self.spaceID)
        parentGO = hm.getParent(go)
        prefabPath = spawnSound3DOnRemoveComponent.prefabPath
        CGF.loadGameObjectIntoHierarchy(prefabPath, parentGO, Math.Vector3(0, 0, 0))