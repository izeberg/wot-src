import logging, typing, BigWorld, CGF, Event
from constants import ARENA_PERIOD
from script_component.DynamicScriptComponent import DynamicScriptComponent
from grinch_common.shared_helpers import splitVehiclePresentPoints
if typing.TYPE_CHECKING:
    from typing import List, Tuple
    from Vehicle import Vehicle
_logger = logging.getLogger(__name__)

def _diff(old, new):
    diff = {}
    for nkey, nval in new.iteritems():
        oval = old.get(nkey)
        if nval != oval:
            diff[nkey] = nval

    return diff


class GrinchScoreComponent(DynamicScriptComponent):

    def __init__(self):
        super(GrinchScoreComponent, self).__init__()
        self.onTeamScoreUpdated = Event.Event()
        self.onVehiclePointsUpdated = Event.Event()
        self.onVehiclesTotalScoreUpdated = Event.Event()

    def _onAvatarReady(self):
        arena = BigWorld.player().arena
        if arena.period >= ARENA_PERIOD.BATTLE:
            self.set_teamScore({})
            self.set_vehiclePoints({})
            self.set_vehicleTotalScore({})

    def onDestroy(self):
        super(GrinchScoreComponent, self).onDestroy()
        self.onTeamScoreUpdated.clear()
        self.onVehiclePointsUpdated.clear()
        self.onVehiclesTotalScoreUpdated.clear()

    def getVehiclePoints(self, vehicleID):
        return splitVehiclePresentPoints(self.getVehiclePresents(vehicleID))

    def getVehiclePresents(self, vehicleID):
        return self.vehiclePoints.get(vehicleID, [])

    def getVehicleLimit(self, vehicle):
        subset = self.vehicleLimits.viewkeys() & vehicle.typeDescriptor.type.tags
        if subset:
            return self.vehicleLimits.get(list(subset).pop(), 0)
        return 0

    def getVehicleTotalScore(self, vehicleID):
        return self.vehicleTotalScore.get(vehicleID, 0)

    def set_teamScore(self, _):
        self.onTeamScoreUpdated(self.teamScore)

    def set_vehiclePoints(self, prev):
        for vehID, presents in self.vehiclePoints.iteritems():
            vehicle = BigWorld.entities.get(vehID)
            if vehicle:
                hierarchy = CGF.HierarchyManager(self.spaceID)
                from grinch.cgf.presents import PresentStackComponent
                for go, comp in hierarchy.findComponentsInHierarchy(vehicle.appearance.gameObject, PresentStackComponent):
                    comp.setCounter(go, presents)

        diff = _diff(prev, self.vehiclePoints)
        if diff:
            self.onVehiclePointsUpdated(diff)

    def set_vehicleTotalScore(self, prev):
        diff = _diff(prev, self.vehicleTotalScore)
        if diff:
            self.onVehiclesTotalScoreUpdated(diff)