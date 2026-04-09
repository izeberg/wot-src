from gui.Scaleform.daapi.view.battle.shared.consumables_panel import ConsumablesPanel

class HBConsumablesPanelMeta(ConsumablesPanel):

    def as_setShellInfinityS(self, idx, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setShellInfinity(idx, value)

    def as_addAbilitySlotS(self, idx, data):
        if self._isDAAPIInited():
            return self.flashObject.as_addAbilitySlot(idx, data)

    def as_updateAbilityS(self, idx, stage, timeRemaining, maxTime):
        if self._isDAAPIInited():
            return self.flashObject.as_updateAbility(idx, stage, timeRemaining, maxTime)

    def as_addPassiveAbilitySlotS(self, idx, iconPath, state, tooltipText):
        if self._isDAAPIInited():
            return self.flashObject.as_addPassiveAbilitySlot(idx, iconPath, state, tooltipText)

    def as_updatePassiveAbilityS(self, idx, state, tooltipText):
        if self._isDAAPIInited():
            return self.flashObject.as_updatePassiveAbility(idx, state, tooltipText)

    def as_resetPassiveAbilitiesS(self, slots=None):
        if self._isDAAPIInited():
            return self.flashObject.as_resetPassiveAbilities(slots)

    def as_addRoleAbilitySlotS(self, idx, data):
        if self._isDAAPIInited():
            return self.flashObject.as_addRoleAbilitySlot(idx, data)

    def as_setRoleAbilityProgressS(self, idx, progress=0):
        if self._isDAAPIInited():
            return self.flashObject.as_setRoleAbilityProgress(idx, progress)

    def as_setRoleAbilityTooltipS(self, idx, tooltipText):
        if self._isDAAPIInited():
            return self.flashObject.as_setRoleAbilityTooltip(idx, tooltipText)