from __future__ import absolute_import, division
import logging, typing
from battle_modifiers_common import BattleParams
from items import vehicles
from renewable_subscription_common.schema import renewableSubscriptionsConfigSchema
from renewable_subscription_common.settings_constants import WotPlusTier
if typing.TYPE_CHECKING:
    from battle_modifiers_common import BattleModifiers
    from renewable_subscription_common.schema import _SubscriptionFeaturesModel, _SubscriptionFullModel, _AdditionalXPBonusFeatureModel, _CompatibleVehicles, _BonusFactors, _FeatureModel, _ExclusiveVehicleFeatureModel, _BadgesFeatureModel, _ExclusiveVehicle
_logger = logging.getLogger(__name__)
ONE_HOUR = 3600

def getModelTierSettings(model, tierID):
    return model.getTierSettingsById(tierID)


def getCurrentModelTierSettings(tierID):
    return getModelTierSettings(renewableSubscriptionsConfigSchema.getModel(), tierID)


class _ModelProvider(object):
    __slots__ = ()

    def getModelRef(self):
        raise NotImplementedError


class _GlobalModelProvider(_ModelProvider):
    __slots__ = ()

    def getModelRef(self):
        return renewableSubscriptionsConfigSchema.getModel()


class SpecificModelProvider(_ModelProvider):
    __slots__ = ('_modelRef', )

    def __init__(self, model):
        super(SpecificModelProvider, self).__init__()
        self._modelRef = model

    def getModelRef(self):
        return self._modelRef


