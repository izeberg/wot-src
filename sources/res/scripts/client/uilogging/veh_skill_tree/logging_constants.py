from enum import Enum
FEATURE_VEH_SKILL_TREE = 'veh_skill_tree'
VEH_SKILL_TREE_SCREEN = 'tier_11_progression_screen'

class VehSkillTreeActions(str, Enum):
    CLICK = 'click'
    OPEN = 'open'
    CLOSE = 'close'


class VehSkillTreeItems(str, Enum):
    SKILL_TREE = 'skill_tree'
    RESEARCH_BUTTON = 'research_button'