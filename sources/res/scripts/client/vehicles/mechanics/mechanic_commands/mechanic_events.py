import typing
from Event import SafeEvent
from vehicles.components.component_events import ComponentEvents
from vehicles.mechanics.mechanic_commands.mechanic_interfaces import IMechanicCommandsEventsLogic
if typing.TYPE_CHECKING:
    from vehicles.mechanics.mechanic_constants import VehicleMechanicCommand

class MechanicCommandsEvents(ComponentEvents, IMechanicCommandsEventsLogic):

    def __init__(self):
        super(MechanicCommandsEvents, self).__init__()
        self.onMechanicCommand = SafeEvent(self._eventsManager)

    def processMechanicCommand(self, command):
        self.onMechanicCommand(command)