from armory_quests_common.armory_quests_cache import getArmoryQuestsCache
from armory_yard.skeletons.armory_yard_reroll_controller import IArmoryYardRerollController
from armory_yard_constants import CONDITION_PREFIX, getConditionTokenByQuestID, getConditionToken
from gui.Scaleform.daapi.view.lobby.server_events.events_helpers import QuestPostBattleInfo
from gui.impl import backport
from gui.impl.gen import R
from gui.server_events import conditions, formatters
from gui.server_events.event_items import IExtensionQuestsSource
from helpers import dependency
from skeletons.gui.game_control import IArmoryYardController
from skeletons.gui.shared import IItemsCache

class ArmoryPlayerConditionQuestsSource(IExtensionQuestsSource):
    __armoryYardController = dependency.descriptor(IArmoryYardController)
    __armoryYardRerollCtrl = dependency.descriptor(IArmoryYardRerollController)
    __itemsCache = dependency.descriptor(IItemsCache)

    def isActive(self):
        return self.__armoryYardController.isActive() and self.__armoryYardRerollCtrl.isRerollEnabled()

    def questInSource(self, questID):
        if questID.startswith(CONDITION_PREFIX):
            condToken = getConditionTokenByQuestID(questID)
            return questID in getArmoryQuestsCache().get(condToken, {})
        return False

    def getQuestsData(self):
        result = {}
        for tokenQuestID, defaultConditionID in self.__armoryYardController.serverSettings.iterByDefaultRerollQuests():
            conditionID = self.__itemsCache.items.armoryYard.overrideConditions.get(tokenQuestID, defaultConditionID)
            if conditionID is not None:
                result.update(getArmoryQuestsCache().get(getConditionToken(conditionID), {}))

        return result

    def getQuestByID(self, questID):
        if questID.startswith(CONDITION_PREFIX):
            condToken = getConditionTokenByQuestID(questID)
            return getArmoryQuestsCache().get(condToken, {}).get(questID, None)
        else:
            return


class ArmoryDynamicQuestPostBattleInfo(QuestPostBattleInfo):
    __armoryYardRerollCtrl = dependency.descriptor(IArmoryYardRerollController)

    def getPostBattleInfo(self, svrEvents, pCur, pPrev, isProgressReset, isCompleted, progressData):
        tokenQuest = self.event.getTokenQuest()
        if tokenQuest is not None and not tokenQuest.isCompleted():
            return super(ArmoryDynamicQuestPostBattleInfo, self).getPostBattleInfo(svrEvents, pCur, pPrev, isProgressReset, isCompleted, progressData)
        else:
            return

    def _getProgresses(self, pCur, pPrev):
        index = 0
        progresses = []
        customQuestDescr = self.event.getDescription()
        for cond in self.event.bonusCond.getConditions().items:
            if isinstance(cond, conditions.Cumulativable):
                for _, (curProg, totalProg, diff, _) in cond.getProgressPerGroup(pCur, pPrev).iteritems():
                    if cond.getKey() in ('battlesCount', 'sum'):
                        label = cond.getCustomDescription() or customQuestDescr
                    elif cond.getKey() in ('vehicleKills', 'vehicleDamage', 'vehicleStun'):
                        label = cond.getCustomDescription() or cond.getUserString()
                    else:
                        label = cond.getUserString()
                    if not diff or not label:
                        continue
                    index += 1
                    progresses.append({'progrTooltip': None, 
                       'progrBarType': formatters.PROGRESS_BAR_TYPE.SIMPLE, 
                       'maxProgrVal': totalProg, 
                       'currentProgrVal': curProg, 
                       'description': '%d. %s' % (index, label), 
                       'progressDiff': '+ %s' % backport.getIntegralFormat(diff), 
                       'progressDiffTooltip': backport.text(R.strings.tooltips.quests.progress.earnedInBattle())})

        return progresses