from gui.Scaleform.daapi.view.battle.shared.damage_log_panel import DamageLogPanel

class LunarBattleDamageLogPanelMeta(DamageLogPanel):

    def as_updateSummaryLunarValueS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_updateSummaryLunarValue(value)