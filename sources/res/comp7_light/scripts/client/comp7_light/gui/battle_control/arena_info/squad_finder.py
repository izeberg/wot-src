from gui.battle_control.arena_info.squad_finder import TeamScopeNumberingFinder

class Comp7LightTeamScopeNumberingFinder(TeamScopeNumberingFinder):
    __slots__ = ()

    @classmethod
    def _getSquadRange(cls):
        return xrange(2, 8)