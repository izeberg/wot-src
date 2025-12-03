from AbilityEquipment import AbilityEquipment

class DamageModifierAbilityEquipment(AbilityEquipment):

    def set_currentDamageModifier(self, _):
        currentDamageModifier = self.currentDamageModifier
        equipments = self._sessionProvider.shared.equipments
        equipments.onUpdateDamageModifier(self.compactDescr, currentDamageModifier)