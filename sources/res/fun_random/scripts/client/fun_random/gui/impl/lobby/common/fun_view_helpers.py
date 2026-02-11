from __future__ import absolute_import
from account_helpers.AccountSettings import AccountSettings, FUN_RANDOM_PROGRESSION, FUN_RANDOM_PROGR_PREV_COUNTER, FUN_RANDOM_INF_PROGR_PREV_COUNTER, FUN_RANDOM_INF_PROGR_PREV_COMPLETE_COUNT
from typing import Any, Dict, List, Optional, Tuple, Union, TYPE_CHECKING
import math_utils
from fun_random.gui.impl.gen.view_models.views.lobby.common.fun_random_progression_stage import FunRandomProgressionStage, Rarity
from fun_random.gui.impl.gen.view_models.views.lobby.common.fun_random_progression_state import FunRandomProgressionStatus
from fun_random.gui.impl.gen.view_models.views.lobby.common.fun_random_quest_card_model import FunRandomQuestCardModel, CardState
from fun_random.gui.impl.lobby.common.bonuses import FunRandomGoodiesBonusUIPacker
from fun_random.gui.impl.lobby.common.lootboxes import FunRandomLootBoxTokenBonusPacker, FunRandomRewardLootBoxTokenBonusPacker, FunRandomLootBoxVehiclesBonusUIPacker, FunRandomRewardsViewLootBoxTokenBonusPacker, FEP_CATEGORY
from fun_random.gui.feature.fun_constants import FunSubModesState
from fun_random.gui.feature.sub_systems.fun_performance_analyzers import PerformanceGroup
from gui.impl import backport
from gui.impl.auxiliary.collections_helper import TmanTemplateBonusPacker
from gui.impl.auxiliary.rewards_helper import BlueprintBonusTypes
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.common.mode_performance_model import PerformanceRiskEnum
from gui.impl.gen.view_models.views.lobby.user_missions.constants.event_banner_state import EventBannerState
from gui.impl.lobby.common.view_helpers import packBonusModelAndTooltipData
from gui.server_events.bonuses import GoodiesBonus, LootBoxTokensBonus, mergeBonuses
from gui.shared.formatters import time_formatters
from gui.shared.formatters.ranges import toRomanRangeString
from gui.shared.missions.packers.bonus import BonusUIPacker, ExtendedBlueprintBonusUIPacker, getDefaultBonusPackersMap, Customization3Dand2DbonusUIPacker, VehiclesBonusUIPacker
from gui.shared.money import Currency
from helpers import dependency
from shared_utils import first, findFirst
from skeletons.gui.shared import IItemsCache
if TYPE_CHECKING:
    from frameworks.wulf import Array
    from fun_random.gui.feature.models.common import FunSubModesStatus
    from fun_random.gui.feature.models.progressions import FunProgression
    from fun_random.gui.impl.gen.view_models.views.lobby.common.fun_random_progression_state import FunRandomProgressionState
    from gui.server_events.bonuses import SimpleBonus
    from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel
    from gui.impl.gen.view_models.common.missions.bonuses.item_bonus_model import ItemBonusModel
    from gui.impl.gen.view_models.views.lobby.common.mode_performance_model import ModePerformanceModel
    from fun_random.gui.impl.gen.view_models.views.lobby.common.fun_random_progression_condition import FunRandomProgressionCondition
    from fun_random.gui.impl.gen.view_models.views.lobby.common.fun_random_infinite_progression_condition import FunRandomInfiniteProgressionCondition
    from fun_random.gui.server_events.event_items import FunProgressionTriggerQuest
_PROGRESSION_STATUS_MAP = {(False, False, False): FunRandomProgressionStatus.ACTIVE_RESETTABLE, 
   (False, False, True): FunRandomProgressionStatus.ACTIVE_RESETTABLE, 
   (True, False, False): FunRandomProgressionStatus.COMPLETED_RESETTABLE, 
   (False, True, False): FunRandomProgressionStatus.ACTIVE_FINAL, 
   (False, True, True): FunRandomProgressionStatus.ACTIVE_FINAL, 
   (True, True, False): FunRandomProgressionStatus.COMPLETED_FINAL, 
   (True, False, True): FunRandomProgressionStatus.ACTIVE_INFINITE_RESETTABLE, 
   (True, True, True): FunRandomProgressionStatus.ACTIVE_INFINITE_FINAL}
_EVENT_STATE_MAP = {FunSubModesState.BEFORE_SEASON: EventBannerState.ANNOUNCE, 
   FunSubModesState.BETWEEN_SEASONS: EventBannerState.ANNOUNCE, 
   FunSubModesState.AVAILABLE: EventBannerState.IN_PROGRESS, 
   FunSubModesState.NOT_AVAILABLE: EventBannerState.INACTIVE, 
   FunSubModesState.NOT_AVAILABLE_END: EventBannerState.FINISHED}
