from __future__ import absolute_import
from gui.Scaleform.daapi.view.battle.shared.crosshair.container import CrosshairPanelContainer
from last_stand.gui.scaleform.daapi.view.battle.shared.crosshair import plugins

class LSCrosshairPanelContainer(CrosshairPanelContainer):

    def _getPlugins(self):
        res = super(LSCrosshairPanelContainer, self)._getPlugins()
        res['vehicleState'] = plugins.LSVehicleStatePlugin
        return res