import logging, typing
from grinch_progression.gui.impl.gen.view_models.views.lobby.views.mission_model import MissionModel
from grinch_progression.gui.impl.lobby.views.quests_helper import isGrinchWeekendQuestID, getRoleStr, vehicleRoleStrToModel, isSpecialQuest
from grinch_progression.skeletons.game_controller import IGrinchProgressionController
from grinch.gui.impl.gen.view_models.views.lobby.post_battle.post_battle_mission_model import PostBattleMissionModel
from gui.impl import backport
from gui.impl.gen import R
from gui.server_events.bonuses import BattleTokensBonus
from gui.shared.missions.packers.events import findFirstConditionModel, getEventUIDataPacker
import constants
from helpers import dependency
if typing.TYPE_CHECKING:
    from typing import Optional
    from gui.server_events.event_items import ServerEventAbstract
    from gui.impl.gen.view_models.common.missions.daily_quest_model import DailyQuestModel
    from gui.impl.gen.view_models.common.missions.conditions.preformatted_condition_model import PreformattedConditionModel
_logger = logging.getLogger(__name__)

@dependency.replace_none_kwargs(grinchProgressionCtrl=IGrinchProgressionController)
def calculatePrize(quest, grinchProgressionCtrl=None):
    bonusTokenCount = 0
    for bonus in quest.getBonuses():
        if not isinstance(bonus, BattleTokensBonus):
            continue
        bonusTokens = bonus.getTokens()
        for tokenID, token in bonusTokens.iteritems():
            if tokenID == grinchProgressionCtrl.token:
                bonusTokenCount += token.count
                break

    return bonusTokenCount


class GrinchDailyQuestUIDataPacker(object):

    def __init__(self, event):
        self._event = event

    def pack(self):
        model = MissionModel()
        self._packModel(model)
        self._packPrize(model)
        return model

    @classmethod
    def _getFirstConditionModelFromQuestModel(cls, dailyQuestModel):
        postBattleModel = findFirstConditionModel(dailyQuestModel.postBattleCondition)
        bonusConditionModel = findFirstConditionModel(dailyQuestModel.bonusCondition)
        if postBattleModel and (postBattleModel.getConditionType() != 'win' or not bonusConditionModel):
            return postBattleModel
        return bonusConditionModel

    def _packModel(self, cardModel):
        questUIPacker = getEventUIDataPacker(self._event)
        fullQuestModel = questUIPacker.pack()
        postbattleConditionModel = self._getFirstConditionModelFromQuestModel(fullQuestModel)
        if postbattleConditionModel is None:
            return
        else:
            if fullQuestModel.getDescription():
                postbattleConditionModel.setDescrData(fullQuestModel.getDescription())
            self._feedModel(cardModel, postbattleConditionModel)
            return

    def _packPrize(self, cardModel):
        bonusTokenCount = calculatePrize(self._event)
        if bonusTokenCount:
            cardModel.setPrize(bonusTokenCount)
        else:
            _logger.warning("Can't find token bonus")

    def _feedModel(self, model, postbattleConditionModel):
        model.setDescription(postbattleConditionModel.getDescrData())
        currentProgress = postbattleConditionModel.getCurrent()
        if currentProgress == 0 and self._event.isCompleted():
            currentProgress = 1
        model.setCurrent(currentProgress)
        model.setTarget(postbattleConditionModel.getTotal() or 1)
        model.setQuestId(self._event.getID())
        isEventMission = isGrinchWeekendQuestID(self._event.getID())
        model.setIsEventMission(isEventMission)
        if isEventMission:
            model.setRole(vehicleRoleStrToModel(getRoleStr(self._event)))


class GrinchRandomDailyQuestUIDataPacker(GrinchDailyQuestUIDataPacker):

    def _feedModel(self, model, postbattleConditionModel):
        condStr = backport.text(R.strings.grinch_progression.gameBoardView.missionsDialog.precondition.random())
        model.setPrecondition(condStr)
        super(GrinchRandomDailyQuestUIDataPacker, self)._feedModel(model, postbattleConditionModel)


class GrinchPostBattleQuestUIDataPacker(GrinchDailyQuestUIDataPacker):

    def pack(self):
        model = PostBattleMissionModel()
        self._packModel(model)
        self._packPrize(model)
        return model

    def _feedModel(self, model, postbattleConditionModel):
        model.setDescription(postbattleConditionModel.getDescrData())
        model.setCurrentProgress(postbattleConditionModel.getCurrent())
        model.setTotalProgress(postbattleConditionModel.getTotal())


def getGrinchUIDataPacker(event):
    if event.getType() in constants.EVENT_TYPE.LIKE_BATTLE_QUESTS:
        if isSpecialQuest(event):
            return GrinchRandomDailyQuestUIDataPacker(event)
        return GrinchDailyQuestUIDataPacker(event)
    else:
        _logger.warning('Only LIKE_BATTLE_QUESTS allowed')
        return


def getGrinchPostBattleUIDataPacker(event):
    if event.getType() in constants.EVENT_TYPE.LIKE_BATTLE_QUESTS:
        return GrinchPostBattleQuestUIDataPacker(event)
    else:
        _logger.warning('Only LIKE_BATTLE_QUESTS allowed')
        return