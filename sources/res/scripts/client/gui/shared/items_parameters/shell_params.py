from __future__ import absolute_import, division
import math, typing
from enum import IntEnum
from collections import OrderedDict
from future.utils import iteritems
from past.utils import old_div
from constants import SHELL_TYPES, SHELL_MECHANICS_TYPE
from gui.shared.items_parameters import calcShellParams, getShellDescriptors, NO_DATA, isShellCalibration, isBustleFeedShotGun
from gui.shared.items_parameters.base_params import CompatibleParams, ParamsDictProxy
from gui.shared.items_parameters.functions import isStunParamVisible, getBasicShell, getBustleFeedDamage, getShellCalibrationDamage, getShellCalibrationPiercingPower
from gui.shared.items_parameters.params_constants import AUTOCANNON_SHOT_DISTANCE, PIERCING_DISTANCES, EPSILON
from gui.shared.utils import AVG_DAMAGE_PER_SECOND, DAMAGE_PROP_NAME, PIERCING_POWER_PROP_NAME, NORMALIZATION_ANGLE, RICOCHET_ANGLE, CRITICAL_HIT_CHANCE, PENETRATION_LOSS
from gui.shared.utils.functions import getShellImpactParams
from items import vehicles
from items.components.component_constants import MODERN_HE_PIERCING_POWER_REDUCTION_FACTOR_FOR_SHIELDS
from helpers_common import computePiercingPowerAtDist
from math_common import round_py2_style, round_py2_style_int
from vehicles.mechanics.mechanic_constants import VehicleMechanic
if typing.TYPE_CHECKING:
    from typing import Optional
BASE_SHELL_PARAMETERS = (
 'avgDamage',
 AVG_DAMAGE_PER_SECOND,
 'avgPiercingPower',
 'shotSpeed',
 'explosionRadius',
 'stunDurationList')

def _isDifferentValues(paramName, parameters):
    value = parameters[0][1].get(paramName)
    return any(paramGroup[1].get(paramName) != value for paramGroup in parameters)


SHELL_MECHANIC_ADDITIONAL_PARAMETERS = {VehicleMechanic.SHELL_PARAMS_SWITCHER: OrderedDict([
                                         (
                                          NORMALIZATION_ANGLE, _isDifferentValues),
                                         (
                                          RICOCHET_ANGLE, _isDifferentValues),
                                         (
                                          PENETRATION_LOSS, _isDifferentValues),
                                         (
                                          CRITICAL_HIT_CHANCE, _isDifferentValues)])}

def getMechanicParameters(mechanic, parameters):
    mechanicParams = SHELL_MECHANIC_ADDITIONAL_PARAMETERS.get(mechanic)
    if mechanicParams is None:
        return ()
    else:
        return tuple(paramName for paramName, validator in iteritems(mechanicParams) if validator(paramName, parameters))


class CriticalHitChanceType(IntEnum):
    STANDARD = 1
    DECREASED = 2
    INCREASED = 3


_SHELL_KINDS = (
 SHELL_TYPES.HOLLOW_CHARGE, SHELL_TYPES.HIGH_EXPLOSIVE,
 SHELL_TYPES.ARMOR_PIERCING, SHELL_TYPES.ARMOR_PIERCING_HE, SHELL_TYPES.ARMOR_PIERCING_CR)

def _average(listOfNumbers):
    return old_div(sum(listOfNumbers), len(listOfNumbers))


