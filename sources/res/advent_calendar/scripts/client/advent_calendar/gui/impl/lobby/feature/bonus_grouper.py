from __future__ import absolute_import
from enum import Enum
from advent_calendar.gui.impl.lobby.feature.advent_helper import getFlattenedBonuses
from gui.goodies.goodie_items import Booster, DemountKit, RecertificationForm, MentoringLicense
from gui.server_events.bonuses import C11nProgressTokenBonus, splitBonuses
from gui.shared.gui_items import GUI_ITEM_TYPE
from helpers import dependency
from skeletons.gui.goodies import IGoodiesCache

class QuestRewardsGroups(Enum):
    CURRENCIES_AND_PREMIUM = 'currenciesAndPremium'
    BOOSTERS = 'boosters'
    CUSTOMIZATIONS = 'customizations'
    CREW_BONUSES_OR_X5 = 'crewBonusesOrX5'
    PROGRESSION_REWARDS = 'progressionRewards'
    EXPERIMENTAL_EQUIPMENT_AND_COMPONENTS = 'experimentalEquipmentAndComponents'


class AdventCalendarQuestsBonusGrouper(object):
    __goodiesCache = dependency.descriptor(IGoodiesCache)

    def __init__(self, groupAndValueExtractorMapping=None):
        self._groupAndValueExtractors = {'goodies': self._extractGoodies, 
           'credits': self._extractCurrency, 
           'tokens': self._extractTokens, 
           'crewBooks': self._extractCrewBook, 
           'premium_plus': self._extractCurrency, 
           'customizations': self._extractCustomizations, 
           'crewSkins': self._extractCrewSkins, 
           'equipCoin': self._extractCurrency, 
           'items': self._extractItems}
        if groupAndValueExtractorMapping is not None:
            self._groupAndValueExtractors.update(groupAndValueExtractorMapping)
        return

    @staticmethod
    def _extractCurrency(bonus):
        name = bonus.getName()
        if name == 'equipCoin':
            return {QuestRewardsGroups.EXPERIMENTAL_EQUIPMENT_AND_COMPONENTS: {name}}
        if name == 'premium_plus':
            name = 'premium_plus_universal'
        return {QuestRewardsGroups.CURRENCIES_AND_PREMIUM: {name}}

    @staticmethod
    def _extractTokens(bonus):
        if 'battle_bonus_x5' in bonus.getValue():
            return {QuestRewardsGroups.CREW_BONUSES_OR_X5: {'bonus_battle_task'}}
        return {}

    @staticmethod
    def _extractCrewBook(_):
        return {QuestRewardsGroups.CREW_BONUSES_OR_X5: {'universal_brochure'}}

    @staticmethod
    def _extractCustomizations(bonus):
        values = set()
        for v in bonus.getValue():
            custType = v['custType']
            if custType == 'projection_decal':
                custType = 'projectionDecal'
            values.add(custType)

        return {QuestRewardsGroups.CUSTOMIZATIONS: values}

    @staticmethod
    def _extractCrewSkins(_):
        return {QuestRewardsGroups.CUSTOMIZATIONS: {'crewSkin1'}}

    @staticmethod
    def _emptyExtractor(_):
        return {}

    @staticmethod
    def _extractGoodies(bonus):
        groupedBonuses = {}
        for goodieId in bonus.getValue():
            goodie = AdventCalendarQuestsBonusGrouper.__goodiesCache.getGoodie(goodieId)
            if isinstance(goodie, Booster):
                groupedBonuses.setdefault(QuestRewardsGroups.BOOSTERS, set()).add(goodie.boosterGuiType)
            elif isinstance(goodie, (DemountKit, RecertificationForm)):
                groupedBonuses.setdefault(QuestRewardsGroups.CREW_BONUSES_OR_X5, set()).add(goodie.itemTypeName)

        return groupedBonuses

    @staticmethod
    def _extractItems(bonus):
        for item in bonus.getItems():
            if item.itemTypeID == GUI_ITEM_TYPE.OPTIONALDEVICE and item.isModernized:
                return {QuestRewardsGroups.EXPERIMENTAL_EQUIPMENT_AND_COMPONENTS: {'expequipments_gift'}}

        return {}

    def group(self, quests):
        groupedBonuses = {}
        for bonus in getFlattenedBonuses(quests):
            name = bonus.getName()
            for group, value in self._groupAndValueExtractors.get(name, self._emptyExtractor)(bonus).items():
                groupedBonuses.setdefault(group, set()).update(value)

        return groupedBonuses


