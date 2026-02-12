from constants import SCENARIO_RESULT
from messenger.formatters.service_channel import BattleResultsFormatter
from fun_random.gui.feature.util.fun_mixins import FunProgressionWatcher
from gui.impl import backport
from gui.impl.gen import R

class LunarPossessionBattleResultsFormatter(BattleResultsFormatter, FunProgressionWatcher):
    _strRes = R.strings.lunar_messenger.notifications.battleResults
    _battleResultKeys = {SCENARIO_RESULT.WIN: 'LunarPossessionBattleResult', 
       SCENARIO_RESULT.PARTIAL: 'LunarPossessionBattleResult', 
       SCENARIO_RESULT.LOSE: 'LunarPossessionBattleResult'}

    def _prepareFormatData(self, message):
        templateName, ctx = super(LunarPossessionBattleResultsFormatter, self)._prepareFormatData(message)
        self.__addLunarCtx(message.data, ctx)
        self.__addProgressionTokenCount(message.data, ctx)
        self.__addMissionCount(message.data, ctx)
        return (templateName, ctx)

    def __addLunarCtx(self, battleResults, ctx):
        isWinner = battleResults.get('isWinner', 0)
        mainResultStr = ('victory' if isWinner == 1 else 'defeat') if isWinner != 0 else 'draw'
        ctx['mainResult'] = backport.text(self._strRes.dyn(mainResultStr).header())
        ctx['eventName'] = backport.text(self._strRes.eventName())

    def __addMissionCount(self, battleResults, ctx):
        triggers = {trigger.getID() for trigger in self.getActiveProgression().conditions.triggers}
        completedMissionsCount = sum(1 for trigger in battleResults.get('completedQuestIDs', set()) if trigger in triggers)
        if not completedMissionsCount:
            ctx['missionsCountStr'] = ''
            return
        ctx['missionsCountStr'] = backport.text(self._strRes.missionsCompleted(), missionsCount=completedMissionsCount)

    def __addProgressionTokenCount(self, battleResults, ctx):
        counterName = self.getActiveProgression().conditions.counterName
        progressionTokens = battleResults.get('tokens', {}).get(counterName, {})
        if not progressionTokens:
            ctx['lunarProgressionTokenStr'] = ''
            return
        ctx['lunarProgressionTokenStr'] = backport.text(self._strRes.progressionTokens(), tokenCount=progressionTokens['count'])