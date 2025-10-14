from constants import ARENA_GUI_TYPE
from frontline.constants.common import FRONTLINE_GROUPS
from gui.impl.battle.battle_page.ammunition_panel.groups_controller import RespawnAmmunitionGroupsController
from gui.impl.common.ammunition_panel.ammunition_groups_controller import RANDOM_GROUPS
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider

class FLRespawnAmmunitionGroupsController(RespawnAmmunitionGroupsController):
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def _getGroups(self):
        arenaGuiType = self.__sessionProvider.arenaVisitor.getArenaGuiType()
        if arenaGuiType in (ARENA_GUI_TYPE.EPIC_BATTLE, ARENA_GUI_TYPE.EPIC_TRAINING):
            return FRONTLINE_GROUPS
        return RANDOM_GROUPS