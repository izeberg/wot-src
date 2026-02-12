import typing
from gui.Scaleform.daapi.view.battle.shared.markers2d.markers import VehicleMarker
from gui.Scaleform.daapi.view.battle.shared.markers2d.settings import CommonMarkerType
from gui.Scaleform.daapi.view.battle.shared.markers2d.vehicle_plugins import RespawnableVehicleMarkerPlugin
from gui.shared import g_eventBus, EVENT_BUS_SCOPE
from lunar_possession.gui.shared.events import BuffEvents
from lunar_possession_common.component_helpers import isSpiritCarrier
if typing.TYPE_CHECKING:
    from Vehicle import Vehicle
    from gui.prb_control.items.unit_items import VehicleInfo
    from gui.battle_control.battle_constants import PLAYER_GUI_PROPS
VEHICLE_MARKER = 'LunarVehicleMarker'
LUNAR_INDICATOR = 'showLunarIndicator'

class LunarVehicleMarkerPlugin(RespawnableVehicleMarkerPlugin):

    def start(self):
        super(LunarVehicleMarkerPlugin, self).start()
        g_eventBus.addListener(BuffEvents.VEHICLE_GET_BUFF, self.__updateIndicator, EVENT_BUS_SCOPE.BATTLE)
        g_eventBus.addListener(BuffEvents.VEHICLE_LOSE_BUFF, self.__updateIndicator, EVENT_BUS_SCOPE.BATTLE)
        ctrl = self.sessionProvider.shared.feedback
        if ctrl is not None:
            ctrl.onVehicleMarkerAdded += self.__checkForSpiritCarrier
        return

    def stop(self):
        g_eventBus.removeListener(BuffEvents.VEHICLE_GET_BUFF, self.__updateIndicator, EVENT_BUS_SCOPE.BATTLE)
        g_eventBus.removeListener(BuffEvents.VEHICLE_LOSE_BUFF, self.__updateIndicator, EVENT_BUS_SCOPE.BATTLE)
        ctrl = self.sessionProvider.shared.feedback
        if ctrl is not None:
            ctrl.onVehicleMarkerAdded -= self.__checkForSpiritCarrier
        super(LunarVehicleMarkerPlugin, self).stop()
        return

    def _getMarkerSymbol(self, vehicleID):
        return VEHICLE_MARKER

    def _getMarker2dType(self):
        return CommonMarkerType.VEHICLE

    def _restoreMarker(self, marker, vProxy, vInfo, guiProps):
        super(LunarVehicleMarkerPlugin, self)._restoreMarker(marker, vProxy, vInfo, guiProps)
        if not marker.isAlive():
            self._updateMarkerState(marker.getMarkerID(), 'dead', True, '')
            self._setMarkerBoundEnabled(marker.getMarkerID(), False)
        else:
            self._setMarkerBoundEnabled(marker.getMarkerID(), True)

    def __updateIndicator(self, event):
        marker = self._markers.get(event.vehicleID, None)
        if marker is not None and marker.isActive():
            self._invokeMarker(marker.getMarkerID(), LUNAR_INDICATOR, event.eventType == BuffEvents.VEHICLE_GET_BUFF)
        return

    def __checkForSpiritCarrier(self, vProxy, vInfo, guiProps):
        vehicleID = vInfo.vehicleID
        if vehicleID is None:
            return
        else:
            marker = self._markers.get(vehicleID, None)
            if marker is not None and marker.isActive():
                self._invokeMarker(marker.getMarkerID(), LUNAR_INDICATOR, isSpiritCarrier(vehicleID))
            return