from __future__ import absolute_import
from future.utils import lrange
from gui.battle_control.arena_info.squad_finder import TeamScopeNumberingFinder

class Comp7TeamScopeNumberingFinder(TeamScopeNumberingFinder):
    __slots__ = ()

    @classmethod
    def _getSquadRange(cls):
        return lrange(2, 8)