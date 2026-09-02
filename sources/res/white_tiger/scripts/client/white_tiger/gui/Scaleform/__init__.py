from gui.shared.system_factory import registerLobbyTooltipsBuilders
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as _TOOLTIPS

def registerWhiteTigerTooltipsBuilders():
    registerLobbyTooltipsBuilders([
     (
      'white_tiger.gui.Scaleform.daapi.view.tooltips.wt_lobby_builders', _TOOLTIPS.WT_BATTLES_SET)])