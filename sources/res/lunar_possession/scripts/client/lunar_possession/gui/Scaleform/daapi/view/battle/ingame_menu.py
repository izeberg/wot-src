from lunar_possession.gui.Scaleform.daapi.view.battle.premature_leave import showLunarPossesionLeaverAliveWindow
from gui.Scaleform.daapi.view.battle.shared.ingame_menu import IngameMenu

class LunarPossessionIngameMenu(IngameMenu):

    @staticmethod
    def _showLeaverAliveWindow(isPlayerIGR):
        return showLunarPossesionLeaverAliveWindow()