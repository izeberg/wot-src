from __future__ import absolute_import
from future.utils import lrange
from gui.battle_control.arena_info.squad_finder import TeamScopeNumberingFinder

class LSTeamScopeNumberingFinder(TeamScopeNumberingFinder):
    __slots__ = ()

    @classmethod
    def _getSquadRange(cls):
        return lrange(2, 6)