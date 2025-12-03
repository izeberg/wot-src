import weakref, BigWorld, CGF, Math, math_utils, GenericComponents
from cgf_script.bonus_caps_rules import bonusCapsManager
from cgf_script.component_meta_class import ComponentProperty, CGFMetaTypes, registerComponent
from cgf_script.managers_registrator import onAddedQuery, onRemovedQuery, onProcessQuery
from grinch.cgf import getVehicleFromGO
from grinch_common.grinch_constants import ARENA_BONUS_TYPE_CAPS, CaptureStates
from grinch_common.cgf.presents import HomebaseComponent
from constants import IS_CLIENT, NULL_ENTITY_ID
from helpers import dependency
if IS_CLIENT:
    from skeletons.gui.battle_session import IBattleSessionProvider
    from gui.Scaleform.daapi.view.battle.shared.component_marker.markers import AreaMarker
    from gui.Scaleform.daapi.view.battle.shared.component_marker.markers_components import ComponentBitMask, MinimapMarkerComponent
    from grinch.gui.shared.events import TurretDeployEvent, RageAbilityEvent, AbilityEvent, HomebaseMarkerEvent, CapturablePointEvent
    from GrinchCapturablePointComponent import GrinchCapturablePointComponent
else:

    class AreaMarker(object):
        pass


    class MinimapMarkerComponent(object):
        pass


    class IBattleSessionProvider(object):
        pass


    class TurretDeployEvent(object):
        pass


    class RageAbilityEvent(object):
        pass


    class AbilityEvent(object):
        pass


    class HomebaseMarkerEvent(object):
        pass


    class GrinchCapturablePointComponent(object):
        pass


def getHomebaseMarkerTransform(team):
    spaceID = BigWorld.player().spaceID
    hierarchy = CGF.HierarchyManager(spaceID)
    query = CGF.Query(spaceID, (CGF.GameObject, HomebaseComponent))
    for homebaseGO, homebaseComp in query:
        if team == homebaseComp.team:
            for go, _ in hierarchy.findComponentsInHierarchy(homebaseGO, GrinchHomebaseMarker):
                tranformComponent = go.findComponentByType(GenericComponents.TransformComponent)
                if tranformComponent:
                    return tranformComponent.worldTransform

    return Math.Matrix()


class StaticMinimapMarkerComponent(MinimapMarkerComponent):

    def _setupMarker(self, gui, **kwargs):
        config = self._config
        gui.invoke(self._componentID, 'as_setIcon', config['icon'])


class DynamicMinimapMarkerComponent(MinimapMarkerComponent):

    def _setupMarker(self, gui, **kwargs):
        config = self._config
        gui.invoke(self._componentID, 'as_setIcon', config['icon'])


class StaticAreaMarker(AreaMarker):
    COMPONENT_CLASS = {2: StaticMinimapMarkerComponent}


class DynamicAreaMarker(AreaMarker):
    COMPONENT_CLASS = {2: DynamicMinimapMarkerComponent}


@registerComponent
class GrinchHomebaseMarker(object):
    category = 'Grinch'
    editorTitle = 'Grinch Homebase Marker'
    domain = CGF.DomainOption.DomainClient


@registerComponent
class GrinchDeployMarker(object):
    category = 'Grinch'
    domain = CGF.DomainOption.DomainClient
    source = ComponentProperty(type=CGFMetaTypes.STRING, value='', editorName='source')

    def __init__(self):
        super(GrinchDeployMarker, self).__init__()
        self.vehicleID = NULL_ENTITY_ID
        self.sourceComponent = None
        return


@registerComponent
class GrinchFlareMarker(object):
    category = 'Grinch'
    domain = CGF.DomainOption.DomainClient

    def __init__(self):
        super(GrinchFlareMarker, self).__init__()
        self.vehicleID = NULL_ENTITY_ID


@registerComponent
class GrinchDartStunMarker(object):
    category = 'Grinch'
    domain = CGF.DomainOption.DomainClient

    def __init__(self):
        super(GrinchDartStunMarker, self).__init__()
        self.vehicleID = NULL_ENTITY_ID


