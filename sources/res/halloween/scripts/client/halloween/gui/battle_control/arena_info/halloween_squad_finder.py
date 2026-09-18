from __future__ import absolute_import
from builtins import range
from gui.battle_control.arena_info.squad_finder import TeamScopeNumberingFinder

class HalloweenTeamScopeNumberingFinder(TeamScopeNumberingFinder):
    __slots__ = ()

    @classmethod
    def _getSquadRange(cls):
        return range(2, 6)