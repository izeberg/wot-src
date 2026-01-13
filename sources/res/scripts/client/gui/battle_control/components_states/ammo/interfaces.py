from __future__ import absolute_import
import typing
if typing.TYPE_CHECKING:
    from gui.battle_control.components_states.ammo.constants import AmmoShootPossibility

class IComponentAmmoState(object):

    def isReloadingBlocked(self):
        raise NotImplementedError

    def canChangeVehicleSetting(self, code):
        raise NotImplementedError

    def canShootValidation(self):
        raise NotImplementedError

    def getShotsAmount(self):
        raise NotImplementedError

    def getShootPossibility(self, currentShells):
        raise NotImplementedError

    def getSpecialReloadMessage(self):
        raise NotImplementedError