from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.shared.system_factory import registerScaleformLobbyPackages, registerLobbyTooltipsBuilders

def registerNewYearScaleform():
    registerScaleformLobbyPackages(('new_year.gui.Scaleform.daapi.view.lobby', ))
    registerLobbyTooltipsBuilders([
     (
      'new_year.gui.Scaleform.daapi.view.tooltips.lobby_builders',
      TOOLTIPS_CONSTANTS.NEW_YEAR_LOBBY_SET)])