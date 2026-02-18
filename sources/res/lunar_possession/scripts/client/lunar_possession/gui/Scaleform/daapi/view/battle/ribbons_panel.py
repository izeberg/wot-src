from gui.Scaleform.daapi.view.battle.shared.ribbons_panel import BattleRibbonsPanel
from lunar_possession.gui.Scaleform.daapi.view.battle import ribbons_aggregator
from gui.impl import backport
from lunar_possession.gui.Scaleform.genConsts.LUNAR_BATTLE_EFFICIENCY_TYPES import LUNAR_BATTLE_EFFICIENCY_TYPES
from gui.impl.gen import R

class LunarPossessionBattleRibbonsPanel(BattleRibbonsPanel):

    def __init__(self):
        super(LunarPossessionBattleRibbonsPanel, self).__init__(ribbonsAggregator=ribbons_aggregator.createRibbonsAggregator())

    def _getRibbonsConfig(self):
        config = super(LunarPossessionBattleRibbonsPanel, self)._getRibbonsConfig()
        config.extend([
         [
          LUNAR_BATTLE_EFFICIENCY_TYPES.SPIRIT_CARRIER_DOT,
          backport.text(R.strings.lunar_battle.ribbon.efficiencyRibbons.spiritCarrierDot())]])
        return config