from __future__ import absolute_import
import typing, weakref
from events_containers.common.containers import ClientEventsContainer
from events_containers.components.common import ClientComponentEventsDebugger
from vehicles.mechanics.mechanic_commands.mechanic_interfaces import IMechanicCommandsEventsLogic
if typing.TYPE_CHECKING:
    from vehicles.mechanics.mechanic_constants import VehicleMechanicCommand
    from vehicles.mechanics.mechanic_commands.mechanic_interfaces import IMechanicCommandsComponent

class MechanicCommandsEvents(ClientEventsContainer, IMechanicCommandsEventsLogic):

    def __init__(self, component):
        super(MechanicCommandsEvents, self).__init__()
        self.__componentRef = weakref.ref(component)
        self.onMechanicCommand = self._createEvent()

    def destroy(self):
        self.__componentRef = None
        super(MechanicCommandsEvents, self).destroy()
        return

    def processMechanicCommand(self, command):
        self.onMechanicCommand(command)

    def _getComponent(self):
        if self.__componentRef is not None:
            return self.__componentRef()
        else:
            return

    def _createEventsDebugger(self):
        return MechanicCommandsEventsDebugger(self, self._getComponent())


class MechanicCommandsEventsDebugger(ClientComponentEventsDebugger):
    _EVENTS_DEBUG_PREFIX = 'MECHANIC_CMD'