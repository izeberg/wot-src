from __future__ import absolute_import
from fort_rush.gui.scaleform.daapi.view.battle import ribbons_aggregator
from fort_rush.gui.scaleform.genConsts.FORT_RUSH_BATTLE_EFFICIENCY_TYPES import FORT_RUSH_BATTLE_EFFICIENCY_TYPES
from gui.Scaleform.daapi.view.battle.shared.ribbons_panel import BattleRibbonsPanel
from gui.impl import backport
from gui.impl.gen import R

class FortRushBattleRibbonsPanel(BattleRibbonsPanel):

    def __init__(self):
        super(FortRushBattleRibbonsPanel, self).__init__(ribbonsAggregator=ribbons_aggregator.createRibbonsAggregator())

    def _getRibbonsConfig(self):
        result = super(FortRushBattleRibbonsPanel, self)._getRibbonsConfig()
        result.extend([
         [
          FORT_RUSH_BATTLE_EFFICIENCY_TYPES.FORT_RUSH_BASE_CAPTURE_HEAL,
          backport.text(R.strings.fort_rush.battleEfficiency.baseHeal())],
         [
          FORT_RUSH_BATTLE_EFFICIENCY_TYPES.FORT_RUSH_POINTS,
          backport.text(R.strings.fort_rush.battleEfficiency.personalPoints())]])
        return result