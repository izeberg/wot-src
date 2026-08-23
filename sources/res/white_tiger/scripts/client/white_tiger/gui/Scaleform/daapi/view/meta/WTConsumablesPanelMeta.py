from gui.Scaleform.daapi.view.battle.shared.consumables_panel import ConsumablesPanel

class WTConsumablesPanelMeta(ConsumablesPanel):

    def as_wtShowActiveS(self, idx, time=0):
        if self._isDAAPIInited():
            return self.flashObject.as_wtShowActive(idx, time)

    def as_wtSetDisabledS(self, idx, value):
        if self._isDAAPIInited():
            return self.flashObject.as_wtSetDisabled(idx, value)

    def as_wtShowCooldownS(self, idx, time):
        if self._isDAAPIInited():
            return self.flashObject.as_wtShowCooldown(idx, time)

    def as_wtShowReadyS(self, idx):
        if self._isDAAPIInited():
            return self.flashObject.as_wtShowReady(idx)

    def as_wtSetChargeProgressS(self, idx, charge):
        if self._isDAAPIInited():
            return self.flashObject.as_wtSetChargeProgress(idx, charge)

    def as_wtShowPreparingS(self, idx):
        if self._isDAAPIInited():
            return self.flashObject.as_wtShowPreparing(idx)

    def as_wtShowDeployingS(self, idx):
        if self._isDAAPIInited():
            return self.flashObject.as_wtShowDeploying(idx)

    def as_wtSetLockedS(self, idx, value):
        if self._isDAAPIInited():
            return self.flashObject.as_wtSetLocked(idx, value)

    def as_wtAddPassiveAbilitySlotS(self, idx, iconPath, tooltipText):
        if self._isDAAPIInited():
            return self.flashObject.as_wtAddPassiveAbilitySlot(idx, iconPath, tooltipText)