from gui.battle_control import avatar_getter
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
from portal_common.portal_constants import PortalBossesID

def getBossVehicleName():
    sessionProvider = dependency.instance(IBattleSessionProvider)
    arenaDP = sessionProvider.getArenaDP()
    if arenaDP is None:
        return ''
    else:
        battleState = avatar_getter.getArenaInfo().portalBattleStateComponent
        boss = battleState.bossInfo[PortalBossesID.BOSS_ID]
        vInfo = arenaDP.getVehicleInfo(boss.vehicleID)
        if vInfo:
            return vInfo.vehicleType.shortName
        return ''