import Event, BigWorld, CGF, logging
from portal_common.portal_constants import PORTAL_GAME_PARAMS_KEY
from portal_constants import PORTAL_FRONTIER_MARKERS
from TeleportReplicableComponent import TeleportReplicableComponent
from script_component.DynamicScriptComponent import DynamicScriptComponent
from portal_common_cgf.portal_2d_markers.components import PortalReplicableMarkerStatesComponent as replicableMarkerStatesComponentBase
from portal_client_cgf.portal_2d_markers.components import PortalAreaMarker
_logger = logging.getLogger(__name__)

class PortalReplicableMarkerStatesComponent(DynamicScriptComponent, replicableMarkerStatesComponentBase):

    def __init__(self, *args, **kwargs):
        super(PortalReplicableMarkerStatesComponent, self).__init__(*args, **kwargs)
        self.__eventManager = Event.EventManager()
        self.onMarkerStateChanged = Event.SafeEvent(self.__eventManager)
        self.onMarkerProgressChanged = Event.SafeEvent(self.__eventManager)
        self.onMarkersInitialized = Event.SafeEvent(self.__eventManager)
        self.activeMarkerComponent = None
        return

    def onDestroy(self):
        self.__eventManager.clear()
        self.__eventManager = None
        TeleportReplicableComponent.onTeleportLinked -= self.__onTeleportLinked
        super(PortalReplicableMarkerStatesComponent, self).onDestroy()
        return

    @property
    def gameObject(self):
        return self.entity.entityGameObject

    def set_markerID(self, prev):
        self.onMarkerStateChanged(self.gameObject, self.markerID)

    def set_maxProgress(self, prev):
        self.onMarkerProgressChanged(self.gameObject, self.currentProgress, self.maxProgress)

    def set_currentProgress(self, prev):
        self.onMarkerProgressChanged(self.gameObject, self.currentProgress, self.maxProgress)

    def initTeleportTunnelMarkers(self, teleportGO, linkedTeleportGO):
        teleportName = teleportGO.name
        linkedTeleportName = linkedTeleportGO.name
        hm = CGF.HierarchyManager(self.spaceID)
        markerGOQuery = hm.findComponentsInHierarchy(teleportGO, PortalAreaMarker)
        markerComponents = [ markerComp for _, markerComp in markerGOQuery ]
        campName = self.getCampNameByTeleport(teleportName) or self.getCampNameByTeleport(linkedTeleportName)
        if not campName:
            _logger.error('There is no camp for teleports %s | %s', teleportName, linkedTeleportName)
            return
        frontierName = self.__getFrontierNameByCamp(campName)
        if not frontierName:
            _logger.error('There is no campFrontier in config! %s', campName)
            return
        frontierMarkers = getattr(PORTAL_FRONTIER_MARKERS, frontierName.upper())
        teleportMarkers = frontierMarkers['teleport']
        for markerComponent in markerComponents:
            markerComponent.marker2DEntryID = teleportMarkers['markers2d'][markerComponent.stateID]
            markerComponent.markerMinimapEntryID = teleportMarkers['markersMinimap'][markerComponent.stateID]

        self.onMarkersInitialized(teleportGO)

    def initCampMarkers(self, campGO, markerComponents):
        campName = campGO.name
        frontierName = self.__getFrontierNameByCamp(campName)
        if not frontierName:
            _logger.error('There is no campFrontier in config! %s', campName)
            return
        frontierMarkers = getattr(PORTAL_FRONTIER_MARKERS, frontierName.upper())
        campMarkers = frontierMarkers['camp']
        for markerComponent in markerComponents:
            markerComponent.marker2DEntryID = campMarkers['markers2d'][markerComponent.stateID]
            markerComponent.markerMinimapEntryID = campMarkers['markersMinimap'][markerComponent.stateID]

        self.onMarkersInitialized(campGO)

    def _onAvatarReady(self):
        TeleportReplicableComponent.onTeleportLinked += self.__onTeleportLinked

    def getCampNameByTeleport(self, teleportName):
        player = BigWorld.player()
        portalConfig = player.lobbyContext.getServerSettings().getSettings()[PORTAL_GAME_PARAMS_KEY]
        campTeleports = portalConfig['scenario']['teleportSettings']['campTeleports']
        return campTeleports.get(teleportName)

    def __onTeleportLinked(self, teleportGO):
        sourceComponent = teleportGO.findComponentByType(TeleportReplicableComponent)
        index = sourceComponent.index
        teleports = CGF.Query(self.spaceID, (CGF.GameObject, TeleportReplicableComponent)).values()
        linkedTeleports = [ teleportGO for teleportGO, component in teleports if component.index == index ]
        if len(linkedTeleports) != 2:
            return
        sourceTeleport = linkedTeleports[0]
        destinationTeleport = linkedTeleports[1]
        self.initTeleportTunnelMarkers(sourceTeleport, destinationTeleport)
        linkedMarkersComponent = destinationTeleport.findComponentByType(PortalReplicableMarkerStatesComponent)
        linkedMarkersComponent.initTeleportTunnelMarkers(destinationTeleport, sourceTeleport)

    def __getFrontierNameByCamp(self, campName):
        player = BigWorld.player()
        portalConfig = player.lobbyContext.getServerSettings().getSettings()[PORTAL_GAME_PARAMS_KEY]
        frontierInfos = portalConfig['scenario']['campsSettings']['frontiers']
        campFrontier = None
        for frontier, frontierInfo in frontierInfos.iteritems():
            if campName in frontierInfo['camps']:
                campFrontier = frontier

        return campFrontier