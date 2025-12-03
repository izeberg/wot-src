import typing
from gui.battle_control.battle_constants import BATTLE_CTRL_ID
from gui.battle_control.controllers.sound_ctrls.common import ShotsResultSoundController
from constants import VEHICLE_HIT_FLAGS as VHF
if typing.TYPE_CHECKING:
    from typing import Optional

class GrinchSoundBattleController(ShotsResultSoundController):

    def getControllerID(self):
        return BATTLE_CTRL_ID.SHOTS_RESULT_SOUND

    def getVehicleHitResultSound(self, enemyVehID, hitFlags, enemiesHitCount):
        sound = super(GrinchSoundBattleController, self).getVehicleHitResultSound(enemyVehID, hitFlags, enemiesHitCount)
        if hitFlags & (VHF.CHASSIS_DAMAGED_BY_PROJECTILE | VHF.CHASSIS_DAMAGED_BY_EXPLOSION):
            sound = None
        return sound