@registerComponent
class GrinchRageUndeadMarker(object):
    category = 'Grinch'
    editorTitle = 'Grinch Rage Undead Marker'
    domain = CGF.DomainOption.DomainClient

    def __init__(self):
        super(GrinchRageUndeadMarker, self).__init__()
        self.vehicleID = NULL_ENTITY_ID


@registerComponent
class GrinchMinimapMarker(object):
    category = 'Grinch'
    editorTitle = 'Grinch Minimap Marker'
    domain = CGF.DomainOption.DomainClient
    symbol = ComponentProperty(type=CGFMetaTypes.STRING, value='', editorName='Symbol')
    container = ComponentProperty(type=CGFMetaTypes.STRING, value='', editorName='Container')
    onlyTranslation = ComponentProperty(type=CGFMetaTypes.BOOL, value=False, editorName='Only Translation')
    offset = ComponentProperty(type=CGFMetaTypes.VECTOR3, value=Math.Vector3(0, 0, 0), editorName='offset')
    areaRadius = ComponentProperty(type=CGFMetaTypes.FLOAT, value=0.0, editorName='areaRadius')
    disappearanceRadius = ComponentProperty(type=CGFMetaTypes.FLOAT, value=1.0, editorName='Disappearance Radius')
    reverseDisappearing = ComponentProperty(type=CGFMetaTypes.BOOL, value=False, editorName='Reverse disappearing')
    type = ComponentProperty(type=CGFMetaTypes.STRING, value='static', editorName='MarkerType')

    def __init__(self):
        super(GrinchMinimapMarker, self).__init__()
        self.marker = None
        self.markerID = None
        return


@registerComponent
class GrinchCapturableMinimapMarker(GrinchMinimapMarker):
    editorTitle = 'Grinch Capturable Minimap Marker'

    def __init__(self):
        super(GrinchCapturableMinimapMarker, self).__init__()
        self.baseName = ''

    def onUpdated(self, event):
        if event.capturablePointName != self.baseName:
            return
        if event.captureState == CaptureStates.NEUTRAL:
            return
        newSymbol = ('team_{}_{}_base').format(event.ownersTeam, event.capturablePointName)
        markerComp = self.marker.getComponentByType(ComponentBitMask.MINIMAP_MARKER)[0]
        markerComp._config['icon'] = newSymbol
        gui = markerComp._gui()
        if gui:
            markerComp._setupMarker(gui)


@bonusCapsManager(ARENA_BONUS_TYPE_CAPS.GRINCH, CGF.DomainOption.DomainClient)
class GrinchHudHomebaseMarkerManager(CGF.ComponentManager):

    @onAddedQuery(CGF.GameObject, GrinchHomebaseMarker, GenericComponents.TransformComponent, tickGroup='postTickUpdate')
    def onAddedHomebaseMarker(self, go, _, transform):
        from gui.shared import g_eventBus, EVENT_BUS_SCOPE
        hierarchyManager = CGF.HierarchyManager(go.spaceID)
        if not hierarchyManager:
            return
        homebaseGO = hierarchyManager.getTopMostParent(go)
        homebase = homebaseGO.findComponentByType(HomebaseComponent)
        if not homebase:
            return
        g_eventBus.handleEvent(HomebaseMarkerEvent(HomebaseMarkerEvent.HOMEBASE_MARKER_UPDATE, team=homebase.team, matrix=transform.worldTransform), scope=EVENT_BUS_SCOPE.BATTLE)


@bonusCapsManager(ARENA_BONUS_TYPE_CAPS.GRINCH, CGF.DomainOption.DomainClient)
class GrinchHudCapturablePointManager(CGF.ComponentManager):

    @onAddedQuery(CGF.GameObject, GrinchCapturablePointComponent, GenericComponents.TransformComponent)
    def onAddedCapturablePointComponent(self, gameObject, capturablePoint, transform):
        from gui.shared import g_eventBus, EVENT_BUS_SCOPE
        g_eventBus.handleEvent(CapturablePointEvent(CapturablePointEvent.INIT_CAPTURABLE_POINT), EVENT_BUS_SCOPE.BATTLE)


