from comp7_light.gui.impl.battle.ammunition_panel.prebattle_ammunition_panel_view import Comp7LightPrebattleAmmunitionPanelView
from comp7_core.gui.impl.battle.ammunition_panel.prebattle_ammunition_panel_inject import Comp7CorePrebattleAmmunitionPanelInject

class Comp7LightPrebattleAmmunitionPanelInject(Comp7CorePrebattleAmmunitionPanelInject):

    def _makeInjectView(self, vehicle, *args):
        return Comp7LightPrebattleAmmunitionPanelView(vehicle, *args)