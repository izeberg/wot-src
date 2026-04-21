from __future__ import absolute_import
import typing, BigWorld
from constants import LowChargeShotReloadingState
from gui.battle_control.battle_constants import CANT_SHOOT_ERROR
from gui.battle_control.components_states.ammo import DefaultComponentAmmoState, AmmoShootPossibility
from gui.shared.utils.decorators import ReprInjector
from vehicles.mechanics.mechanic_states import IMechanicState

@ReprInjector.simple('reloadingState', 'timeLeft', 'baseTime', 'endTime', 'lowChargeTime')
class LowChargeShotMechanicState(typing.NamedTuple('LowChargeShotMechanicState', (
 (
  'reloadingState', LowChargeShotReloadingState),
 (
  'timeLeft', float),
 (
  'baseTime', float),
 (
  'endTime', float),
 (
  'lowChargeTime', float),
 (
  'almostFinishedTime', float),
 (
  'reloadTimeCoefficient', float))), IMechanicState):

    @classmethod
    def fromComponentStatus(cls, status, params):
        return cls(status.reloadingState, status.timeLeft, status.baseTime, status.endTime, status.lowChargeTime, params.almostFinishedTime, params.reloadTimeCoefficient)

    @property
    def duration(self):
        timeLeftCalculated = self.calculateTimeLeft()
        if self.reloadingState == LowChargeShotReloadingState.INITIAL_RELOAD:
            return self.lowChargeTime - (self.baseTime - timeLeftCalculated)
        if self.reloadingState == LowChargeShotReloadingState.LOW_CHARGE:
            return timeLeftCalculated - self.almostFinishedTime
        if self.reloadingState == LowChargeShotReloadingState.ALMOST_FINISHED:
            return timeLeftCalculated
        if self.reloadingState == LowChargeShotReloadingState.QUICK_RELOAD:
            return timeLeftCalculated
        return self.timeLeft

    def isTransition(self, other):
        return self.reloadingState != other.reloadingState

    def calculateTimeLeft(self):
        return max(0.0, self.endTime - BigWorld.serverTime())


class LowChargeShotAmmoState(DefaultComponentAmmoState):

    def __init__(self, mechanicState):
        self.__mechanicState = mechanicState

    def canShootValidation(self):
        if self.__mechanicState.reloadingState == LowChargeShotReloadingState.ALMOST_FINISHED:
            return (False, CANT_SHOOT_ERROR.LOW_CHARGE_SHOT_BLOCKING)
        return super(LowChargeShotAmmoState, self).canShootValidation()

    def getShootPossibility(self, currentShells):
        if currentShells[0] > 0 and self.__mechanicState.reloadingState in (
         LowChargeShotReloadingState.LOW_CHARGE,
         LowChargeShotReloadingState.FULL_CHARGE):
            return AmmoShootPossibility.ALLOWED
        return AmmoShootPossibility.DENIED