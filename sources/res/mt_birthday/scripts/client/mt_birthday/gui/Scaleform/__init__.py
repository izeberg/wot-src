from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.shared.system_factory import registerLobbyTooltipsBuilders, registerScaleformLobbyPackages

def registerBirthdayScaleform():
    registerScaleformLobbyPackages(('mt_birthday.gui.Scaleform.daapi.view.lobby', ))


def registerGiftSystemTooltipsBuilders():
    registerLobbyTooltipsBuilders([
     (
      'mt_birthday.gui.Scaleform.daapi.view.tooltips.lobby_builders',
      TOOLTIPS_CONSTANTS.BIRTHDAY_SET)])