_PERFORMANCE_GROUP_TO_RISK_ENUM = {PerformanceGroup.LOW_RISK: PerformanceRiskEnum.LOWRISK, 
   PerformanceGroup.MEDIUM_RISK: PerformanceRiskEnum.MEDIUMRISK, 
   PerformanceGroup.HIGH_RISK: PerformanceRiskEnum.HIGHRISK}
FUN_RANDOM_MAPPING = {'tokens': FunRandomLootBoxTokenBonusPacker, 
   'lootBox': FunRandomLootBoxTokenBonusPacker, 
   'tmanToken': TmanTemplateBonusPacker, 
   'vehicles': VehiclesBonusUIPacker, 
   'customizations': Customization3Dand2DbonusUIPacker, 
   'goodies': FunRandomGoodiesBonusUIPacker, 
   BlueprintBonusTypes.BLUEPRINTS: ExtendedBlueprintBonusUIPacker, 
   BlueprintBonusTypes.BLUEPRINTS_ANY: ExtendedBlueprintBonusUIPacker, 
   BlueprintBonusTypes.FINAL_BLUEPRINTS: ExtendedBlueprintBonusUIPacker}
RARITY_ORDER = (
 Rarity.ORDINARY,
 Rarity.UNUSUAL,
 Rarity.RARE,
 Rarity.EPIC,
 Rarity.LEGENDARY)
LOOTBOX_TYPE = 'fep_{0}'
RARITY_VALUES = tuple(LOOTBOX_TYPE.format(v.value) for v in RARITY_ORDER)
DEFAULT_FEP_LB_RARITY = Rarity.ORDINARY
DEFAULT_NON_FEP_LB_RARITY = Rarity.LEGENDARY
DEFAULT_FEP_PROGRESSION_STAGE_RARITY = Rarity.RARE
_FUN_PROGRESSION_BONUS_ORDER = [
 'lootBox',
 'customizations',
 'tmanToken',
 Currency.CRYSTAL,
 Currency.EQUIP_COIN,
 Currency.FREE_XP,
 'crewBooks',
 'mentoring_license',
 'premium_plus',
 Currency.CREDITS,
 'goodies']

def getFormattedTimeLeft(seconds):
    return time_formatters.getTillTimeByResource(seconds, R.strings.fun_random.modeSelector.status.timeLeft, removeLeadingZeros=True)


def getConditionText(rootStrPath, levels):
    battleCondition = rootStrPath.dyn('battleCondition')
    components = [backport.text(battleCondition()) if battleCondition.exists() else '']
    levelCondition = rootStrPath.dyn('levelCondition')
    levels = toRomanRangeString(levels)
    if levelCondition.exists() and levels:
        components.append(backport.text(levelCondition(), levels=levels))
    if len(components) > 1:
        return (' ').join(components)
    return first(components, '')


def getFunRandomEventState(status):
    return _EVENT_STATE_MAP.get(status.state, EventBannerState.INACTIVE)


def getFunRandomBonusPacker():
    mapping = getDefaultBonusPackersMap()
    mapping.update(FUN_RANDOM_MAPPING)
    return BonusUIPacker(mapping)


def getCompensatedFunRandomBonusPacker():
    mapping = getDefaultBonusPackersMap()
    mapping.update(FUN_RANDOM_MAPPING)
    mapping.update({'vehicles': FunRandomLootBoxVehiclesBonusUIPacker})
    return BonusUIPacker(mapping)


def getFunRandomRewardsViewBonusPacker():
    mapping = getDefaultBonusPackersMap()
    mapping.update(FUN_RANDOM_MAPPING)
    mapping.update({'vehicles': FunRandomLootBoxVehiclesBonusUIPacker, 
       'lootBox': FunRandomRewardsViewLootBoxTokenBonusPacker})
    return BonusUIPacker(mapping)


def getFunRandomSpecialBonusPacker():
    mapping = getDefaultBonusPackersMap()
    mapping.update(FUN_RANDOM_MAPPING)
    mapping.update({'tokens': FunRandomRewardLootBoxTokenBonusPacker, 
       'lootBox': FunRandomRewardLootBoxTokenBonusPacker})
    return BonusUIPacker(mapping)


def defineProgressionStatus(progression):
    if progression is not None:
        return _PROGRESSION_STATUS_MAP[(
         progression.state.isCompleted, progression.state.isLastProgression, progression.hasUnlimitedProgression)]
    else:
        return FunRandomProgressionStatus.DISABLED


