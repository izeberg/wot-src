from constants import ARENA_GUI_TYPE
from gui.Scaleform.daapi.settings import config as sf_config
from gui.shared.system_factory import registerScaleformBattlePackages, registerScaleformLobbyPackages

def registerPortalBattlePackages():
    registerScaleformBattlePackages(ARENA_GUI_TYPE.PORTAL, sf_config.BATTLE_PACKAGES + ('portal.gui.Scaleform.daapi.view.battle', ))


def registerPortalLobbyPackages():
    registerScaleformLobbyPackages(['portal.gui.Scaleform.daapi.view.lobby'])