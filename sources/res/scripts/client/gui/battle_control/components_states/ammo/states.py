from __future__ import absolute_import
import typing
from gui.battle_control.battle_constants import CANT_SHOOT_ERROR
from gui.battle_control.components_states.ammo.constants import AmmoShootPossibility
from gui.battle_control.components_states.ammo.interfaces import IComponentAmmoState

class DefaultComponentAmmoState(IComponentAmmoState):

    def isReloadingBlocked(self):
        return False

    def canChangeVehicleSetting(self, code):
        return True

    def canShootValidation(self):
        return (
         True, CANT_SHOOT_ERROR.UNDEFINED)

    def getShotsAmount(self):
        return -1

    def getShootPossibility(self, currentShells):
        return AmmoShootPossibility.NOT_DEFINED

    def getSpecialReloadMessage(self):
        return