class ShellParams(CompatibleParams):

    @property
    def caliber(self):
        return self._itemDescr.caliber

    @property
    def piercingPower(self):
        piercingPower = self._getRawParams()[PIERCING_POWER_PROP_NAME]
        shot = self.__getShellDescriptor()
        if shot is None:
            return piercingPower
        else:
            if isShellCalibration(self._vehicleDescr):
                return [ getShellCalibrationPiercingPower(self._vehicleDescr, shot.shell, piercingPower) for piercingPower in piercingPower
                       ]
            return piercingPower

    @property
    def damage(self):
        return self._getRawParams()[DAMAGE_PROP_NAME]

    @property
    def avgDamage(self):
        damage = self._itemDescr.armorDamage[0]
        shot = self.__getShellDescriptor()
        if shot is None:
            return damage
        else:
            if isShellCalibration(self._vehicleDescr):
                return round_py2_style_int(getShellCalibrationDamage(self._vehicleDescr, shot.shell))
            if isBustleFeedShotGun(self._vehicleDescr):
                return getBustleFeedDamage(self._vehicleDescr, shot.shell, shot.shell.armorDamage[0])
            return shot.shell.armorDamage[0]

    @property
    def avgMutableDamage(self):
        if self._itemDescr.isDamageMutable:
            return self._itemDescr.armorDamage
        else:
            return

    @property
    def avgDamagePerSecond(self):
        if self._vehicleDescr and self._vehicleDescr.isAutoShootGunVehicle:
            return round_py2_style(float(self.avgDamage) / self._vehicleDescr.gun.clip[1])
        else:
            return

    @property
    def avgPiercingPower(self):
        return round_py2_style_int(_average(self.piercingPower))

    @property
    def explosionRadius(self):
        if self._itemDescr.kind == SHELL_TYPES.HIGH_EXPLOSIVE:
            return self.__getShellType().explosionRadius
        return 0

    @property
    def piercingPowerTable(self):
        if self._itemDescr.kind in (SHELL_TYPES.ARMOR_PIERCING, SHELL_TYPES.ARMOR_PIERCING_CR):
            if self._vehicleDescr is None:
                return NO_DATA
            result = []
            shellDescriptor = self.__getShellDescriptor()
            if not shellDescriptor:
                return
            maxDistance = self.maxShotDistance
            shellCalibrationGun = isShellCalibration(self._vehicleDescr)
            for distance in PIERCING_DISTANCES:
                if distance > maxDistance:
                    distance = int(maxDistance)
                currPiercing = computePiercingPowerAtDist(shellDescriptor.piercingPower, distance)
                if shellCalibrationGun:
                    result.append((distance,
                     round_py2_style_int(getShellCalibrationPiercingPower(self._vehicleDescr, shellDescriptor.shell, currPiercing))))
                else:
                    result.append((distance, currPiercing))

            return result
        return

    @property
    def maxShotDistance(self):
        if self._itemDescr.kind in _SHELL_KINDS:
            result = self.__getShellDescriptor()
            if result:
                return result.maxDistance
        return

    @property
    def isBasic(self):
        return self._vehicleDescr is not None and getBasicShell(self._vehicleDescr).compactDescr == self._itemDescr.compactDescr

    @property
    def compatibles(self):
        getter = vehicles.getItemByCompactDescr
        overallList = [ getter(gunCD).userString for gunCD in self._getPrecachedInfo().guns ]
        uniques = []
        for weapon in overallList:
            if weapon not in uniques:
                uniques.append(weapon)

        return uniques

    @property
    def stunMaxDuration(self):
        if self._itemDescr.hasStun:
            return self._itemDescr.stun.stunDuration
        else:
            return

    @property
    def stunMinDuration(self):
        if self._itemDescr.hasStun:
            return self._itemDescr.stun.guaranteedStunDuration * self._itemDescr.stun.stunDuration
        else:
            return

    @property
    def stunDurationList(self):
        if self._itemDescr.hasStun:
            return (self.stunMinDuration, self.stunMaxDuration)
        else:
            return

    @property
    def shotSpeed(self):
        shot = self.__getShellDescriptor()
        if shot is None or self._itemDescr.kind not in _SHELL_KINDS:
            return
        projSpeedFactor = vehicles.g_cache.commonConfig['miscParams']['projectileSpeedFactor']
        shotSpeed = shot.speed / projSpeedFactor
        return shotSpeed

    @property
    def normalizationAngle(self):
        _, normalizationAngle, _, _ = getShellImpactParams(self.__getShellType())
        return round_py2_style_int(math.degrees(normalizationAngle))

    @property
    def ricochetAngle(self):
        ricochetAngleCos, _, _, _ = getShellImpactParams(self.__getShellType())
        return round_py2_style_int(math.degrees(math.acos(ricochetAngleCos)))

    @property
    def penetrationLoss(self):
        shellType = self.__getShellType()
        if not hasattr(shellType, 'piercingPowerLossFactorByDistance'):
            return None
        else:
            return round_py2_style_int(shellType.piercingPowerLossFactorByDistance * 10 + EPSILON)

    @property
    def screensArmorMultiplier(self):
        if not self.__isModernHE():
            return None
        else:
            return int(MODERN_HE_PIERCING_POWER_REDUCTION_FACTOR_FOR_SHIELDS)

    @property
    def criticalHitChance(self):
        if not self._itemDescr.isArmorPercingType:
            return
        else:
            shot = self.__getShellDescriptor()
            if shot is None:
                return
            modifier = shot.shell.chanceToHitByProjectileModifier
            if modifier == 1.0:
                return CriticalHitChanceType.STANDARD
            if modifier > 1.0:
                return CriticalHitChanceType.INCREASED
            return CriticalHitChanceType.DECREASED

    def getParamsDict(self):
        stunConditionParams = ('stunMaxDuration', 'stunMinDuration')
        return ParamsDictProxy(self, conditions=((['maxShotDistance'], lambda v: v == AUTOCANNON_SHOT_DISTANCE),
         (
          stunConditionParams, lambda s: isStunParamVisible(self._itemDescr))))

    def _extractRawParams(self):
        if self._vehicleDescr is not None:
            descriptors = getShellDescriptors(self._itemDescr, self._vehicleDescr)
            params = calcShellParams(descriptors)
        else:
            params = self._getPrecachedInfo().params
        return params

    def _getCompatible(self):
        return (
         (
          'shellGuns', (', ').join(self.compatibles)),)

    def __isModernHE(self):
        shellType = self.__getShellType()
        return shellType.name == SHELL_TYPES.HIGH_EXPLOSIVE and shellType.mechanics == SHELL_MECHANICS_TYPE.MODERN

    def __getShellDescriptor(self):
        if self._vehicleDescr is None:
            return
        else:
            shellDescriptors = getShellDescriptors(self._itemDescr, self._vehicleDescr)
            if shellDescriptors:
                return shellDescriptors[0]
            return

    def __getShellType(self):
        shot = self.__getShellDescriptor()
        if shot is None:
            return self._itemDescr.type
        else:
            return shot.shell.type