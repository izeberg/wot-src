import typing, BigWorld
from constants import ExtraShotClipStates
from vehicles.mechanics.mechanic_constants import VehicleMechanic
from vehicles.mechanics.mechanic_helpers import getVehicleMechanic
if typing.TYPE_CHECKING:
    from Vehicle import Vehicle

def getVehicleExtraShotController(vehicle):
    return getVehicleMechanic(VehicleMechanic.EXTRA_SHOT_CLIP, vehicle)


class ExtraShotState(typing.NamedTuple('ExtraShotState', (('reloadState', int),))):

    def isReloadAfterShot(self, timeLeft, baseTime):
        if self.reloadState & ExtraShotClipStates.EXTRA_FULL_RELOAD:
            return self.reloadState & ExtraShotClipStates.FULL_RELOAD_WITH_EXTRA_TIME
        return timeLeft == baseTime


class ExtraShotClipComponent(BigWorld.DynamicScriptComponent):

    def getMechanicState(self):
        return ExtraShotState(self.reloadState)