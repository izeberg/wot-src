from gui.impl.lobby.tank_setup.ammunition_panel.blocks_controller import HangarAmmunitionBlocksController
from gui.prb_control import prbDispatcherProperty
from gui.impl.common.ammunition_panel.ammunition_groups_controller import AmmunitionGroupsController, RANDOM_GROUPS

class HangarAmmunitionGroupsController(AmmunitionGroupsController):
    __slots__ = ()

    @prbDispatcherProperty
    def prbDispatcher(self):
        return

    def _getGroups(self):
        if self._vehicle is None:
            return []
        else:
            return RANDOM_GROUPS

    def _createAmmunitionBlockController(self, vehicle, ctx=None):
        return HangarAmmunitionBlocksController(vehicle, ctx=ctx)