from gui.Scaleform.daapi.view.meta.WTCrosshairPanelContainerMeta import WTCrosshairPanelContainerMeta
from white_tiger.gui.Scaleform.daapi.view.battle.white_tiger.crosshair import plugins

class WhiteTigerCrosshairPanelContainer(WTCrosshairPanelContainerMeta):

    def __init__(self):
        super(WhiteTigerCrosshairPanelContainer, self).__init__()
        self.addPlugins(plugins.createPlugins())