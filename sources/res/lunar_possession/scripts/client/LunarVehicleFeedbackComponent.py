from gui.shared import g_eventBus, EVENT_BUS_SCOPE
from helpers import dependency
from lunar_possession.gui.shared.events import PlayerScoreUpdatedEvents
from script_component.DynamicScriptComponent import DynamicScriptComponent
from skeletons.gui.battle_session import IBattleSessionProvider

class LunarVehicleFeedbackComponent(DynamicScriptComponent):
    _sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def _onAvatarReady(self):
        self._sendScoreUpdate()

    def set_scoreTotal(self, oldTotal):
        self._sendScoreUpdate()

    def _sendScoreUpdate(self):
        g_eventBus.handleEvent(PlayerScoreUpdatedEvents(PlayerScoreUpdatedEvents.PLAYER_SCORE_UPDATED, score=self.scoreTotal), scope=EVENT_BUS_SCOPE.BATTLE)