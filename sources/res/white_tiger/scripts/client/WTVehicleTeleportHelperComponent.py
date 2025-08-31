import typing, BigWorld
from script_component.DynamicScriptComponent import DynamicScriptComponent
if typing.TYPE_CHECKING:
    from typing import Any
    from Avatar import Avatar

class WTVehicleTeleportHelperComponent(DynamicScriptComponent):

    def onTeleported(self, *args, **kwargs):
        BigWorld.callback(0.1, self.updateCameraDirection)

    def updateCameraDirection(self):
        player = BigWorld.player()
        arcadeCameraManager = player.inputHandler.ctrls['arcade']
        if arcadeCameraManager:
            arcadeCameraManager.camera.setToVehicleDirection()