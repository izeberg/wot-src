from Event import EventManager, SafeEvent
from vehicles.components.component_events.events_interfaces import IComponentEvents

class ComponentEvents(IComponentEvents):

    def __init__(self):
        super(ComponentEvents, self).__init__()
        self._eventsManager = EventManager()
        self.onComponentEventsDestroy = SafeEvent(self._eventsManager)

    def destroy(self):
        self.onComponentEventsDestroy(self)
        self._eventsManager.clear()
        super(ComponentEvents, self).destroy()