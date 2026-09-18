from __future__ import absolute_import, division
import typing, BigWorld
from items.vehicle_mechanics_types import SpecBoostModeMechanicVariant
from gui.shared.utils.decorators import ReprInjector
from vehicles.mechanics.generic_mechanics.spec_boost_mode.mechanic_interfaces import ISpecBoostModeMechanicState, ISpecBoostModeMechanicParams
from vehicles.mechanics.common.mechanic_models import MechanicParamsWithVariants
if typing.TYPE_CHECKING:
    from items.components.shared_components import SpecBoostModeParams

@ReprInjector.withParent()
class SpecBoostModeMechanicParams(ISpecBoostModeMechanicParams, MechanicParamsWithVariants):

    @classmethod
    def fromMechanicParams(cls, params):
        return cls(SpecBoostModeMechanicVariant.fromString(params.mechanicVariant))


class SpecBoostModeMechanicState(ISpecBoostModeMechanicState):

    def __init__(self, state, baseTime, endTime):
        super(SpecBoostModeMechanicState, self).__init__()
        self.__state = state
        self.__baseTime = baseTime
        self.__endTime = endTime

    @classmethod
    def fromComponentStatus(cls, status):
        return cls(status.state, status.baseTime, status.endTime)

    @property
    def progress(self):
        if self.__baseTime > 0:
            return 1.0 - self.timeLeft / self.__baseTime
        return 1.0

    @property
    def timeLeft(self):
        return max(0.0, self.__endTime - BigWorld.serverTime() if self.__endTime >= 0 else self.__baseTime)

    @property
    def state(self):
        return self.__state

    def isTransition(self, other):
        return self.state != other.state