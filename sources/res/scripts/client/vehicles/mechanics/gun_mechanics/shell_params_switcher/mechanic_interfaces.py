from __future__ import absolute_import
import typing
from vehicles.mechanics.mechanic_states import IMechanicState
if typing.TYPE_CHECKING:
    from items.components.shared_components import ShellSwitcherParams

class IShellParamsSwitcherComponentParams(object):

    @classmethod
    def fromMechanicParams(cls, params, vehIntCD):
        raise NotImplementedError

    @property
    def shellSubtypes(self):
        raise NotImplementedError


class IShellParamsSwitcherMechanicState(IMechanicState):

    @property
    def state(self):
        raise NotImplementedError

    @property
    def baseState(self):
        raise NotImplementedError

    @property
    def isActive(self):
        raise NotImplementedError

    @property
    def lastActiveShotTimestamp(self):
        raise NotImplementedError

    @property
    def mechanicSubtype(self):
        raise NotImplementedError

    def isNoAmmo(self):
        raise NotImplementedError

    def isCritState(self):
        raise NotImplementedError

    def timeLeft(self):
        raise NotImplementedError