@bonusCapsManager(ARENA_BONUS_TYPE_CAPS.GRINCH, CGF.DomainOption.DomainClient)
class GrinchHudMinimapManager(CGF.ComponentManager):
    __guiSessionProvider = dependency.descriptor(IBattleSessionProvider)

    @onAddedQuery(GrinchCapturableMinimapMarker, GrinchCapturablePointComponent, GenericComponents.TransformComponent)
    def onAddedCapturableMinimapMarker(self, marker, capturablePoint, transform):
        from gui.shared import g_eventBus, EVENT_BUS_SCOPE, EventPriority
        g_eventBus.addListener(CapturablePointEvent.CAPTURABLE_POINT_UPDATE, marker.onUpdated, EVENT_BUS_SCOPE.BATTLE, EventPriority.HIGH)
        marker.baseName = capturablePoint.capturablePointName
        self.addMinimapMarker(marker, transform)

    @onRemovedQuery(GrinchCapturableMinimapMarker)
    def onRemovedCapturableMinimapMarker(self, marker):
        from gui.shared import g_eventBus, EVENT_BUS_SCOPE
        g_eventBus.removeListener(CapturablePointEvent.CAPTURABLE_POINT_UPDATE, marker.onUpdated, EVENT_BUS_SCOPE.BATTLE)
        self.removeMinimapMarker(marker)

    @onAddedQuery(GrinchMinimapMarker, GenericComponents.TransformComponent)
    def onAddedMinimapMarker(self, marker, transform):
        self.addMinimapMarker(marker, transform)

    @onRemovedQuery(GrinchMinimapMarker)
    def onRemovedMinimapMarker(self, marker):
        self.removeMinimapMarker(marker)

    def addMinimapMarker(self, marker, transform):
        transform = transform.worldTransform
        matrixProduct = math_utils.MatrixProviders.product(transform, math_utils.createTranslationMatrix(marker.offset))
        data = {'visible': True, 
           'areaRadius': marker.areaRadius, 
           'disappearingRadius': marker.disappearanceRadius, 
           'reverseDisappearing': marker.reverseDisappearing, 
           ComponentBitMask.MINIMAP_MARKER: [
                                           {'symbol': 'DynamicEntry' if marker.type == 'dynamic' else 'StaticEntry', 
                                              'icon': marker.symbol, 
                                              'container': marker.container, 
                                              'onlyTranslation': marker.onlyTranslation}], 
           'matrixProduct': matrixProduct, 
           'bitMask': ComponentBitMask.MINIMAP_MARKER}
        marker.marker = DynamicAreaMarker(data) if marker.type == 'dynamic' else StaticAreaMarker(data)
        marker.markerID = self.__guiSessionProvider.shared.areaMarker.addMarker(marker.marker)

    def removeMinimapMarker(self, marker):
        areaMarkerCtrl = self.__guiSessionProvider.shared.areaMarker
        if areaMarkerCtrl:
            areaMarkerCtrl.removeMarker(marker.markerID)


@bonusCapsManager(ARENA_BONUS_TYPE_CAPS.GRINCH, CGF.DomainOption.DomainClient)
class GrinchHudDeployMarkerManager(CGF.ComponentManager):

    @onAddedQuery(CGF.GameObject, GrinchDeployMarker)
    def onAddedGrinchDeployMarker(self, go, marker):
        vehicle = getVehicleFromGO(self.spaceID, go)
        if vehicle and marker.source in vehicle.components:
            marker.vehicleID = vehicle.id
            marker.sourceComponent = weakref.proxy(vehicle.components.get(marker.source))

    @onRemovedQuery(GrinchDeployMarker)
    def onRemovedGrinchDeployMarker(self, marker):
        from gui.shared import g_eventBus, EVENT_BUS_SCOPE
        g_eventBus.handleEvent(TurretDeployEvent(TurretDeployEvent.TURRET_DEPLOY_TIME_CHANGED, deployTimeLeft=0, vehicleID=marker.vehicleID), scope=EVENT_BUS_SCOPE.BATTLE)

    @onProcessQuery(GrinchDeployMarker, updatePeriod=0.1)
    def onProcessGrinchDeployMarker(self, marker):
        from gui.shared import g_eventBus, EVENT_BUS_SCOPE
        if not marker.vehicleID:
            return
        timeLeft = marker.sourceComponent.endtime - BigWorld.serverTime()
        g_eventBus.handleEvent(TurretDeployEvent(TurretDeployEvent.TURRET_DEPLOY_TIME_CHANGED, deployTimeLeft=timeLeft, vehicleID=marker.vehicleID), scope=EVENT_BUS_SCOPE.BATTLE)


