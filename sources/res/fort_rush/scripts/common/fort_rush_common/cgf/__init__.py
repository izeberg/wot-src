from __future__ import absolute_import
from typing import TYPE_CHECKING
import CGF
if TYPE_CHECKING:
    from typing import List, Optional, TypeVar
    from CGF import ComponentAccessor
    T = TypeVar('T')

def getTopMostGO(go):
    if not go.valid:
        return None
    else:
        hierarchyManager = CGF.findHierarchySingleton(go.spaceID)
        if not hierarchyManager:
            return None
        return hierarchyManager.getTopMostParent(go)


def findFirstComponentInHierarchy(root, componentType):
    components = CGF.findInHierarchyWithComponent(root, componentType, True)
    if components:
        return components[0]
    else:
        return