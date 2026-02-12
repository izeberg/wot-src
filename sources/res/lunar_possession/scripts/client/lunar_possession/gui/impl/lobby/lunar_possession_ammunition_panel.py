from gui.impl.common.ammunition_panel.ammunition_panel_blocks import ShellsBlock
from gui.impl.gen.view_models.views.lobby.tank_setup.tank_setup_constants import TankSetupConstants
from gui.impl.lobby.tank_setup.ammunition_panel.blocks_controller import HangarAmmunitionBlocksController
from gui.impl.lobby.tank_setup.ammunition_panel.groups_controller import HangarAmmunitionGroupsController
from gui.impl.common.tabs_controller import tabUpdateFunc

class LunarPossessionHangarAmmunitionGroupsController(HangarAmmunitionGroupsController):
    __slots__ = ()

    def _createAmmunitionBlockController(self, vehicle, ctx=None):
        return LunarPossessionAmmunitionBlocksController(vehicle, ctx=ctx)


class LunarPossessionAmmunitionBlocksController(HangarAmmunitionBlocksController):
    __slots__ = ()

    @tabUpdateFunc(TankSetupConstants.SHELLS)
    def _updateShells(self, viewModel, isFirst=False):
        LunarPossessionShellsBlock(self._vehicle, self._currentSection).adapt(viewModel, isFirst)


class LunarPossessionShellsBlock(ShellsBlock):

    def updateBlock(self, viewModel):
        super(LunarPossessionShellsBlock, self).updateBlock(viewModel)
        viewModel.setIsWarning(False)

    def _updateSlotWithItem(self, model, idx, slotItem):
        super(LunarPossessionShellsBlock, self)._updateSlotWithItem(model, idx, slotItem)
        model.setIsInfinity(True)