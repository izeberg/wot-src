from __future__ import absolute_import
import logging, typing
from gui.impl.gen.view_models.common.missions.conditions.condition_group_model import ConditionGroupModel
from gui.shared.missions.packers.conditions import PostBattleConditionPacker, BonusConditionPacker
from gui.shared.missions.packers.events import findFirstConditionModel
from helpers_common import reprSlots
from journey_marathon.jm_helpers import jmCtrl
if typing.TYPE_CHECKING:
    from typing import Iterable, Optional, List
    from gui.server_events.event_items import Quest
    from gui.impl.gen.view_models.common.missions.conditions.preformatted_condition_model import PreformattedConditionModel as ConditionModel
_error = logging.getLogger(__name__).error
_topByMaxRange = {1: 'top1', 3: 'top3', 5: 'top5', 7: 'top7'}

class JmQuestInfo(object):
    __slots__ = ('id', 'isCumulative', 'isCompleted', 'currProgress', 'totalProgress',
                 'descr', 'iconKey', 'coinCount')

    def __init__(self, qID, isCumulative, isCompleted, currProgress, totalProgress, descr, iconKey, coinCount):
        self.id = qID
        self.isCumulative = isCumulative
        self.isCompleted = isCompleted
        self.currProgress = currProgress
        self.totalProgress = totalProgress
        self.descr = descr
        self.iconKey = iconKey
        self.coinCount = coinCount

    __repr__ = reprSlots


def packJmQuests(quests):
    coinToken, _, __ = jmCtrl().jmTokens.getJmCoinToken()
    packPostBattleCondition = PostBattleConditionPacker().pack
    packBonusCondition = BonusConditionPacker().pack
    qInfos = []
    for quest in quests:
        qID = quest.getID()
        isCompleted = quest.isCompleted()
        coinCount = getJmQuestTokenBonusCount(quest, coinToken)
        if coinCount <= 0:
            coinCount = 1
            _error('Quest must have coin tokens as reward, qID = %s', quest.getID())
        rootPostBattle = ConditionGroupModel()
        packPostBattleCondition(quest, rootPostBattle)
        postBattle = findFirstConditionModel(rootPostBattle)
        rootBonusCond = ConditionGroupModel()
        packBonusCondition(quest, rootBonusCond)
        bonusCond = findFirstConditionModel(rootBonusCond)
        bonusCondPriority = bonusCond or postBattle
        postBattlePriority = postBattle or bonusCond
        iconKey = 'folder'
        if bonusCondPriority is None:
            _error('Failed to parse quest = %s', qID)
            descr = ''
            isCumulative = False
            currProgress = 0
            totalProgress = 1
        else:
            descr = quest.getDescription() or bonusCondPriority.getDescrData()
            isCumulative = bonusCondPriority.getConditionType() in ('cumulative', 'battles')
            totalProgress = bonusCondPriority.getTotal() or 1
            currProgress = totalProgress if isCompleted else bonusCondPriority.getCurrent()
            iconKey = 'folder'
            postBattleItems = rootPostBattle.getItems()
            bonusItems = rootBonusCond.getItems()
            if not (len(postBattleItems) > 1 or len(bonusItems) > 1):
                iconKey = postBattlePriority.getIconKey()
                if iconKey == 'top':
                    results = quest.postBattleCond.getConditions().find('results')
                    if results is not None:
                        _, maxRange = results.getMaxRange()
                        iconKey = _topByMaxRange.get(maxRange, 'top')
        qInfo = JmQuestInfo(qID, isCumulative, isCompleted, currProgress, totalProgress, descr, iconKey, coinCount)
        qInfos.append(qInfo)

    return qInfos


def getJmQuestTokenBonusCount(quest, token):
    return quest.getRawBonuses().get('tokens', {}).get(token, {}).get('count', 0)