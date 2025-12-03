from typing import TYPE_CHECKING
from Event import Event
from script_component.DynamicScriptComponent import DynamicScriptComponent
if TYPE_CHECKING:
    from grinch_common.grinch_constants import MissileLauncherStatuses

class GrinchLauncherControllerComponent(DynamicScriptComponent):

    def __init__(self):
        super(GrinchLauncherControllerComponent, self).__init__()
        self.onLauncherStateChanged = Event()

    def updateState(self, newState):
        self.cell.updateLauncherState(newState)

    def set_launcherState(self, prev):
        self.onLauncherStateChanged(self.entity.id, self.launcherState)