class RewardsBonusGroups(Enum):
    CREW_MEMBER = 'crewMember'
    LOOTBOX = 'lootbox'
    PREMIUM = 'premium_plus'
    STYLE_2D = 'style'
    DECAL = 'projection_decal'
    RESERVE_CREDITS = 'booster_credits'
    RESERVE_EXP = 'booster_xp'
    RESERVE_COMBINED_EXP = 'booster_free_xp_and_crew_xp'
    CREW_BONUSES = 'booklet'
    RECERTIFICATION_FORM = 'recertificationForm'
    MENTORING_LICENSE = 'mentoringLicense'
    BATTLE_BONUS_5X = 'battleBonus5X'
    EXPERIMENTAL_EQUIPMENT = 'experimental_equipment'
    CREDITS = 'credits'
    COMPONENTS = 'equipCoin'
    FREEXP = 'freeXP'
    NONE = 'none'


class RewardBonusGrouper(object):
    _goodiesCache = dependency.descriptor(IGoodiesCache)

    def __init__(self, rewardsBonusGroup, groupAndValueExtractorMapping=None):
        self._rewardsBonuses = rewardsBonusGroup
        self._groupAndValueExtractors = {'goodies': self._extractGoodies, 
           'credits': self._extractCurrency, 
           'tokens': self._extractTokens, 
           'crewBooks': self._extractCrewBook, 
           'premium_plus': self._extractCurrency, 
           'customizations': self._extractCustomizations, 
           'tmanToken': self._extractTman, 
           'equipCoin': self._extractCurrency, 
           'currencies': self._extractCurrencies, 
           'items': self._extractItems, 
           'lootBox': self._extractLootBoxes, 
           'freeXP': self._extractCurrency, 
           C11nProgressTokenBonus.BONUS_NAME: self._extractProgressionCustomizations}
        if groupAndValueExtractorMapping is not None:
            self._groupAndValueExtractors.update(groupAndValueExtractorMapping)
        return

    def _extractCurrency(self, bonus):
        try:
            return self._rewardsBonuses(bonus.getName())
        except ValueError:
            return

        return

    def _extractLootBoxes(self, _):
        return self._rewardsBonuses.LOOTBOX

    def _extractCurrencies(self, bonus):
        try:
            return self._rewardsBonuses(bonus.getCode())
        except ValueError:
            return

        return

    def _extractTokens(self, bonus):
        if 'battle_bonus_x5' in bonus.getValue():
            return self._rewardsBonuses.BATTLE_BONUS_5X
        else:
            return

    def _extractCrewBook(self, _):
        return self._rewardsBonuses.CREW_BONUSES

    def _extractCustomizations(self, bonus):
        customizations = bonus.getValue()
        if not customizations:
            return
        else:
            try:
                return self._rewardsBonuses(customizations[0]['custType'])
            except ValueError:
                return

            return

    def _extractProgressionCustomizations(self, _):
        return self._rewardsBonuses.STYLE_2D

    def _extractTman(self, _):
        return self._rewardsBonuses.CREW_MEMBER

    @staticmethod
    def _emptyExtractor(_):
        return

    def _extractGoodies(self, bonus):
        goodieIds = bonus.getValue().keys()
        if not goodieIds:
            return
        else:
            try:
                goodie = self._goodiesCache.getGoodie(goodieIds[0])
                if isinstance(goodie, Booster):
                    return self._rewardsBonuses(goodie.boosterGuiType)
                if isinstance(goodie, (DemountKit, RecertificationForm, MentoringLicense)):
                    return self._rewardsBonuses(goodie.itemTypeName)
            except ValueError:
                return

            return

    def _extractItems(self, bonus):
        for item in bonus.getItems():
            if item.itemTypeID == GUI_ITEM_TYPE.OPTIONALDEVICE and item.isModernized:
                return self._rewardsBonuses.EXPERIMENTAL_EQUIPMENT

        return

    def group(self, bonuses):
        groupedBonuses = []
        for bonus in splitBonuses(bonuses):
            group = self._groupAndValueExtractors.get(bonus.getName(), self._emptyExtractor)(bonus)
            if group:
                groupedBonuses.append((group, bonus))

        return groupedBonuses