from __future__ import absolute_import
import BattleReplay
from gui.battle_control.arena_info.arena_descrs import ArenaWithLabelDescription
from gui.impl import backport
from white_tiger.gui.wt_event_helpers import isBossTeam
from gui.impl.gen import R

class WhiteTigerArenaDescription(ArenaWithLabelDescription):

    def getDescriptionString(self, isInBattle=True):
        return backport.text(R.strings.white_tiger_lobby.headerButtons.battle.types.white_tiger())

    def getWinString(self, isInBattle=True):
        if isBossTeam(self._team):
            return backport.text(R.strings.white_tiger_battle_hints.loading.winText.boss())
        return backport.text(R.strings.white_tiger_battle_hints.loading.winText.hunters())

    def getTeamName(self, team):
        if isBossTeam(team):
            return backport.text(R.strings.white_tiger_battle.stats.team.boss())
        return backport.text(R.strings.white_tiger_battle.stats.team.hunters())

    def isInvitationEnabled(self):
        replayCtrl = BattleReplay.g_replayCtrl
        return not replayCtrl.isPlaying