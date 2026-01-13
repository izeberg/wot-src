from __future__ import absolute_import
import typing
from typing import Set, Optional
if typing.TYPE_CHECKING:
    from items.vehicles import VehicleDescr
    from vehicles.mechanics.mechanic_constants import VehicleMechanic
    VehicleModule = typing.TypeVar('VehicleModule')

class IMechanicFactory(object):

    @classmethod
    def getMechanics(cls, guiItem, vehDescr, mechanics, withOverrides=False):
        raise NotImplementedError