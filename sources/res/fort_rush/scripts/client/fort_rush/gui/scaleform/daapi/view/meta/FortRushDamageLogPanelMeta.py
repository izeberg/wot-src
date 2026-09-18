from gui.Scaleform.daapi.view.battle.shared.damage_log_panel import DamageLogPanel

class FortRushDamageLogPanelMeta(DamageLogPanel):

    def as_updateSummaryFortRushValueS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_updateSummaryFortRushValue(value)