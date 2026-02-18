from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor
from lunar_possession.gui.impl.battle.top_score_panel.lunar_possession_top_score_panel import LunarPossessionTopScorePanelView

class LunarPossessionTopScorePanel(InjectComponentAdaptor):

    def _makeInjectView(self):
        return LunarPossessionTopScorePanelView()