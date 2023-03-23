from typing import TYPE_CHECKING, Dict, List, Tuple
import tankmen
from constants import PerkData, CrewContextArgs, SkillProcessorArgs, GroupSkillProcessorArgs, CHANCE_TO_HIT_SUFFIX_FACTOR
from debug_utils import *
from items.combined_crew_skill import CombinedCrewSkill
from items.components.skills_constants import ROLES_BY_SKILLS
from items.utils import isclose
from items.vehicles import TANKMAN_EXTRA_NAMES
from soft_exception import SoftException
if TYPE_CHECKING:
    from items.artefacts import SkillEquipment
_DO_DEBUG_LOG = False
CREW_CONTEXT_FORCE_UPDATE_INDEX = -29222
_ADDITIVE_FACTORS = frozenset(ten + CHANCE_TO_HIT_SUFFIX_FACTOR for ten in TANKMAN_EXTRA_NAMES)

class VehicleDescrCrew(object):

    def __init__(self, vehicleDescr, crewCompactDescrs, activityFlags=None, isFire=False, defaultSixthSenseDisabled=False):
        if activityFlags is None:
            activityFlags = [
             True] * len(crewCompactDescrs)
        self._vehicleDescr = vehicleDescr
        self._crewCompactDescrs = crewCompactDescrs
        self._activityFlags = activityFlags
        self._isFire = isFire
        self._defaultSixthSenseDisabled = defaultSixthSenseDisabled
        skills, self._perks = self._validateAndComputeCrew()
        self._skills = skills
        if _DO_DEBUG_LOG:
            items = skills.iteritems()
            for skillName, skillData in sorted(items, cmp=lambda x, y: cmp(x[0], y[0])):
                LOG_DEBUG("TankmanIdxs/levels with skill '%s': %s" % (skillName, str(skillData)))

        self._commanderIdx = skills['commander'][0][0]
        self.__factorsDirty = True
        self._levelIncreaseByVehicle = 0.0
        self._levelIncreaseByBrotherhood = 0.0
        self._affectingFactors = {'crewRolesFactor': 1.0, 
           'radioDistanceFactor': 0.0}
        self._camouflageFactor = 1.0
        self._boostedSkills = {}
        self._useCachedLevelIncrease = False
        self.lastUsedLevels = {}
        return

    def boostSkillBy(self, equipment):
        self._boostedSkills[equipment.skillName] = equipment
        self._factorsDirty = True

    def discardSkillBoostBy(self, equipment):
        skill = self._boostedSkills.get(equipment.skillName)
        if skill is None:
            LOG_ERROR('Failed to discard skill (arenaUniqueID, vehicleID, skillName):', self.__getUniqueArenaID(), self.__getVehicleID(), equipment.skillName, stack=True)
            return
        else:
            del self._boostedSkills[equipment.skillName]
            self._factorsDirty = True
            return

    def callSkillProcessor(self, skillName, *args):
        try:
            skillProcessor = self._skillProcessors.get(skillName)
            if skillProcessor is None:
                return
            equipment = self._boostedSkills.get(skillName)
            if equipment is not None:
                equipment.updateCrewSkill(*args)
            skillProcessor(self, *args)
        except:
            LOG_ERROR('Failed to process skill (arenaUniqueID, vehicleID, skillName, skillData):', self.__getUniqueArenaID(), self.__getVehicleID(), skillName, self._skills[skillName], stack=True)
            LOG_CURRENT_EXCEPTION()

        return

    @property
    def skills(self):
        return self._skills

    @property
    def camouflageFactor(self):
        if self._factorsDirty:
            self._buildFactors()
        return self._camouflageFactor

    @property
    def _factorsDirty(self):
        return self.__factorsDirty

    @_factorsDirty.setter
    def _factorsDirty(self, necessity):
        self.__factorsDirty = necessity

    @property
    def useCachedLevelIncrease(self):
        return self._useCachedLevelIncrease

    @useCachedLevelIncrease.setter
    def useCachedLevelIncrease(self, value):
        self._useCachedLevelIncrease = value

    def isCrewActive(self):
        return True in self._activityFlags

    def recomputeSkill(self, skillName):
        for idxInCrew, level in self._skills.get(skillName, ()):
            if self._activityFlags[idxInCrew]:
                self._factorsDirty = True
                break

    def onCollectShotDispersionFactors(self, factors):
        if self._factorsDirty:
            self._buildFactors()
        factors[0] *= self._shotDispFactor

    def onCollectFactors(self, factors):
        newLevelIncreaseByVehicle = factors['crewLevelIncrease'] + self._vehicleDescr.miscAttrs['crewLevelIncrease']
        if self._levelIncreaseByVehicle != newLevelIncreaseByVehicle:
            self._levelIncreaseByVehicle = newLevelIncreaseByVehicle
            if hasattr(self, '_vehicle') and not self._useCachedLevelIncrease:
                self._vehicle.events.onTankmanStatusChanged(self._vehicle, CREW_CONTEXT_FORCE_UPDATE_INDEX)
            self._factorsDirty = True
        for key, factor in self._affectingFactors.iteritems():
            if not isclose(factors[key], factor):
                self._affectingFactors.update((k, factors[k]) for k in self._affectingFactors.iterkeys())
                self._factorsDirty = True
                break

        if self._factorsDirty:
            self._buildFactors()
        for name, value in self._factors.iteritems():
            try:
                if name in _ADDITIVE_FACTORS:
                    factors[name] += value
                else:
                    factors[name] *= value
            except:
                pass

        try:
            r = factors['chassis/terrainResistance']
            value = self._terrainResistanceFactors
            r[0] *= value[0]
            r[1] *= value[1]
            r[2] *= value[2]
        except:
            pass

    def saveLastUsedPerkLevel(self, perkID, level):
        skillName = tankmen.getSkillsConfig().vsePerkToSkill.get(perkID)
        self.lastUsedLevels[skillName] = level

    def _calcLeverIncreaseForNonCommander(self, commonLevelIncrease):
        if not self._activityFlags[self._commanderIdx]:
            levelIncreaseByCommander = 0.0
        else:
            commanderLevel = self._skills['commander'][0][1] + commonLevelIncrease
            levelIncreaseByCommander = commanderLevel / tankmen.COMMANDER_ADDITION_RATIO
        result = commonLevelIncrease + levelIncreaseByCommander
        if _DO_DEBUG_LOG:
            LOG_DEBUG(('levelIncreaseByCommander={}').format(levelIncreaseByCommander))
            LOG_DEBUG(('nonCommanderLeverIncrease={}').format(result))
        return result

    def _buildFactors(self):
        self._factors = {}
        self._shotDispFactor = 1.0
        self._terrainResistanceFactors = [1.0, 1.0, 1.0]
        self._levelIncreaseByBrotherhood = self._calculateLevelIncreaseByBrotherhood()
        commonLevelIncrease = self._levelIncreaseByBrotherhood + self._levelIncreaseByVehicle
        nonCommanderLevelIncrease = self._calcLeverIncreaseForNonCommander(commonLevelIncrease)
        if _DO_DEBUG_LOG:
            LOG_DEBUG(('Crew level increase by vehicle={}, by brotherhood={}').format(self._levelIncreaseByVehicle, self._levelIncreaseByBrotherhood))
        skillEfficiencies = self._calculateSkillEfficiencies(commonLevelIncrease, nonCommanderLevelIncrease)
        self._processSkills(skillEfficiencies, commonLevelIncrease, nonCommanderLevelIncrease)
        self._factorsDirty = False

    def _calculateLevelIncreaseByBrotherhood(self):
        value = 0.0
        if self._isFire:
            return value
        else:
            skillData = self._skills.get('brotherhood')
            if skillData is None:
                return value
            broSum = 0
            for crewIdx, level in skillData:
                if self._activityFlags[crewIdx]:
                    broSum += level

            broLevel = broSum / (len(self._crewCompactDescrs) * tankmen.MAX_SKILL_LEVEL)
            return broLevel * tankmen.getSkillsConfig().getSkill('brotherhood').crewLevelIncrease

    def _calculateSkillEfficiencies(self, commonLevelIncrease, nonCommanderLevelIncrease):
        skills = self._skills
        isFire = self._isFire
        MAX_SKILL_LEVEL = tankmen.MAX_SKILL_LEVEL
        skillEfficiencies = []
        universalistAddition = self._calculateUniversalistAddition(commonLevelIncrease)
        self._updateCommanderUniversalistNotifications(universalistAddition)
        computeSummSkillLevel = self._computeSummSkillLevel
        llen = len
        for skillName in tankmen.ROLES:
            if isFire:
                efficiency = 0.0
                baseAvgLevel = 0.0
            else:
                skillData = skills[skillName]
                baseSummLevel, summLevel, numInactive = computeSummSkillLevel(skillData, nonCommanderLevelIncrease=nonCommanderLevelIncrease, commanderLevelIncrease=commonLevelIncrease)
                summLevel += numInactive * universalistAddition
                skillDataLen = llen(skillData)
                avgLevel = summLevel / skillDataLen
                efficiency = avgLevel / MAX_SKILL_LEVEL
                baseAvgLevel = baseSummLevel / skillDataLen
            skillEfficiencies.append((skillName, efficiency, baseAvgLevel))

        crewCompactDescrsLen = llen(self._crewCompactDescrs)
        crewCompactDescrsLenMaxSkillLev = crewCompactDescrsLen * MAX_SKILL_LEVEL
        for skillName in ('repair', 'camouflage'):
            skillData = skills.get(skillName)
            if skillData is None or isFire:
                efficiency = 0.0
                baseAvgLevel = 0.0
            else:
                baseSummLevel, summLevel, numInactive = computeSummSkillLevel(skillData, nonCommanderLevelIncrease=nonCommanderLevelIncrease, commanderLevelIncrease=commonLevelIncrease)
                efficiency = summLevel / crewCompactDescrsLenMaxSkillLev
                baseAvgLevel = baseSummLevel / crewCompactDescrsLen
            skillEfficiencies.append((skillName, efficiency, baseAvgLevel))

        return skillEfficiencies

    def _calculateUniversalistAddition(self, commonLevelIncrease):
        universalistAddition = 0
        if self._isFire or not self._activityFlags[self._commanderIdx]:
            return universalistAddition
        numInactive = self._activityFlags.count(False)
        if numInactive:
            skillData = self._skills.get('commander_universalist')
            if skillData is not None:
                level = skillData[0][1]
                universalistAddition = (level + commonLevelIncrease) / numInactive
                universalistAddition *= tankmen.getSkillsConfig().getSkill('commander_universalist').efficiency
        return universalistAddition

    def _processSkills(self, skillEfficiencies, commonLevelIncrease, nonCommanderLevelIncrease):
        skills = self._skills
        isFire = self._isFire
        getSkill = tankmen.getSkillsConfig().getSkill
        skillToBoost = set(self._boostedSkills.iterkeys())
        callSkillProcessor = self.callSkillProcessor
        for skillName, efficiency, baseAvgLevel in skillEfficiencies:
            self.lastUsedLevels[skillName] = efficiency * 100
            factor = 0.57 + 0.43 * efficiency
            skillToBoost.discard(skillName)
            callSkillProcessor(skillName, GroupSkillProcessorArgs(factor, baseAvgLevel))

        for skillName, skillData in skills.iteritems():
            if skillName in tankmen.ROLES_AND_COMMON_SKILLS:
                continue
            skillConfig = getSkill(skillName)
            perkID = skillConfig.vsePerk
            perkData = self._perks.get(perkID)
            ccs = self._findBestTankmanForSkill({'crew': skillData} if perkData is None else perkData.args.skillData)
            self.lastUsedLevels[skillName] = ccs.level
            skillToBoost.discard(skillName)
            callSkillProcessor(skillName, SkillProcessorArgs(level=ccs.tankmanLevel, levelIncrease=ccs.levelIncrease, isActive=ccs.isTankmanActive, isFire=isFire, skillConfig=skillConfig, hasActiveTankmanForBooster=self._hasActiveTankmanForBooster(skillName)))

        for skillName in skillToBoost:
            callSkillProcessor(skillName, SkillProcessorArgs(level=0, levelIncrease=0, isActive=False, isFire=isFire, skillConfig=getSkill(skillName), hasActiveTankmanForBooster=self._hasActiveTankmanForBooster(skillName)))

        return

    def _getCrewForSkillBooster(self, skillName):
        crew = set()
        crewRoles = self._vehicleDescr.type.crewRoles
        rolesBySkill = ROLES_BY_SKILLS[skillName]
        for idxInCrew, roles in enumerate(crewRoles):
            for role in roles:
                if role not in rolesBySkill:
                    continue
                crew.add(idxInCrew)

        return crew

    def _hasActiveTankmanForBooster(self, skillName):
        return any(self._activityFlags[idxInCrew] for idxInCrew in self._getCrewForSkillBooster(skillName))

    def _updateCommanderFactors(self, a):
        a.factor *= self._affectingFactors['crewRolesFactor']
        self._factors['circularVisionRadius'] = a.factor
        if _DO_DEBUG_LOG:
            LOG_DEBUG("Factor/baseAvgLevel/crewRolesFactor of skill '%s': (%s, %s, %s)" % (
             'commander', a.factor, a.baseAvgLevel, self._affectingFactors['crewRolesFactor']))

    def _updateRadiomanFactors(self, a):
        a.factor *= self._affectingFactors['crewRolesFactor']
        self._factors['radio/distance'] = a.factor * (1.0 + self._affectingFactors['radioDistanceFactor'])
        if _DO_DEBUG_LOG:
            LOG_DEBUG("Factor/baseAvgLevel/crewRolesFactor of skill '%s': (%s, %s, %s)" % (
             'radioman', a.factor, a.baseAvgLevel, self._affectingFactors['crewRolesFactor']))

    def _updateDriverFactors(self, a):
        a.factor *= self._affectingFactors['crewRolesFactor']
        factor = 1.0 / a.factor
        r = self._terrainResistanceFactors
        r[0] *= factor
        r[1] *= factor
        r[2] *= factor
        if _DO_DEBUG_LOG:
            LOG_DEBUG("Factor/baseAvgLevel/crewRolesFactor of skill '%s': (%s, %s, %s)" % (
             'driver', factor, a.baseAvgLevel, self._affectingFactors['crewRolesFactor']))

    def _updateLoaderFactors(self, a):
        a.factor *= self._affectingFactors['crewRolesFactor']
        self._factors['gun/reloadTime'] = 1.0 / a.factor
        if _DO_DEBUG_LOG:
            LOG_DEBUG("Factor/baseAvgLevel/crewRolesFactor of skill '%s': (%s, %s, %s)" % (
             'loader', a.factor, a.baseAvgLevel, self._affectingFactors['crewRolesFactor']))

    def _updateGunnerFactors(self, a):
        a.factor *= self._affectingFactors['crewRolesFactor']
        factors = self._factors
        factors['turret/rotationSpeed'] = a.factor
        factors['gun/rotationSpeed'] = a.factor
        factors['gun/aimingTime'] = 1.0 / a.factor
        self._shotDispFactor = 1.0 / a.factor
        if _DO_DEBUG_LOG:
            LOG_DEBUG("Factor/baseAvgLevel/crewRolesFactor of skill '%s': (%s, %s, %s)" % (
             'gunner', a.factor, a.baseAvgLevel, self._affectingFactors['crewRolesFactor']))

    def _updateRepairFactors(self, a):
        self._factors['repairSpeed'] = a.factor
        if _DO_DEBUG_LOG:
            LOG_DEBUG("Factor/baseAvgLevel of skill '%s': (%s, %s)" % (
             'repair', a.factor, a.baseAvgLevel))

    def _updateCamouflageFactors(self, a):
        self._camouflageFactor = a.factor
        if _DO_DEBUG_LOG:
            LOG_DEBUG("Factor/baseAvgLevel of skill '%s': (%s, %s)" % (
             'camouflage', a.factor, a.baseAvgLevel))

    def _findBestTankmanForSkill(self, skillData):
        if not self._useCachedLevelIncrease:
            commanderLevelIncrease = self._levelIncreaseByBrotherhood + self._levelIncreaseByVehicle
            nonCommanderLevelIncrease = self._calcLeverIncreaseForNonCommander(commanderLevelIncrease)
            self._cachedLevelIncrease = (commanderLevelIncrease, nonCommanderLevelIncrease)
        else:
            commanderLevelIncrease, nonCommanderLevelIncrease = self._cachedLevelIncrease
        commanderIdx = self._commanderIdx
        bestActiveTankman = None
        maxActiveLevel = 0
        for idxInCrew, level in skillData.get('crew', []):
            levelIncrease = commanderLevelIncrease if idxInCrew == commanderIdx else nonCommanderLevelIncrease
            isActive = self._activityFlags[idxInCrew]
            if isActive:
                if level + levelIncrease > maxActiveLevel:
                    bestActiveTankman = CombinedCrewSkill(tankmanLevel=level, levelIncrease=levelIncrease, isTankmanActive=isActive)
                    maxActiveLevel = level + levelIncrease

        ccs = bestActiveTankman or CombinedCrewSkill(tankmanLevel=0, levelIncrease=0, isTankmanActive=False)
        ccs.hasActiveTankmanForBooster = any(self._activityFlags[idxInCrew] for idxInCrew in skillData.get('b_crew', ()))
        ccs.boosterMultiplier = skillData.get('booster')
        return ccs

    def _isPerkActive(self, skillName):
        for idxInCrew, level in self._skills.get(skillName, ()):
            if self._activityFlags[idxInCrew]:
                return True

        return False

    def _setFactor(self, name, value):
        if name in _ADDITIVE_FACTORS:
            self._factors[name] = self._factors.get(name, 0.0) + value
        else:
            self._factors[name] = self._factors.get(name, 1.0) * value

    def _validateAndComputeCrew(self):

        def makeError(err):
            return '%s: %s, %s' % (err, repr(crewCompactDescrs), repr(vehicleDescr.name))

        crewCompactDescrs = self._crewCompactDescrs
        vehicleDescr = self._vehicleDescr
        vehicleType = vehicleDescr.type
        crewRoles = vehicleType.crewRoles
        vehicleNationID = vehicleType.id[0]
        skillConfig = tankmen.getSkillsConfig()
        MAX_SKILL_LEVEL = tankmen.MAX_SKILL_LEVEL
        if len(crewCompactDescrs) != len(crewRoles):
            raise SoftException(makeError('wrong number or tankmen'))
        skills = {}
        perks = {}
        idxInCrew = 0
        for compactDescr, roles in zip(crewCompactDescrs, crewRoles):
            descr = tankmen.TankmanDescr(compactDescr, True)
            if descr.nationID != vehicleNationID:
                raise SoftException(makeError('wrong tankman nation'))
            if descr.role != roles[0]:
                raise SoftException(makeError('wrong tankman role'))
            factor = descr.efficiencyOnVehicle(vehicleDescr)
            activeSkills = set()
            roleLevelOnVehicle = descr.roleLevel * factor
            for skillName in roles:
                skills.setdefault(skillName, []).append((idxInCrew, roleLevelOnVehicle))
                activeSkills.update(tankmen.SKILLS_BY_ROLES[skillName])

            for skillName, level in descr.skillLevels:
                if skillName not in activeSkills:
                    continue
                levelOnVehicle = level * factor
                vsePerk = skillConfig.getSkill(skillName).vsePerk
                if vsePerk is not None:
                    perkData = perks.setdefault(vsePerk, PerkData(0, CrewContextArgs({'crew': []})))
                    perkData.args.skillData['crew'].append((idxInCrew, levelOnVehicle))
                skills.setdefault(skillName, []).append((idxInCrew, levelOnVehicle))

            idxInCrew += 1
            if not self._defaultSixthSenseDisabled:
                skills.setdefault('commander_sixthSense', []).append((0, MAX_SKILL_LEVEL * 1.0))

        self._addPerksFromEquipment(perks)
        return (skills, perks)

    def _addPerksFromEquipment(self, perks):
        pass

    def _computeSummSkillLevel(self, skillData, nonCommanderLevelIncrease=0.0, commanderLevelIncrease=0.0):
        summLevel = 0.0
        baseSummLevel = 0.0
        numInactive = 0
        activityFlags = self._activityFlags
        commanderIdx = self._commanderIdx
        for idx, level in skillData:
            if not activityFlags[idx]:
                numInactive += 1
                continue
            baseSummLevel += level
            summLevel += level
            summLevel += nonCommanderLevelIncrease if idx != commanderIdx else commanderLevelIncrease

        return (baseSummLevel, summLevel, numInactive)

    def _updateCommanderUniversalistNotifications(self, universalistAddition):
        pass

    def _crewComp(self):
        roleSkills = {name:data for name, data in self._skills.iteritems() if name in tankmen.ROLES if name in tankmen.ROLES}
        return roleSkills

    _skillProcessors = {'commander': _updateCommanderFactors, 
       'radioman': _updateRadiomanFactors, 
       'driver': _updateDriverFactors, 
       'gunner': _updateGunnerFactors, 
       'loader': _updateLoaderFactors, 
       'repair': _updateRepairFactors, 
       'camouflage': _updateCamouflageFactors, 
       'commander_universalist': None, 
       'commander_tutor': None, 
       'commander_expert': None, 
       'commander_sixthSense': None, 
       'commander_eagleEye': None, 
       'commander_enemyShotPredictor': None, 
       'commander_practical': None, 
       'driver_tidyPerson': None, 
       'driver_smoothDriving': None, 
       'driver_virtuoso': None, 
       'driver_badRoadsKing': None, 
       'driver_rammingMaster': None, 
       'driver_motorExpert': None, 
       'gunner_smoothTurret': None, 
       'gunner_gunsmith': None, 
       'gunner_sniper': None, 
       'gunner_rancorous': None, 
       'gunner_focus': None, 
       'gunner_quickAiming': None, 
       'loader_pedant': None, 
       'loader_desperado': None, 
       'loader_intuition': None, 
       'loader_ambushMaster': None, 
       'loader_melee': None, 
       'loader_ammunitionImprove': None, 
       'radioman_finder': None, 
       'radioman_inventor': None, 
       'radioman_lastEffort': None, 
       'radioman_retransmitter': None, 
       'fireFighting': None, 
       'radioman_interference': None}

    def __getUniqueArenaID(self):
        if not hasattr(self, '_vehicle'):
            return -1
        return self._vehicle.arenaUniqueID

    def __getVehicleID(self):
        if not hasattr(self, '_vehicle'):
            return -1
        return self._vehicle.id

    def recalculateSkills(self):
        self._skills, self._perks = self._validateAndComputeCrew()