from __future__ import absolute_import
import typing
from gui.battle_control.components_states.ammo.constants import ActiveAmmoMode, ShellMode
from gui.battle_control.components_states.ammo.interfaces import IAmmoMode

class DefaultAmmoMode(IAmmoMode):

    def getActiveMode(self):
        return ActiveAmmoMode.NOT_DEFINED

    def getModifiedShells(self):
        return ()

    def getShellMode(self, shellIntCD):
        return ShellMode.NOT_DEFINED