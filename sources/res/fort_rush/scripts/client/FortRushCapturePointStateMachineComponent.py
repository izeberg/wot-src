from __future__ import absolute_import
from cgf_client_common.entity_dyn_components import ReplicableDynamicScriptComponent
from fort_rush_common.fort_rush_constants import CaptureStates

class FortRushCapturePointStateMachineComponent(ReplicableDynamicScriptComponent):

    def __init__(self):
        super(FortRushCapturePointStateMachineComponent, self).__init__()
        self.state = CaptureStates.NEUTRAL.value