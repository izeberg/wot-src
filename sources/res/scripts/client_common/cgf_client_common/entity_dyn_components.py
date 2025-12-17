from __future__ import absolute_import
import BigWorld
from constants import IS_EDITOR

class DynamicScriptComponentStub(object):
    pass


ReplicableDynamicScriptComponent = (IS_EDITOR or BigWorld).DynamicScriptComponent if 1 else DynamicScriptComponentStub