from __future__ import absolute_import
import typing
from events_containers.common.containers import IClientEventsContainer
if typing.TYPE_CHECKING:
    from constants import WheeledDashDirection

class IWheeledDashEventsLogic(object):
    onImpulseStarted = None


class IWheeledDashListenerLogic(object):

    def onImpulseStarted(self, direction):
        pass


class IWheeledDashEvents(IClientEventsContainer, IWheeledDashEventsLogic):
    pass