from grinch.gui.Scaleform.daapi.view.battle.hint_panel import plugins
from gui.Scaleform.daapi.view.battle.shared.hint_panel.component import BattleHintPanel

class GrinchBattleHintPanel(BattleHintPanel):

    def _createPlugins(self):
        return plugins.createPlugin()