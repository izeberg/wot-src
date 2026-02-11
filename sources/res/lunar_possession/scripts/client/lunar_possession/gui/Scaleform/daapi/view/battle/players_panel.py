from lunar_possession.gui.Scaleform.daapi.view.meta.LunarPlayersPanelMeta import LunarPlayersPanelMeta
from lunar_possession.gui.battle_control.controllers.lunar_possession_battle_ctrl import ILunarPossessionListener

class LunarPlayersPanel(LunarPlayersPanelMeta, ILunarPossessionListener):

    def _populate(self):
        super(LunarPlayersPanel, self)._populate()
        self.setInitialMode()

    def updateSpiritPossession(self, vehicleId, isEnemy, hasSpirit):
        self.as_setLunarIndicatorVisibilityS(vehicleId, isEnemy, hasSpirit)