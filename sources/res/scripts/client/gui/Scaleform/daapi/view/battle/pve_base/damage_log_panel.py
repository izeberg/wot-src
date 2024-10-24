from account_helpers.settings_core.settings_constants import GRAPHICS
from gui.Scaleform.daapi.view.battle.shared.damage_log_panel import DamageLogPanel

class PveDamageLogPanel(DamageLogPanel):

    def _invalidatePanelVisibility(self):
        if self._isFullStatsShown or self._isWinnerScreenShown:
            return
        if not self._isVisible:
            self._isVisible = True
            self._setSettings(self._isVisible, bool(self.settingsCore.getSetting(GRAPHICS.COLOR_BLIND)))