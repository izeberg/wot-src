import typing, logging
from events_handler import eventHandler
from vehicles.components.component_events import ComponentListener
from vehicles.mechanics.mechanic_commands.mechanic_interfaces import IMechanicCommandsListenerLogic
if typing.TYPE_CHECKING:
    from vehicles.mechanics.mechanic_commands.mechanic_interfaces import IMechanicCommandsEvents
    from vehicles.mechanics.mechanic_constants import VehicleMechanicCommand
_logger = logging.getLogger(__name__)

class MechanicCommandsLogger(ComponentListener, IMechanicCommandsListenerLogic):

    @eventHandler
    def onComponentEventsDestroy(self, events):
        _logger.debug('onComponentEventsDestroy %s', events)
        super(MechanicCommandsLogger, self).onComponentEventsDestroy(events)

    @eventHandler
    def onMechanicCommand(self, command):
        _logger.debug('onMechanicCommand %s', command)