from enum import Enum
from comp7_core.gui.battle_control.arena_info.arena_vos import Comp7CoreKeys
_DEFAULT_ROLE_SKILL_LEVEL = 0
_DEFAULT_PLAYER_RANK = 0
_DEFAULT_PLAYER_DIVISION = 0

class Comp7Keys(Enum):
    RANK = 'rank'
    IS_QUAL_ACTIVE = 'isQualActive'

    @staticmethod
    def getKeys(static=True):
        if static:
            return [(Comp7CoreKeys.ROLE_SKILL_LEVEL, _DEFAULT_ROLE_SKILL_LEVEL), (Comp7Keys.RANK, (_DEFAULT_PLAYER_RANK, _DEFAULT_PLAYER_DIVISION)), (Comp7CoreKeys.VOIP_CONNECTED, False), (Comp7Keys.IS_QUAL_ACTIVE, False)]
        return []

    @staticmethod
    def getSortingKeys(static=True):
        if static:
            return [Comp7Keys.RANK]
        return []


class TournamentComp7Keys(Enum):

    @staticmethod
    def getKeys(static=True):
        if static:
            return [(Comp7CoreKeys.ROLE_SKILL_LEVEL, _DEFAULT_ROLE_SKILL_LEVEL), (Comp7CoreKeys.VOIP_CONNECTED, False)]
        return []

    @staticmethod
    def getSortingKeys(static=True):
        return []