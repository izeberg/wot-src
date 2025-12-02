import typing
from gui.impl import backport
from gui.impl.gen import R
from gui.Scaleform.daapi.view.battle.shared.postmortem_panel import PostmortemPanel
if typing.TYPE_CHECKING:
    from gui.battle_control.arena_info import arena_vos

class GrinchPostmortemPanel(PostmortemPanel):

    def _setDeadReasonInfo(self, vInfoVO, reason, showVehicle, vehLvl, vehImg, vehClass, vehName, killerUserVO):
        if vInfoVO is not None:
            if vInfoVO.player.isBot:
                classTag = vInfoVO.vehicleType.classTag
                if classTag == 'AT-SPG' or classTag == 'SPG':
                    vehClass = backport.image(R.images.grinch.gui.maps.icons.vehicleTypes.white.dyn(classTag.replace('-', '_'))())
        super(GrinchPostmortemPanel, self)._setDeadReasonInfo(vInfoVO, reason, showVehicle, vehLvl, vehImg, vehClass, vehName, killerUserVO)
        return

    def _prepareMessage(self, code, killerVehID, device=None):
        if code == 'DEATH_FROM_SHOT':
            arenaDP = self.sessionProvider.getArenaDP()
            if arenaDP.isVehiclePresented(killerVehID):
                vehInfo = arenaDP.getVehicleInfo(killerVehID)
                if vehInfo.player.isBot:
                    classTag = vehInfo.vehicleType.classTag
                    if classTag == 'AT-SPG':
                        code = 'DEATH_FROM_BIG_TURRET'
                    elif classTag == 'SPG':
                        code = 'DEATH_FROM_TURRET'
        super(GrinchPostmortemPanel, self)._prepareMessage(code, killerVehID, device)