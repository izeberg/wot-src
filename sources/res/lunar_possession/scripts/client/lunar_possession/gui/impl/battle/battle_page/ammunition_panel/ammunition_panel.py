from gui.impl.battle.battle_page.ammunition_panel.ammunition_panel import PrebattleAmmunitionPanel
from lunar_possession.gui.impl.battle.battle_page.ammunition_panel.groups_controller import LunarPrebattleAmmunitionGroupsController

class LunarPrebattleAmmunitionPanel(PrebattleAmmunitionPanel):

    def _createAmmunitionGroupsController(self, vehicle):
        return LunarPrebattleAmmunitionGroupsController(vehicle, ctx=self._ctx)