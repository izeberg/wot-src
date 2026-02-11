from gui.Scaleform.daapi.view.battle.shared.markers2d import MarkersManager
from lunar_possession.gui.Scaleform.daapi.view.battle.markers2d.vehicle_plugins import LunarVehicleMarkerPlugin

class LunarPossessionMarkersManager(MarkersManager):
    MARKERS_MANAGER_SWF = 'lunar_possession|lunarBattleVehicleMarkersApp.swf'

    def _setupPlugins(self, arenaVisitor):
        setup = super(LunarPossessionMarkersManager, self)._setupPlugins(arenaVisitor)
        setup['vehicles'] = LunarVehicleMarkerPlugin
        return setup