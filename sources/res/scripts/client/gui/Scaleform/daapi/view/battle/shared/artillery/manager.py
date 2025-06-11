from gui.Scaleform.daapi.view.battle.shared.artillery.plugins import ArtilleryTimeZonePlugin
from gui.Scaleform.daapi.view.battle.shared.markers2d import MarkersManager

class ArtilleryMarkersManager(MarkersManager):

    def _setupPlugins(self, arenaVisitor):
        setup = super(ArtilleryMarkersManager, self)._setupPlugins(arenaVisitor)
        setup['step_repairs'] = ArtilleryTimeZonePlugin
        return setup