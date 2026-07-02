import logging, BigWorld
from events_core_client.score_system.score_system_events import PlayerInfoScoreEvent
from gui.shared import g_eventBus, EVENT_BUS_SCOPE
_logger = logging.getLogger(__name__)

class PlayerInfoScoreComponent(BigWorld.DynamicScriptComponent):

    def set_scores(self, oldValue):
        g_eventBus.handleEvent(PlayerInfoScoreEvent(eventType=PlayerInfoScoreEvent.SCORES_CHANGED, ctx={'oldScores': oldValue, 'newScores': self.scores}), scope=EVENT_BUS_SCOPE.BATTLE)