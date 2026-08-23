from __future__ import absolute_import
import typing, CommandMapping
from AvatarInputHandler.commands.input_handler_command import InputHandlerCommand
from vehicles.mechanics.mechanic_helpers import getPlayerVehicleMechanicComponent
if typing.TYPE_CHECKING:
    from vehicles.mechanics.mechanic_constants import VehicleMechanic

class SightPointerActivationControl(InputHandlerCommand):

    def __init__(self, mechanic):
        self.__mechanic = mechanic

    def handleKeyEvent(self, isDown, key, mods, event=None):
        if not isDown or not CommandMapping.g_instance.isFired(CommandMapping.CMD_CM_SPECIAL_ABILITY, key):
            return False
        mechanicComponent = getPlayerVehicleMechanicComponent(self.__mechanic)
        if mechanicComponent is not None:
            mechanicComponent.alternateOnState()
        return True


def createSightPointerActivationControl(mechanic, *_, **__):
    return SightPointerActivationControl(mechanic)