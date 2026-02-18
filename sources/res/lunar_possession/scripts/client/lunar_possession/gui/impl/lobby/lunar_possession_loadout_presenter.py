import typing
from fun_random.gui.impl.lobby.hangar.presenters.fun_random_loadout_presenter import FunRandomLoadoutPresenter, FunRandomShellsPresenter
from gui.impl.gen import R
from lunar_possession.gui.impl.lobby.lunar_possession_ammunition_panel import LunarPossessionHangarAmmunitionGroupsController
if typing.TYPE_CHECKING:
    from gui.impl.common.ammunition_panel.ammunition_groups_controller import AmmunitionGroupsController
    from gui.impl.gen.view_models.views.lobby.loadout.shells.shells_model import ShellsModel
    from gui.impl.pub.view_component import ViewComponent

class LunarPossessionLoadoutPresenter(FunRandomLoadoutPresenter):

    def _getChildComponents(self):
        children = super(LunarPossessionLoadoutPresenter, self)._getChildComponents()
        hangar = R.aliases.hangar.shared
        children[hangar.Shells()] = lambda : LunarPossessionShellsPresenter(self._vehInteractingItem)
        return children

    @property
    def _getGroupControllerCls(self):
        return LunarPossessionHangarAmmunitionGroupsController


class LunarPossessionShellsPresenter(FunRandomShellsPresenter):

    def _onLoading(self):
        super(LunarPossessionShellsPresenter, self)._onLoading()
        model = self.getViewModel()
        model.setIsInfinityShells(True)