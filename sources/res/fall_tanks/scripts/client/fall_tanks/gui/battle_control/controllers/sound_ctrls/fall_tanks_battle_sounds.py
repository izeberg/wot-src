from __future__ import absolute_import
import typing, BattleReplay
from gui.battle_control.controllers.sound_ctrls.common import SoundPlayersBattleController
from fun_random.gui.battle_control.controllers.sound_ctrls.fun_random_battle_sounds import FunRandomBattleSoundController, FunRandomBattleReplaySoundController
from fall_tanks.gui.battle_control.controllers.sound_ctrls.race_music_sound_player import RaceMusicSoundPlayer
from fall_tanks.gui.battle_control.controllers.sound_ctrls.vehicle_frags_sound_player import VehicleFragsSoundPlayer
if typing.TYPE_CHECKING:
    from gui.battle_control.controllers import BattleSessionSetup
    from gui.battle_control.controllers.sound_ctrls.common import SoundPlayer

class FallTanksBattleSoundController(FunRandomBattleSoundController):

    def _initializeSoundPlayers(self):
        return (
         RaceMusicSoundPlayer(), VehicleFragsSoundPlayer())


class FallTanksBattleReplaySoundController(FunRandomBattleReplaySoundController):

    def _initializeSoundPlayers(self):
        return (
         RaceMusicSoundPlayer(), VehicleFragsSoundPlayer())


def createFallTanksBattleSoundsController(setup):
    if BattleReplay.g_replayCtrl.isPlaying:
        return FallTanksBattleReplaySoundController(setup)
    return FallTanksBattleSoundController(setup)