@bonusCapsManager(ARENA_BONUS_TYPE_CAPS.GRINCH, CGF.DomainOption.DomainClient)
class GrinchHudRageUndeadMarkerManager(CGF.ComponentManager):

    @onAddedQuery(CGF.GameObject, GrinchRageUndeadMarker)
    def onAddedGrinchRageUndeadMarker(self, go, undeadMarker):
        vehicle = getVehicleFromGO(self.spaceID, go)
        if vehicle:
            undeadMarker.vehicleID = vehicle.id
        from gui.shared import g_eventBus, EVENT_BUS_SCOPE
        g_eventBus.handleEvent(RageAbilityEvent(RageAbilityEvent.VEHICLE_STATUS_CHANGED, vehicleUndeadStatus=True, vehicleID=undeadMarker.vehicleID), scope=EVENT_BUS_SCOPE.BATTLE)

    @onRemovedQuery(GrinchRageUndeadMarker)
    def onRemovedGrinchDeployMarker(self, undeadMarker):
        from gui.shared import g_eventBus, EVENT_BUS_SCOPE
        g_eventBus.handleEvent(RageAbilityEvent(RageAbilityEvent.VEHICLE_STATUS_CHANGED, vehicleUndeadStatus=False, vehicleID=undeadMarker.vehicleID), scope=EVENT_BUS_SCOPE.BATTLE)


@bonusCapsManager(ARENA_BONUS_TYPE_CAPS.GRINCH, CGF.DomainOption.DomainClient)
class GrinchHudFlareMarkerManager(CGF.ComponentManager):

    @onAddedQuery(CGF.GameObject, GrinchFlareMarker)
    def onAddedGrinchFlareMarker(self, go, marker):
        vehicle = getVehicleFromGO(self.spaceID, go)
        if not vehicle or vehicle.isPlayerVehicle:
            return
        marker.vehicleID = vehicle.id
        from gui.shared import g_eventBus, EVENT_BUS_SCOPE
        g_eventBus.handleEvent(AbilityEvent(AbilityEvent.FLARE_MARK, vehicleID=marker.vehicleID, isOn=True), scope=EVENT_BUS_SCOPE.BATTLE)

    @onRemovedQuery(GrinchFlareMarker)
    def onRemovedGrinchFlareMarker(self, marker):
        if marker.vehicleID == NULL_ENTITY_ID:
            return
        from gui.shared import g_eventBus, EVENT_BUS_SCOPE
        g_eventBus.handleEvent(AbilityEvent(AbilityEvent.FLARE_MARK, vehicleID=marker.vehicleID, isOn=False), scope=EVENT_BUS_SCOPE.BATTLE)


@bonusCapsManager(ARENA_BONUS_TYPE_CAPS.GRINCH, CGF.DomainOption.DomainClient)
class GrinchHudDartStunMarkerManager(CGF.ComponentManager):

    @onAddedQuery(CGF.GameObject, GrinchDartStunMarker)
    def onAddedGrinchDartStunMarker(self, go, marker):
        vehicle = getVehicleFromGO(self.spaceID, go)
        if not vehicle or vehicle.isPlayerVehicle:
            return
        marker.vehicleID = vehicle.id
        from gui.shared import g_eventBus, EVENT_BUS_SCOPE
        g_eventBus.handleEvent(AbilityEvent(AbilityEvent.DART_STUN_MARK, vehicleID=marker.vehicleID, isOn=True), scope=EVENT_BUS_SCOPE.BATTLE)

    @onRemovedQuery(GrinchDartStunMarker)
    def onRemovedGrinchDartStunMarker(self, marker):
        if marker.vehicleID == NULL_ENTITY_ID:
            return
        from gui.shared import g_eventBus, EVENT_BUS_SCOPE
        g_eventBus.handleEvent(AbilityEvent(AbilityEvent.DART_STUN_MARK, vehicleID=marker.vehicleID, isOn=False), scope=EVENT_BUS_SCOPE.BATTLE)