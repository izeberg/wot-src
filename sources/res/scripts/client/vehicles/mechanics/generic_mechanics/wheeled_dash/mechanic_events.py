from __future__ import absolute_import
from events_containers.common.containers import ClientEventsContainer
from vehicles.mechanics.generic_mechanics.wheeled_dash.mechanic_interfaces import IWheeledDashEventsLogic

class WheeledDashStateEvents(ClientEventsContainer, IWheeledDashEventsLogic):

    def __init__(self):
        super(WheeledDashStateEvents, self).__init__()
        self.onImpulseStarted = self._createEvent()