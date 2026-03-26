from __future__ import absolute_import
import typing
from events_containers.common.containers import ClientEventsContainerCoreIntegration
if typing.TYPE_CHECKING:
    from events_containers.common.containers.interfaces import IClientEventsContainer

class VehicleComponentEventsCoreIntegration(ClientEventsContainerCoreIntegration):

    def __init__(self, events, component):
        self._spaceID = component.entity.spaceID
        self._vehicleID = component.entity.id
        self._slotName = component.getVehicleSlotName()
        super(VehicleComponentEventsCoreIntegration, self).__init__(events)

    def _attachToEventsContainer(self, events):
        self.lateSubscribeTo(events)