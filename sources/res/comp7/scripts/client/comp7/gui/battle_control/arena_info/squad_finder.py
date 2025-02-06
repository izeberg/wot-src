from gui.battle_control.arena_info.squad_finder import TeamScopeNumberingFinder

class Comp7TeamScopeNumberingFinder(TeamScopeNumberingFinder):
    __slots__ = ()

    @classmethod
    def _getSquadRange(cls):
        return xrange(2, 8)