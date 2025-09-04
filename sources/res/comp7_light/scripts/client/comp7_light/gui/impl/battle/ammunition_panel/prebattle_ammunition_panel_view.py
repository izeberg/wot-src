from comp7_core.gui.impl.battle.ammunition_panel.prebattle_ammunition_panel_view import Comp7CorePrebattleAmmunitionPanelView
from helpers import dependency
from skeletons.gui.game_control import IComp7LightController

class Comp7LightPrebattleAmmunitionPanelView(Comp7CorePrebattleAmmunitionPanelView):
    __comp7LightController = dependency.descriptor(IComp7LightController)

    @property
    def _modeController(self):
        return self.__comp7LightController