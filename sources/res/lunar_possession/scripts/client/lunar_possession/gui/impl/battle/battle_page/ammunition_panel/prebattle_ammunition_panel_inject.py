from gui.impl.battle.battle_page.ammunition_panel.prebattle_ammunition_panel_inject import PrebattleAmmunitionPanelInject
from lunar_possession.gui.impl.battle.battle_page.ammunition_panel.prebattle_ammunition_panel_view import LunarPrebattleAmmunitionPanelView

class LunarPrebattleAmmunitionPanelInject(PrebattleAmmunitionPanelInject):

    def _makeInjectView(self, vehicle, *args):
        return LunarPrebattleAmmunitionPanelView(vehicle, *args)