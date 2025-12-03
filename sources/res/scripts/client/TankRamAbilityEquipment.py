from AbilityEquipment import AbilityEquipment
from PlayerEvents import g_playerEvents

class TankRamAbilityEquipment(AbilityEquipment):

    def showCollisionEffectWithOtherVehicle(self, selfPtForEffects, isAlly):
        g_playerEvents.onCollisionWithOtherAliveVehicle(selfPtForEffects, isAlly)