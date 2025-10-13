import BigWorld, SoundGroups
from halloween.gui.sounds import SoundComponentBase, playSound
from halloween_common.halloween_constants import ATTACK_REASON
from halloween.gui.sounds.sound_constants import BossBattleSound, BOTS_ENGINE, BOTS_EXPLOSION, VehicleSoulsContainerSounds as SoulsSounds, LootSounds
from HWBuffBossAuraComponent import HWBuffBossAuraComponent

class HWBossBattleSounds(SoundComponentBase):
    _APPLIABLE_ATTACK_REASONS = (
     ATTACK_REASON.SHOT,
     ATTACK_REASON.HALLOWEEN_SHOT_AOE_DAMAGE,
     ATTACK_REASON.HALLOWEEN_SHOT_AOE_DRAIN_ENEMY_HP)
    _INVULNERABLE_ATTACK_REASONS = (
     ATTACK_REASON.SHOT,)

    def __init__(self, parent):
        super(HWBossBattleSounds, self).__init__(parent)
        self._arenaBonusType = BigWorld.player().arena.bonusType

    def onAvatarReady(self):
        if self._containsAuraComponent():
            self.parent.soundObject.play(BossBattleSound.AURA_ACTIVATION)

    def onBossDamageReceived(self, attackerID, attackReason, damage):
        if BigWorld.player().playerVehicleID != attackerID:
            return
        if damage > 0 and attackReason in self._APPLIABLE_ATTACK_REASONS:
            playSound(BossBattleSound.BOSS_HIT_MARKER)
        elif not self.arenaPhases.isBossVulnerable:
            if attackReason in self._INVULNERABLE_ATTACK_REASONS:
                playSound(BossBattleSound.BOSS_HIT_MARKER_INVULNERABILITY)

    def _containsAuraComponent(self):
        return HWBuffBossAuraComponent in set([ type(value) for value in self.parent.entity.dynamicComponents.values() ])


class HWCommonEnemySounds(SoundComponentBase):

    def onAvatarReady(self):
        engineEvent = BOTS_ENGINE.get(self.parent.entity.typeDescriptor.name)
        if engineEvent is not None:
            self.parent.soundObject.play(engineEvent)
        return

    def onVehicleKilled(self, victimID, *_):
        if self.parent.entity.id == victimID:
            destroyEvent = BOTS_EXPLOSION.get(self.parent.entity.typeDescriptor.name)
            if destroyEvent is not None:
                SoundGroups.g_instance.playSoundPos(destroyEvent, self.parent.entity.position)
        return


class HWSoulsContainerSounds(SoundComponentBase):

    def __init__(self, parent):
        super(HWSoulsContainerSounds, self).__init__(parent)
        self._souls = 0

    def onAvatarReady(self):
        vehicleSoulsContainer = self.parent.hwSoulsContainer
        if not vehicleSoulsContainer:
            return
        vehicleSoulsContainer.onChangeSoulsCount += self._onVehicleSoulsChanged
        self._souls = vehicleSoulsContainer.souls

    def onDestroy(self):
        vehicleSoulsContainer = self.parent.hwSoulsContainer
        if vehicleSoulsContainer is not None:
            vehicleSoulsContainer.onChangeSoulsCount -= self._onVehicleSoulsChanged
        return

    def _onVehicleSoulsChanged(self, souls, reason):
        sound = SoulsSounds.Player if self.parent.entity.isPlayerVehicle else SoulsSounds.Ally
        if souls == 0:
            self.parent.soundObject.play(sound.OFF)
        elif self._souls == 0:
            self.parent.soundObject.play(sound.ON)
        self._souls = souls


class HWLootSounds(SoundComponentBase):

    def onLootSucceed(self, lootID, vehicleIDs):
        player = BigWorld.player()
        if player is None:
            return
        else:
            if player.playerVehicleID == self.parent.entity.id:
                playSound(LootSounds.Player.PICKUP_SUCCEED.get(lootID))
            elif not vehicleIDs or player.playerVehicleID in vehicleIDs:
                self.parent.soundObject.play(LootSounds.Ally.PICKUP_SUCCEED)
            return