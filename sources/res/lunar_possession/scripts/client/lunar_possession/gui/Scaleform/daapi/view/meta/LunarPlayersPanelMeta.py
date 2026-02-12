from gui.Scaleform.daapi.view.battle.classic.players_panel import PlayersPanel

class LunarPlayersPanelMeta(PlayersPanel):

    def as_setLunarIndicatorVisibilityS(self, vehicleID, isEnemy, isVisible):
        if self._isDAAPIInited():
            return self.flashObject.as_setLunarIndicatorVisibility(vehicleID, isEnemy, isVisible)