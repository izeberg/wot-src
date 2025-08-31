from comp7_light.gui.Scaleform.daapi.view.battle.shared.premature_leave import showComp7LightLeaverAliveWindow
from gui.Scaleform.daapi.view.battle.shared.ingame_menu import IngameMenu

class Comp7LightIngameMenu(IngameMenu):

    @staticmethod
    def _showLeaverAliveWindow(isPlayerIGR):
        return showComp7LightLeaverAliveWindow()