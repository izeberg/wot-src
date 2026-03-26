from __future__ import absolute_import
import BattleReplay
from gui.battle_control.arena_info.arena_descrs import ArenaWithLabelDescription

class LSArenaDescription(ArenaWithLabelDescription):

    def isInvitationEnabled(self):
        replayCtrl = BattleReplay.g_replayCtrl
        return not replayCtrl.isPlaying

    def getArenaBonusType(self):
        return self._visitor.getArenaBonusType()