from enum import Enum
from comp7_core.gui.battle_control.arena_info.arena_vos import Comp7CoreKeys
_DEFAULT_ROLE_SKILL_LEVEL = 0

class Comp7LightKeys(Enum):

    @staticmethod
    def getKeys(static=True):
        if static:
            return [(Comp7CoreKeys.ROLE_SKILL_LEVEL, _DEFAULT_ROLE_SKILL_LEVEL), (Comp7CoreKeys.VOIP_CONNECTED, False)]
        return []

    @staticmethod
    def getSortingKeys(static=True):
        return []