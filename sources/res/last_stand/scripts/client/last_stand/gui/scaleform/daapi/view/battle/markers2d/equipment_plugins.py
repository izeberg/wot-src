from __future__ import absolute_import
from gui.Scaleform.daapi.view.battle.shared.markers2d.plugins import EquipmentsMarkerPlugin
from gui.Scaleform.daapi.view.battle.shared.markers2d import settings

class LSEquipmentsMarkerPlugin(EquipmentsMarkerPlugin):
    LS_EQUIPMENT_MARKER_LINKAGE = 'LSFortConsumablesMarkerUI'
    LS_MARKERS = ('LSEventDeathZoneUI', )

    def _getMarkerLinkage(self, item):
        if item.getMarker() in self.LS_MARKERS:
            return self.LS_EQUIPMENT_MARKER_LINKAGE
        return settings.MARKER_SYMBOL_NAME.EQUIPMENT_MARKER