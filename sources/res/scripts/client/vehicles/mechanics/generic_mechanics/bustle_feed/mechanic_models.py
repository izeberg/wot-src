from __future__ import absolute_import, division
import typing
from collections import namedtuple
import BigWorld
from constants import BUSTLE_FEED_STATE, VEHICLE_SETTING, BUSTLE_FEED_SWITCH_ACCESS
from vehicles.mechanics.mechanic_states import IMechanicState
from gui.battle_control.components_states.ammo import DefaultComponentAmmoState
from gui.battle_control.components_states.ammo.constants import ActiveAmmoMode, ShellMode
from gui.battle_control.components_states.ammo.shells import DefaultAmmoMode
from gui.shared.utils.decorators import ReprInjector
if typing.TYPE_CHECKING:
    from items.components.shared_components import BustleFeedParams
    from items.vehicles import VehicleDescriptor

@ReprInjector.simple('activationTime', 'modifiedShells', 'shotReloadFactor')
class BustleFeedComponentParams(object):

    def __init__(self, activationTime, modifiedShells, shotReloadFactor):
        super(BustleFeedComponentParams, self).__init__()
        self.__activationTime = activationTime
        self.__modifiedShells = modifiedShells
        self.__shotReloadFactor = shotReloadFactor

    @classmethod
    def fromMechanicParams(cls, params, vehDescr):
        modifiedShells = tuple(shot.shell.compactDescr for idx, shot in enumerate(vehDescr.gun.shots) if idx in params.bustleShotsIndices)
        return cls(params.activationTime, modifiedShells, params.bustleShotReloadFactor)

    @property
    def modifiedShells(self):
        return self.__modifiedShells

    @property
    def activationTime(self):
        return self.__activationTime

    @property
    def shotReloadFactor(self):
        return self.__shotReloadFactor


class BustleFeedState(namedtuple('BustleFeedState', ('state', 'baseTime', 'endTime', 'switchAccessState')), IMechanicState):

    def isTransition(self, other):
        return self.state != other.state

    def isSwitchState(self):
        return self.state in (BUSTLE_FEED_STATE.ACTIVATION, BUSTLE_FEED_STATE.DEACTIVATION)

    @property
    def progress(self):
        if self.baseTime > 0:
            return 1.0 - self.timeLeft / self.baseTime
        return 1.0

    @property
    def timeLeft(self):
        return max(0.0, self.endTime - BigWorld.serverTime() if self.endTime >= 0 else self.baseTime)


class BustleFeedAmmoMode(DefaultAmmoMode):

    def __init__(self, mechanicState, modifiedShells):
        self.__mechanicState = mechanicState
        self.__modifiedShells = modifiedShells

    @property
    def isActiveBustleFeed(self):
        return self.__mechanicState.state in (BUSTLE_FEED_STATE.ACTIVE, BUSTLE_FEED_STATE.DEACTIVATION)

    @property
    def isBustleFeedReloadModifierActive(self):
        return self.__mechanicState.state in (BUSTLE_FEED_STATE.ACTIVATION, BUSTLE_FEED_STATE.ACTIVE)

    def getActiveMode(self):
        if self.isActiveBustleFeed:
            return ActiveAmmoMode.MODIFIED_SHELLS
        return ActiveAmmoMode.DEFAULT_SHELLS

    def getModifiedShells(self):
        return self.__modifiedShells

    def getShellMode(self, shellIntCD):
        if self.isBustleShotShell(shellIntCD):
            return ShellMode.BUSTLE_FEED
        return ShellMode.NOT_DEFINED

    def isBustleShotShell(self, shellIntCD):
        return shellIntCD in self.__modifiedShells


class BustleFeedAmmoState(DefaultComponentAmmoState):

    def __init__(self, mechanicState, modifiedShells, shotReloadFactor):
        self.__mechanicState = mechanicState
        self.__ammoMode = BustleFeedAmmoMode(mechanicState, modifiedShells)
        self.__shotReloadFactor = shotReloadFactor

    def canChangeVehicleSetting(self, code):
        if code == VEHICLE_SETTING.CURRENT_SHELLS:
            return self.__canChangeCurrentShell()
        return super(BustleFeedAmmoState, self).canChangeVehicleSetting(code)

    def getAmmoMode(self):
        return self.__ammoMode

    def getShellReloadTimes(self, currShell, shellChangeTime, shells):
        if not self.__ammoMode.isBustleFeedReloadModifierActive:
            return [shellChangeTime] * len(shells)
        isBustleShot = self.__ammoMode.isBustleShotShell
        baseChangeTime = shellChangeTime / self.__shotReloadFactor if isBustleShot(currShell) else shellChangeTime
        return [ baseChangeTime * self.__shotReloadFactor if isBustleShot(shell) else baseChangeTime for shell in shells
               ]

    def __canChangeCurrentShell(self):
        if self.__mechanicState.isSwitchState() or BUSTLE_FEED_SWITCH_ACCESS.isLocked(self.__mechanicState.switchAccessState):
            return False
        return True