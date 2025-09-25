from gui.server_events.events_helpers import EventInfoModel
from halloween_common.halloween_constants import KEY_DAILY_QUEST_TPL
from gui.server_events.awards_formatters import AWARDS_SIZES
from halloween.gui.game_control.halloween_artefacts_controller import compareBonusesByPriority
from halloween.gui.impl.gen.view_models.views.common.bonus_item_view_model import BonusItemViewModel
from halloween.gui.impl.gen.view_models.views.lobby.widgets.hangar_carousel_vehicle_view_model import VehicleStates
from halloween.gui.impl.gen.view_models.views.lobby.widgets.meta_view_model import ArtefactStates
from halloween.gui.impl.lobby.hw_helpers.bonuses_formatters import getHWMetaAwardFormatter, getImgName, HalloweenBonusesAwardsComposer
from halloween.skeletons.halloween_artefacts_controller import IHalloweenArtefactsController
from halloween.skeletons.halloween_controller import IHalloweenController
from helpers import dependency
PROMINENT_REWARD_TOOLTIP_ID = 'prominent_reward_tooltip'
INF_DISPLAY_BONUSES = 999

@dependency.replace_none_kwargs(hwCtrl=IHalloweenController)
def isDailyKeyQuestCompleted(intCD, hwCtrl=None):
    quest = hwCtrl.getHWQuestsCache().get(KEY_DAILY_QUEST_TPL.format(intCD=intCD))
    if quest:
        return quest.isCompleted()
    return True


@dependency.replace_none_kwargs(hwCtrl=IHalloweenController)
def getDailyKeyQuestDescription(intCD, hwCtrl=None):
    quest = hwCtrl.getHWQuestsCache().get(KEY_DAILY_QUEST_TPL.format(intCD=intCD))
    if quest:
        return quest.getDescription()
    return ''


@dependency.replace_none_kwargs(hwCtrl=IHalloweenController)
def isCustomizationHangarDisabled(hwCtrl=None):
    return hwCtrl.isEventPrb()


@dependency.replace_none_kwargs(ctrl=IHalloweenController)
def getVehicleState(vehicle, ctrl=None):
    state = VehicleStates.DEFAULT
    if not ctrl.hasAccessToVehicle(vehicle.intCD):
        state = VehicleStates.LOCKED
    elif vehicle.isInBattle:
        state = VehicleStates.INBATTLE
    elif vehicle.isInUnit:
        state = VehicleStates.INPLATOON
    elif vehicle.isAwaitingBattle:
        state = VehicleStates.INQUEUE
    return state


@dependency.replace_none_kwargs(ctrl=IHalloweenArtefactsController)
def getArtefactState(artefactID, ctrl=None):
    state = ArtefactStates.INPROGRESS
    if ctrl.isArtefactReceived(artefactID):
        state = ArtefactStates.RECEIVE
    elif ctrl.isArtefactOpened(artefactID):
        state = ArtefactStates.OPEN
    return state


def fillRewardsForTooltips(bonusRewards, bonusModels, maxBonuseInView, skipBonuses=None):
    formatter = HalloweenBonusesAwardsComposer(maxBonuseInView, getHWMetaAwardFormatter())
    sortedBonuses = sorted(bonusRewards, cmp=compareBonusesByPriority)
    bonusRewards = formatter.getFormattedBonuses(sortedBonuses, AWARDS_SIZES.BIG)
    for bonus in bonusRewards:
        if skipBonuses is not None and bonus.bonusName in skipBonuses:
            continue
        reward = BonusItemViewModel()
        fillBaseBonusProperties(bonus, reward)
        bonusModels.addViewModel(reward)

    return


@dependency.replace_none_kwargs(ctrl=IHalloweenController)
def fillProminentBonus(resourceID, bonusRewards, bonusItemModel, ctrl=None):
    formatter = HalloweenBonusesAwardsComposer(INF_DISPLAY_BONUSES, getHWMetaAwardFormatter())
    sortedBonuses = sorted(bonusRewards, cmp=compareBonusesByPriority)
    bonusRewards = formatter.getFormattedBonuses(sortedBonuses, AWARDS_SIZES.BIG)
    prominentBonusType = ctrl.getModeSettings().prominentBonus.get(resourceID, '')
    if not prominentBonusType:
        return
    else:
        for bonus in bonusRewards:
            if prominentBonusType not in (bonus.bonusName, bonus.itemTypeName):
                continue
            fillBaseBonusProperties(bonus, bonusItemModel)
            bonusItemModel.setTooltipId(PROMINENT_REWARD_TOOLTIP_ID)
            return bonus

        return


def fillBaseBonusProperties(bonus, bonusModel):
    bonusModel.setUserName(str(bonus.userName))
    bonusModel.setName(bonus.bonusName)
    bonusModel.setValue(str(bonus.label))
    bonusModel.setLabel(str(bonus.label))
    bonusModel.setIcon(getImgName(bonus.getImage(AWARDS_SIZES.BIG)))
    bonusModel.setOverlayType(bonus.getOverlayType(AWARDS_SIZES.SMALL))


def getQuestFinishTimeLeft(quest):
    if quest is None:
        return 0
    else:
        if quest.bonusCond.isDaily():
            return int(EventInfoModel.getDailyProgressResetTimeDelta())
        return quest.getFinishTimeLeft()


@dependency.replace_none_kwargs(ctrl=IHalloweenArtefactsController)
def fillRewards(artefact, bonusModels, maxBonuseInView, idGen, rewardsHighlight=None, ctrl=None):
    bonusCache = {}
    rewardsHighlight = rewardsHighlight or []
    bonusRewards = artefact.bonusRewards
    formatter = HalloweenBonusesAwardsComposer(maxBonuseInView, getHWMetaAwardFormatter())
    sortedBonuses = sorted(bonusRewards, cmp=compareBonusesByPriority)
    bonusRewards = formatter.getFormattedBonuses(sortedBonuses, AWARDS_SIZES.BIG)
    for bonus in bonusRewards:
        tooltipId = ('{}').format(idGen.next())
        bonusCache[tooltipId] = bonus
        reward = BonusItemViewModel()
        reward.setUserName(str(bonus.userName))
        reward.setName(bonus.bonusName)
        reward.setValue(str(bonus.label))
        reward.setLabel(str(bonus.label))
        reward.setIcon(getImgName(bonus.getImage(AWARDS_SIZES.BIG)))
        reward.setOverlayType(bonus.getOverlayType(AWARDS_SIZES.SMALL))
        reward.setTooltipId(tooltipId)
        reward.setIsRewardShined(bonus.bonusName in rewardsHighlight)
        bonusModels.addViewModel(reward)

    return bonusCache