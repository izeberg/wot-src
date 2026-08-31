from __future__ import absolute_import
from gui.prb_control.entities.base.pre_queue.permissions import PreQueuePermissions

class BattleRoyaleTournamentPermissions(PreQueuePermissions):

    def canCreateSquad(self):
        return False