import typing
from helpers import dependency
from new_year.interactive_state_machine.constants import PersonaTypes
from new_year.interactive_state_machine.sm_handler import StateMachineHandler
from new_year.skeletons.i_sm_queue_context import IQueueContext
from new_year.skeletons.new_year import ITamagotchiDataProvider

class OldManStateMachineHandler(StateMachineHandler):
    __slots__ = ()
    _TYPE = PersonaTypes.OLD_MAN
    _WARNING_S = 'warning'
    __dataProvider = dependency.descriptor(ITamagotchiDataProvider)
    __context = dependency.descriptor(IQueueContext)

    def handleLoaded(self):
        if not self.isHangarViewLoaded or self.__context.isLocked:
            return False
        if self.__getLowStats() and not self.__context.firstBattleLatch and self.__context.wasInBattle:
            return self._handleMood()
        return self._handleGreeting()

    def _handleFirstEnter(self):
        return False

    def _handleNewWeek(self):
        return False

    def _handleNewEnter(self):
        return False

    def _handleMood(self):
        lowStats = self.__getLowStats()
        if not lowStats:
            return False
        self.__context.firstBattleLatch = True
        if len(lowStats) > 1:
            self.setTrigger(self._WARNING_S)
            return True
        self.setTrigger(lowStats[0])
        return True

    def __getLowStats(self):
        if not self.__dataProvider.raccoonState:
            return []
        indicatorStates = self.__dataProvider.getIndicatorStates()
        return [ stat for stat, level in indicatorStates.iteritems() if level <= 1 ]