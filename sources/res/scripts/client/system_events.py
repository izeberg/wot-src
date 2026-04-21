from __future__ import absolute_import
from events_container import EventsContainer

class SystemEvents(EventsContainer):

    def __init__(self):
        super(SystemEvents, self).__init__()
        self.onBeforeSend = self._createEvent()
        self.onDependencyConfigReady = self._createEvent()


g_systemEvents = SystemEvents()