def packAdditionalRewards(progression, stageIndex, showCount, isSpecial=False):
    if progression.isInUnlimitedProgression:
        bonuses = progression.unlimitedProgression.bonuses
    else:
        stage = findFirst(lambda s: s.stageIndex == stageIndex, progression.stages)
        bonuses = stage.bonuses if stage is not None else []
    return packBonuses(sortFunProgressionBonuses(bonuses), showCount, isSpecial)


def packBonuses(bonuses, showCount, isSpecial):
    result = []
    packer = getFunRandomSpecialBonusPacker() if isSpecial else getFunRandomBonusPacker()
    for bonus in mergeBonuses([ b for b in bonuses if b.isShowInGUI() ]):
        result.extend(packer.pack(bonus))

    return result[showCount:]


def packProgressionActiveStage(progression, stageModel, isSpecial=False, tooltips=None):
    maximumPoints = progression.conditions.maximumCounter
    _packStage(progression.activeStage.bonuses, math_utils.clamp(0, maximumPoints, progression.conditions.counter), progression.activeStage.requiredCounter, maximumPoints, progression.conditions.counter >= progression.conditions.maximumCounter, stageModel, isSpecial, tooltips, DEFAULT_FEP_PROGRESSION_STAGE_RARITY)


def packInfiniteProgressionStage(progression, stageModel, isSpecial=False, tooltips=None):
    maximumPoints = requiredPoints = progression.unlimitedProgression.maximumCounter
    _packStage(progression.unlimitedProgression.bonuses, math_utils.clamp(0, maximumPoints, progression.unlimitedProgression.counter), requiredPoints, maximumPoints, progression.unlimitedProgression.unlimitedExecutor.isCompleted(), stageModel, isSpecial, tooltips)


def packFullProgressionConditions(modeUserName, progression, conditionModel):
    packProgressionConditions(progression, conditionModel)
    conditionModel.setTitle(modeUserName)
    maxPoints = progression.conditions.maximumCounter
    currentPoints = math_utils.clamp(0, maxPoints, progression.conditions.counter)
    conditionModel.setCurrentPoints(currentPoints)
    conditionModel.setMaximumPoints(maxPoints)
    progressionsData = AccountSettings.getSettings(FUN_RANDOM_PROGRESSION)
    progressionCounters = progressionsData.get(progression.config.name, {})
    prevPoints = progressionCounters.get(FUN_RANDOM_PROGR_PREV_COUNTER, 0)
    conditionModel.setPrevPoints(prevPoints)


def packProgressionConditions(progression, conditionModel):
    _packConditions(conditionModel, progression.statusTimer, progression.conditions.text, progression.conditions.triggers)


def packFullInfiniteProgressionConditions(modeUserName, progression, conditionModel):
    packInfiniteProgressionConditions(progression, conditionModel)
    conditionModel.setTitle(modeUserName)
    maxPoints = progression.unlimitedProgression.maximumCounter
    currentPoints = math_utils.clamp(0, maxPoints, progression.unlimitedProgression.counter)
    conditionModel.setCurrentPoints(currentPoints)
    conditionModel.setMaximumPoints(maxPoints)
    progressionsData = AccountSettings.getSettings(FUN_RANDOM_PROGRESSION)
    progressionCounters = progressionsData.get(progression.config.name, {})
    prevPoints = progressionCounters.get(FUN_RANDOM_INF_PROGR_PREV_COUNTER, 0)
    conditionModel.setPrevPoints(prevPoints)
    completeCount = progression.unlimitedProgression.unlimitedExecutor.getBonusCount()
    conditionModel.setCompleteCount(completeCount)
    prevCompleteCount = progressionCounters.get(FUN_RANDOM_INF_PROGR_PREV_COMPLETE_COUNT, 0)
    conditionModel.setPrevCompleteCount(prevCompleteCount)


def packInfiniteProgressionConditions(progression, conditionModel):
    text = progression.unlimitedProgression.unlimitedTrigger.getDescription()
    triggers = (progression.unlimitedProgression.unlimitedTrigger,)
    statusTimer = progression.statusTimer
    _packConditions(conditionModel, statusTimer, text, triggers)


def packProgressionStages(progression, stagesModel, tooltips=None):
    stagesModel.clear()
    maximumPoints = progression.conditions.maximumCounter
    for stage in progression.stages:
        stageModel = FunRandomProgressionStage()
        _packStage(stage.bonuses, progression.conditions.counter, stage.requiredCounter, maximumPoints, progression.conditions.counter >= stage.requiredCounter, stageModel, tooltips=tooltips, defaultRarity=DEFAULT_FEP_PROGRESSION_STAGE_RARITY)
        stagesModel.addViewModel(stageModel)

    stagesModel.invalidate()


