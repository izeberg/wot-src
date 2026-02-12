from gui.impl.battle.battle_page.ammunition_panel.groups_controller import PrebattleAmmunitionGroupsController
from lunar_possession.gui.impl.battle.battle_page.ammunition_panel.blocks_controller import LunarPrebattleAmmunitionBlocksController

class LunarPrebattleAmmunitionGroupsController(PrebattleAmmunitionGroupsController):

    def _createAmmunitionBlockController(self, vehicle, ctx=None):
        return LunarPrebattleAmmunitionBlocksController(vehicle, ctx=ctx)