class SubscriptionSettingsStorage(object):
    __slots__ = ('_tierID', '_modelProvider')

    def __init__(self, tierID, modelProvider=None):
        super(SubscriptionSettingsStorage, self).__init__()
        self._tierID = tierID
        self._modelProvider = modelProvider or _GlobalModelProvider()

    def updateTierID(self, tierID):
        self._tierID = tierID

    def iterTier(self):
        settingsModel = self._modelProvider.getModelRef()
        if settingsModel:
            for tier in settingsModel.tiers:
                yield (
                 tier.id, getModelTierSettings(settingsModel, tier.id))

    def reverseIterTiers(self):
        settingsModel = self._modelProvider.getModelRef()
        if settingsModel:
            tiers = settingsModel.tiers
            for i in range(len(tiers) - 1, -1, -1):
                yield (
                 tiers[i].id, getModelTierSettings(settingsModel, tiers[i].id))

    def isRenewableSubscriptionEnabled(self):
        settingsModel = self._modelProvider.getModelRef()
        if not settingsModel:
            return False
        return settingsModel.enabled

    def isEnabledForSteam(self):
        settingsModel = self._modelProvider.getModelRef()
        if not settingsModel:
            return False
        return settingsModel.enabledForSteam

    def isProductEnabledForSteam(self, tier):
        if not self.isEnabledForSteam():
            return False
        tierSettings = self._modelProvider.getModelRef()
        if not tierSettings:
            return False
        for tierSetting in tierSettings.tiers:
            if tier == tierSetting.id:
                return tierSetting.productEnabledForSteam

        return False

    def isGoldReserveFeatureEnabled(self):
        settingsModel = self._modelProvider.getModelRef()
        if not settingsModel:
            return False
        if not settingsModel.enabled:
            return False
        return settingsModel.goldReserveFeature.enabled

    def isGoldReserveFeatureAvailable(self):
        tierSettings = self._getEnabledTierSettings()
        if not tierSettings:
            return False
        return self._getFeatureAvailability(tierSettings.goldReserveFeature)

    def isExcludedMapFeatureEnabled(self):
        settingsModel = self._modelProvider.getModelRef()
        if not settingsModel:
            return False
        return settingsModel.excludedMapFeature.enabled

    def isExcludedMapFeatureAvailable(self):
        tierSettings = self._getEnabledTierSettings()
        if not tierSettings:
            return False
        return self._getFeatureAvailability(tierSettings.excludedMapFeature)

    def getExcludedMapsCount(self):
        tierSettings = self._getEnabledTierSettings()
        if not tierSettings:
            return 0
        if not tierSettings.excludedMapFeature.enabled:
            return 0
        if not tierSettings.excludedMapFeature.available:
            return 0
        return tierSettings.excludedMapFeature.count

    def isDailyAttendanceFeatureEnabled(self):
        tierSettings = self._getEnabledTierSettings()
        if not tierSettings:
            return False
        return tierSettings.dailyAttendanceFeature.enabled

    def isDailyAttendanceFeatureAvailable(self):
        tierSettings = self._getEnabledTierSettings()
        if not tierSettings:
            return False
        return self._getFeatureAvailability(tierSettings.dailyAttendanceFeature)

    def getDailyAttendanceQuestPrefix(self):
        tierSettings = self._getEnabledTierSettings()
        if not tierSettings:
            return None
        else:
            return tierSettings.dailyAttendanceFeature.questPrefix

    def isProBoostFeatureEnabled(self):
        settingsModel = self._modelProvider.getModelRef()
        if not settingsModel:
            return False
        if not settingsModel.enabled:
            return False
        return settingsModel.proBoostFeature.enabled

    def isProBoostFeatureAvailable(self):
        tierSettings = self._getEnabledTierSettings()
        if not tierSettings:
            return False
        return self._getFeatureAvailability(tierSettings.proBoostFeature)

    def getProBoostApplicableVehiclesLimit(self):
        tierSettings = self._getEnabledTierSettings()
        if not tierSettings:
            return 0
        return tierSettings.proBoostFeature.applicableVehiclesLimit

    def getProBoostCooldown(self, formatted=False):
        tierSettings = self._getEnabledTierSettings()
        if not tierSettings:
            return 0
        if formatted:
            return int(tierSettings.proBoostFeature.cooldown / ONE_HOUR)
        return tierSettings.proBoostFeature.cooldown

    def getProBoostBonusFactors(self):
        tierSettings = self._getEnabledTierSettings()
        if not tierSettings:
            return None
        else:
            return tierSettings.proBoostFeature.bonusFactors

    def getProBoostExcludedTags(self):
        if self.isProBoostFeatureAvailable():
            return self._getCurrentTierSettings().proBoostFeature.excludedTags
        return list()

    def getProBoostCompatibleVehicles(self):
        if self.isProBoostFeatureAvailable():
            return self._getCurrentTierSettings().proBoostFeature.compatibleVehicles
        return list()

    def hasVehicleProBoostExcludedTags(self, vehicleCD):
        vehType = vehicles.getVehicleType(vehicleCD)
        return any(tag in vehType.tags for tag in self.getProBoostExcludedTags())

    def isVehicleProBoostCompatible(self, vehicleCD):
        compatibleVehicles = self.getProBoostCompatibleVehicles()
        vehicleLevel = vehicles.getVehicleType(vehicleCD).level
        vehicleClass = vehicles.getVehicleClass(vehicleCD)
        for compatibleVehicle in compatibleVehicles:
            if compatibleVehicle.tankClass == vehicleClass and vehicleLevel in compatibleVehicle.excludedLevels:
                return False

        return True

    def getMaxGoldReserveCapacity(self):
        tierSettings = self._getCurrentTierSettings()
        if not tierSettings:
            return 0
        return tierSettings.goldReserveFeature.maxCapacity

    def getGoldReserveGain(self, battleType, battleModifiers):
        tierSettings = self._getCurrentTierSettings()
        if not tierSettings:
            return
        else:
            from constants import ARENA_BONUS_TYPE_IDS
            strArenaBonusTypeName = ARENA_BONUS_TYPE_IDS.get(battleType, '')
            if not strArenaBonusTypeName:
                return
            return battleModifiers(BattleParams.GOLD_RESERVE_GAINS, tierSettings.goldReserveFeature.getArenaTypeToGain()).get(strArenaBonusTypeName, None)

    def isBadgesEnabled(self):
        tierSettings = self._getEnabledTierSettings()
        if not tierSettings:
            return False
        return tierSettings.badgesFeature.enabled

    def isBadgesAvailable(self):
        tierSettings = self._getEnabledTierSettings()
        if not tierSettings:
            return False
        return self._getFeatureAvailability(tierSettings.badgesFeature)

    def getEnabledBadges(self):
        if self.isBadgesEnabled():
            return set(self._getCurrentTierSettings().badgesFeature.badgeIDs)
        return set()

    def getBadgesConfig(self):
        tierSettings = self._getEnabledTierSettings()
        if not tierSettings:
            return None
        else:
            return tierSettings.badgesFeature

    def isFreeEquipmentDemountingEnabled(self):
        settingsModel = self._modelProvider.getModelRef()
        if not settingsModel:
            return False
        if not settingsModel.enabled:
            return False
        return settingsModel.freeEquipmentDemountingFeature.enabled

    def isFreeEquipmentDemountingAvailable(self):
        tierSettings = self._getEnabledTierSettings()
        if not tierSettings:
            return False
        return self._getFeatureAvailability(tierSettings.freeEquipmentDemountingFeature)

    def isFreeDeluxeEquipmentDemountingEnabled(self):
        if not self.isFreeEquipmentDemountingEnabled():
            return False
        settingsModel = self._modelProvider.getModelRef()
        if not settingsModel:
            return False
        return settingsModel.freeEquipmentDemountingFeature.deluxeEnabled

    def isFreeDeluxeEquipmentDemountingAvailable(self):
        if not self.isFreeEquipmentDemountingAvailable():
            return False
        tierSettings = self._getCurrentTierSettings()
        if not tierSettings:
            return False
        return tierSettings.freeEquipmentDemountingFeature.deluxeEnabled

    def isPassiveCrewXPEnabled(self):
        settingsModel = self._modelProvider.getModelRef()
        if not settingsModel:
            return False
        return settingsModel.passiveCrewXPFeature.enabled

    def isPassiveCrewXPAvailable(self):
        tierSettings = self._getEnabledTierSettings()
        if not tierSettings:
            return False
        return self._getFeatureAvailability(tierSettings.passiveCrewXPFeature)

    def getCrewXPPerMinute(self):
        tierSettings = self._getCurrentTierSettings()
        if not tierSettings:
            return 0.0
        return tierSettings.passiveCrewXPFeature.xpPerMinute

    def isBattleBonusesEnabled(self):
        settingsModel = self._modelProvider.getModelRef()
        if not settingsModel:
            return False
        if not settingsModel.enabled:
            return False
        return settingsModel.battleBonusesFeature.enabled

    def isBattleBonusesAvailable(self):
        tierSettings = self._getEnabledTierSettings()
        if not tierSettings:
            return False
        return self._getFeatureAvailability(tierSettings.battleBonusesFeature)

    def getBattleBonusesFeatureFactors(self):
        tierSettings = self._getEnabledTierSettings()
        if not tierSettings:
            return None
        else:
            if not tierSettings.battleBonusesFeature.available:
                return None
            return tierSettings.battleBonusesFeature.bonusFactors

    def getAdditionalXPBonusConfig(self):
        tierSettings = self._getEnabledTierSettings()
        if not tierSettings:
            return None
        else:
            return tierSettings.additionalXPBonusFeature

    def isAdditionalXPBonusEnabled(self):
        settingsModel = self._modelProvider.getModelRef()
        if not settingsModel:
            return False
        if not settingsModel.enabled:
            return False
        return settingsModel.additionalXPBonusFeature.enabled

    def isAdditionalXPBonusAvailable(self):
        tierSettings = self._getEnabledTierSettings()
        if not tierSettings:
            return False
        return self._getFeatureAvailability(tierSettings.additionalXPBonusFeature)

    def getAdditionalXPBonusCount(self):
        config = self.getAdditionalXPBonusConfig()
        if not config:
            return 0
        if not config.enabled:
            return 0
        if not config.available:
            return 0
        return config.applyCount

    def getExclusiveVehicleConfig(self):
        tierSettings = self._getEnabledTierSettings()
        if not tierSettings:
            return None
        else:
            return tierSettings.exclusiveVehicleFeature

    def isExclusiveVehicleEnabled(self):
        config = self.getExclusiveVehicleConfig()
        if not config:
            return False
        return config.enabled

    def isExclusiveVehicleAvailable(self):
        tierSettings = self._getEnabledTierSettings()
        if not tierSettings:
            return False
        return self._getFeatureAvailability(tierSettings.exclusiveVehicleFeature)

    def getExclusiveVehicles(self):
        config = self.getExclusiveVehicleConfig()
        if config and config.enabled:
            return config.exclusiveVehicles
        return []

    def getExclusiveVehiclesCount(self):
        return 2

    def isOptionalDevicesAssistantEnabled(self):
        tierSettings = self._getEnabledTierSettings()
        if not tierSettings:
            return False
        return tierSettings.optionalDevicesAssistantFeature.enabled

    def isOptionalDevicesAssistantAvailable(self):
        tierSettings = self._getEnabledTierSettings()
        if not tierSettings:
            return False
        return self._getFeatureAvailability(tierSettings.optionalDevicesAssistantFeature)

    def isCrewAssistantEnabled(self):
        tierSettings = self._getEnabledTierSettings()
        if not tierSettings:
            return False
        return tierSettings.crewAssistantFeature.enabled

    def isCrewAssistantAvailable(self):
        tierSettings = self._getEnabledTierSettings()
        if not tierSettings:
            return False
        return self._getFeatureAvailability(tierSettings.crewAssistantFeature)

    def getAllProductCodes(self):
        settingsModel = self._modelProvider.getModelRef()
        if not settingsModel:
            return []
        return settingsModel.getAllProductCodes()

    def getProductCodesForTier(self, tierID):
        settingsModel = self._modelProvider.getModelRef()
        if not settingsModel:
            return []
        return settingsModel.getTierProductCodes(tierID)

    def isBattlePassFeatureEnabled(self):
        settingsModel = self._modelProvider.getModelRef()
        if not settingsModel:
            return False
        return settingsModel.battlePassFeature.enabled

    def isBattlePassFeatureAvailable(self):
        tierSettings = self._getEnabledTierSettings()
        if not tierSettings:
            return False
        return self._getFeatureAvailability(tierSettings.battlePassFeature)

    def getBattlePassVehiclePointsListForMode(self, bonusType, vehTypeCompDescr=0):
        settingsModel = self._modelProvider.getModelRef()
        if not settingsModel:
            return (tuple(), tuple())
        if not settingsModel.enabled:
            return (tuple(), tuple())
        return settingsModel.battlePassFeature.getVehiclePointListsForMode(bonusType, vehTypeCompDescr)

    def getBestBattlePassBonusTier(self):
        for tierID, tier in self.reverseIterTiers():
            if tier.battlePassFeature.available:
                return tierID

        return WotPlusTier.NONE

    def isBattlePassBonusIncludedInAnyTier(self):
        return self.getBestBattlePassBonusTier() in WotPlusTier.ALL

    def getTierAvailableFeatures(self, tierID):
        tierSettings = self._getSpecificTierSettings(tierID)
        if not tierSettings:
            return frozenset()
        return tierSettings.getAvailableFeatures()

    def isServiceRecordCustomizationEnabled(self):
        tierSettings = self._getEnabledTierSettings()
        if not tierSettings:
            return False
        return tierSettings.serviceRecordCustomizationFeature.enabled

    def isServiceRecordCustomizationAvailable(self):
        tierSettings = self._getEnabledTierSettings()
        if not tierSettings:
            return False
        return self._getFeatureAvailability(tierSettings.serviceRecordCustomizationFeature)

    def _getCurrentTierSettings(self):
        return self._getSpecificTierSettings(self._tierID)

    def _getSpecificTierSettings(self, tierID):
        settingsModel = self._modelProvider.getModelRef()
        if not settingsModel:
            return None
        else:
            return getModelTierSettings(settingsModel, tierID)

    def _getEnabledTierSettings(self):
        if not self.isRenewableSubscriptionEnabled():
            return None
        else:
            return self._getCurrentTierSettings()

    def _getFeatureAvailability(self, feature):
        if not feature.enabled:
            return False
        return feature.available