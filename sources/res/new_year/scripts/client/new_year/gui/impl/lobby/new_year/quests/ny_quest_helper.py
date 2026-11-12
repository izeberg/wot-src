import typing
from gui.shared.missions.packers.events import findFirstConditionModel
from helpers import dependency, time_utils
from helpers.time_utils import ONE_WEEK
from new_year.helpers.server_settings import getNewYearGeneralConfig
from new_year_common.items.components.ny_constants import CurrentNYConstants
from shared_utils import first
from skeletons.gui.shared import IItemsCache
if typing.TYPE_CHECKING:
    from gui.impl.gen.view_models.common.missions.daily_quest_model import DailyQuestModel
    from gui.server_events.event_items import TokenQuest

def getWeekFromStart():
    return int(time_utils.getServerUTCTime() - getNewYearGeneralConfig().getNewYearStartDate()) / ONE_WEEK


def getCurrentWeek():
    return max(1, min(getWeekFromStart() + 1, CurrentNYConstants.MAX_CELEB_TEXTS))


@dependency.replace_none_kwargs(itemsCache=IItemsCache)
def modifyTokenQuestConditions(quest, questModel, itemsCache=None):
    token = first(quest.accountReqs.getTokens())
    if token is None:
        return
    else:
        postBattleModel = findFirstConditionModel(questModel.postBattleCondition)
        if postBattleModel is None:
            postBattleModel = findFirstConditionModel(questModel.bonusCondition)
        if postBattleModel is None:
            return
        neededCount = token.getNeededCount()
        currTokenCount = token.getReceivedCount()
        lastViewedTokenCount = itemsCache.items.tokens.getLastViewedProgress(token.getID())
        earned = currTokenCount - lastViewedTokenCount if currTokenCount >= lastViewedTokenCount else currTokenCount
        postBattleModel.setTotal(neededCount)
        postBattleModel.setCurrent(neededCount if quest.isCompleted() else currTokenCount)
        postBattleModel.setEarned(earned)
        return