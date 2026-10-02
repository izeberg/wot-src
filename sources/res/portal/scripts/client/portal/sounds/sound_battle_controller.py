import BattleReplay, typing, WWISE
from gui.battle_control.controllers.sound_ctrls.common import SoundPlayersBattleController
from portal.sounds.sound_players import PortalGameFlowStateSoundPlayer, PortalVehicleStateSoundPlayer
if typing.TYPE_CHECKING:
    from gui.battle_control.controllers import BattleSessionSetup
    from gui.battle_control.controllers.sound_ctrls.common import SoundPlayer

class PortalBattleSoundCtrl(SoundPlayersBattleController):

    def __init__(self, setup):
        super(PortalBattleSoundCtrl, self).__init__()

    def startControl(self, *args):
        WWISE.activateRemapping('portal25')
        super(PortalBattleSoundCtrl, self).startControl()

    def stopControl(self):
        WWISE.deactivateRemapping('portal25')
        super(PortalBattleSoundCtrl, self).stopControl()

    def _initializeSoundPlayers(self):
        return (
         PortalGameFlowStateSoundPlayer(),
         PortalVehicleStateSoundPlayer())


class ReplayPortalBattleSoundCtrl(PortalBattleSoundCtrl):
    pass


def createPortalBattleSoundsController(setup):
    if BattleReplay.g_replayCtrl.isPlaying:
        return ReplayPortalBattleSoundCtrl(setup)
    return PortalBattleSoundCtrl(setup)