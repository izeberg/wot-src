from frontline.gui.impl.battle.battle_page.ammunition_panel.groups_controller import FLRespawnAmmunitionGroupsController
from gui.impl.common.ammunition_panel.base import BaseAmmunitionPanel

class FLRespawnAmmunitionPanel(BaseAmmunitionPanel):

    def _createAmmunitionGroupsController(self, vehicle):
        return FLRespawnAmmunitionGroupsController(vehicle, ctx=self._ctx)