def packProgressionState(progression, stateModel):
    stateModel.setStatus(defineProgressionStatus(progression))
    stateModel.setCurrentStage(progression.state.currentStageIndex + 1)
    stateModel.setMaximumStage(progression.state.maximumStageIndex + 1)
    stateModel.setStatusTimer(progression.statusTimer)


def packInfiniteProgressionState(progression, stateModel):
    stateModel.setStatus(defineProgressionStatus(progression))
    unlimitedExecutor = progression.unlimitedProgression.unlimitedExecutor
    stateModel.setCurrentStage(unlimitedExecutor.getBonusCount())
    stateModel.setMaximumStage(unlimitedExecutor.bonusCond.getBonusLimit())
    stateModel.setStatusTimer(progression.statusTimer)


def packStageRewards(bonuses, rewardsModel, isSpecial=False, tooltips=None):
    packer = getFunRandomSpecialBonusPacker() if isSpecial else getFunRandomBonusPacker()
    rewardsModel.clear()
    packBonusModelAndTooltipData(sortFunProgressionBonuses(mergeBonuses(bonuses)), rewardsModel, tooltipData=tooltips, packer=packer)
    rewardsModel.invalidate()


def packPerformanceAlertInfo(performanceModel, performanceGroup, default=PerformanceGroup.LOW_RISK):
    performanceModel.setPerformanceRisk(_PERFORMANCE_GROUP_TO_RISK_ENUM.get(performanceGroup, default))
    performanceModel.setShowPerfRisk(performanceGroup != default)


def _getFunProgressionBonusOrder(bonus):
    bonusName = bonus.getName()
    if isinstance(bonus, GoodiesBonus) and bonus.getMentoringLicenses():
        bonusName = 'mentoring_license'
    try:
        idx = _FUN_PROGRESSION_BONUS_ORDER.index(bonusName)
    except ValueError:
        idx = len(_FUN_PROGRESSION_BONUS_ORDER) + 1

    return idx


def sortFunProgressionBonuses(bonuses):
    return sorted(bonuses, key=_getFunProgressionBonusOrder)


def _packConditions(conditionModel, statusTimer, text, triggers):
    conditionModel.setText(text)
    conditionModel.setStatusTimer(statusTimer)
    _packTriggers(triggers, conditionModel.getConditions())


def _packTriggers(triggers, cardsModel):
    cardsModel.clear()
    for trigger in sorted(triggers, key=lambda q: q.isCompleted()):
        cardModel = FunRandomQuestCardModel()
        _packTrigger(cardModel, trigger)
        cardsModel.addViewModel(cardModel)

    cardsModel.invalidate()


def _packTrigger(cardModel, trigger):
    cardModel.setState(CardState.COMPLETED if trigger.isCompleted() else CardState.ACTIVE)
    cardModel.setDescription(trigger.getDescription())
    cardModel.setQuestCondition(trigger.getQuestCondition())
    cardModel.setCurrentProgress(trigger.getCurrentProgress())
    cardModel.setTotalProgress(trigger.getTotalProgress())
    cardModel.setTotalPoints(trigger.getEarnedPoints())
    altQuest = trigger.getAltQuest()
    cardModel.setMainBonusCount(trigger.getBonusCounterNumber())
    cardModel.setAltBonusCount(altQuest.getBonusCounterNumber() if altQuest else 0)


def _packStage(bonuses, currentPoints, requiredPoints, maximumPoints, isCompleted, stageModel, isSpecial=False, tooltips=None, defaultRarity=DEFAULT_FEP_LB_RARITY):
    stageModel.setCurrentPoints(currentPoints)
    stageModel.setRequiredPoints(requiredPoints)
    stageModel.setMaximumPoints(maximumPoints)
    stageModel.setRarity(getStageRarity(bonuses, defaultRarity))
    stageModel.setIsCompleted(isCompleted)
    packStageRewards(bonuses, stageModel.getRewards(), isSpecial, tooltips)


@dependency.replace_none_kwargs(itemsCache=IItemsCache)
def getStageRarity(bonuses, defaultRarity=DEFAULT_FEP_LB_RARITY, itemsCache=None):
    rarityIdx = RARITY_ORDER.index(defaultRarity)
    for bonus in (b for b in bonuses if isinstance(b, LootBoxTokensBonus)):
        for tID in bonus.getTokens():
            lb = itemsCache.items.tokens.getLootBoxByTokenID(tID)
            if lb is None:
                continue
            if lb.getCategory() != FEP_CATEGORY:
                return DEFAULT_NON_FEP_LB_RARITY
            if lb.getType() in RARITY_VALUES:
                lbRarityIdx = RARITY_VALUES.index(lb.getType())
                if lbRarityIdx > rarityIdx:
                    rarityIdx = lbRarityIdx

    return RARITY_ORDER[rarityIdx]