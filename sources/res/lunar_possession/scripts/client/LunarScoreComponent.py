import BigWorld
from gui.shared import EVENT_BUS_SCOPE, g_eventBus
from lunar_possession.gui.shared.events import TeamScoreEvents
from script_component.DynamicScriptComponent import DynamicScriptComponent
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider

class LunarScoreComponent(DynamicScriptComponent):
    sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def set_teamPoints(self, previous):
        if not self._isAvatarReady:
            return
        self._updateTeamPoints()

    def _onAvatarReady(self):
        self._updateTeamPoints()

    def _updateTeamPoints(self):
        followTeamID = BigWorld.player().team
        if followTeamID == 1:
            followScore, enemyScore, targetScore = self.teamPoints
        else:
            enemyScore, followScore, targetScore = self.teamPoints
        g_eventBus.handleEvent(TeamScoreEvents(TeamScoreEvents.TEAM_SCORE_UPDATE, teamScore=(
         followScore, enemyScore, targetScore)), scope=EVENT_BUS_SCOPE.BATTLE)