from __future__ import absolute_import
from typing import TYPE_CHECKING
import CGF
from event_platform.respawns.respawns import RespawnPolicySystem
if TYPE_CHECKING:
    from typing import Any, Optional, Type

def getRespawnPolicyComponent(spaceID, vehicleId, componentType):
    system = CGF.getSystem(spaceID, RespawnPolicySystem)
    if system is None:
        return
    else:
        policyGO = system.findPolicyGameObject(vehicleId)
        if policyGO is not None:
            return policyGO.findRead(componentType)
        return