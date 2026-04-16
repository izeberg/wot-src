from gui.Scaleform.daapi.view.battle.shared.crosshair import CrosshairPanelContainer
from historical_battles.gui.Scaleform.daapi.view.battle.crosshair.plugins import createPlugins

class HBCrosshairPanelContainer(CrosshairPanelContainer):

    def _getPlugins(self):
        plugins = super(HBCrosshairPanelContainer, self)._getPlugins()
        plugins.update(createPlugins())
        return plugins