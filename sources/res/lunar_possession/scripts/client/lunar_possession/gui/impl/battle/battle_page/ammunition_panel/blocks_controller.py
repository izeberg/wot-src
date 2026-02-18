import typing
from gui.impl.battle.battle_page.ammunition_panel.blocks_controller import PrebattleShellsBlock, _EMPTY_INT_COMPACT_DESCRIPTOR
from gui.impl.common.ammunition_panel.ammunition_blocks_controller import AmmunitionBlocksController
from gui.impl.gen.view_models.views.lobby.tank_setup.tank_setup_constants import TankSetupConstants
from gui.impl.common.tabs_controller import tabUpdateFunc
from helpers import dependency
from skeletons.account_helpers.settings_core import ISettingsCore
if typing.TYPE_CHECKING:
    from gui.shared.gui_items import Vehicle

class LunarPrebattleShellsBlock(PrebattleShellsBlock):

    def _updateSlotWithItem(self, model, idx, slotItem):
        super(LunarPrebattleShellsBlock, self)._updateSlotWithItem(model, idx, slotItem)
        model.setIsInfinity(True)


class LunarPrebattleAmmunitionBlocksController(AmmunitionBlocksController):
    __settingsCore = dependency.descriptor(ISettingsCore)
    __slots__ = ('__nextShellIntCD', '__currentShellIntCD')

    def __init__(self, vehicle, autoCreating=True, ctx=None):
        super(LunarPrebattleAmmunitionBlocksController, self).__init__(vehicle, autoCreating, ctx)
        self.__nextShellIntCD = _EMPTY_INT_COMPACT_DESCRIPTOR
        self.__currentShellIntCD = _EMPTY_INT_COMPACT_DESCRIPTOR

    def onNextShellChanged(self, intCD):
        self.__nextShellIntCD = intCD

    def onCurrentShellChanged(self, intCD):
        self.__currentShellIntCD = intCD

    @tabUpdateFunc(TankSetupConstants.SHELLS)
    def _updateShells(self, viewModel, isFirst=False):
        LunarPrebattleShellsBlock(self._vehicle, self._currentSection, self.__nextShellIntCD, self.__currentShellIntCD).adapt(viewModel, isFirst)