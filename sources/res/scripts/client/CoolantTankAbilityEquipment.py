from AbilityEquipment import AbilityEquipment
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
from items import vehicles

class CoolantTankAbilityEquipment(AbilityEquipment):
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def set_currentPenaltyReloadTime(self, _):
        currentPenaltyReloadTime = self.currentPenaltyReloadTime
        ammoCtrl = self.__sessionProvider.shared.ammo
        descriptor = vehicles.getItemByCompactDescr(self.compactDescr)
        reloadTimeFactor = 1.0
        for factor in descriptor.factors:
            if factor.name == 'gun/reloadTime':
                reloadTimeFactor = factor.value
                break

        ammoCtrl.updatePenaltyReloadTime(reloadTimeFactor, currentPenaltyReloadTime)