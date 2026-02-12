import logging, typing, BigWorld, CGF, GenericComponents, Math, math_utils
from LunarSpiritBuffComponent import LunarSpiritBuffComponent
from cgf_script.bonus_caps_rules import bonusCapsManager
from cgf_script.component_meta_class import ComponentProperty, CGFMetaTypes
from cgf_script.component_meta_class import registerComponent
from cgf_script.managers_registrator import onAddedQuery, onRemovedQuery, autoregister
from constants import IS_CGF_DUMP, IS_EDITOR
from debug_utils import LOG_WARNING
from gui.shared import g_eventBus, EVENT_BUS_SCOPE
from helpers import dependency
from lunar_possession.gui.shared.events import BuffEvents, PointZoneAnimationEvents
from lunar_possession_common.cgf.general_components import TeamIDComponent
from lunar_constants import ARENA_BONUS_TYPE_CAPS
_logger = logging.getLogger(__name__)
if IS_EDITOR or IS_CGF_DUMP:

    class AreaMarker(object):
        pass


    class MinimapMarkerComponent(object):
        pass


    class Vehicle(object):
        pass


    class IBattleSessionProvider(object):
        pass


    class VehicleViewState(object):
        SPIRIT_INDICATOR = 0


    class DestroyTimerViewState(object):
        pass


    class TIMER_VIEW_STATE(object):
        pass


    POINT_ZONE_ALLY_ICON = 0
    POINT_ZONE_OPPONENT_ICON = 0
else:
    from gui.battle_control import avatar_getter
    from skeletons.gui.battle_session import IBattleSessionProvider
    from gui.Scaleform.daapi.view.battle.shared.component_marker.markers import AreaMarker
    from gui.Scaleform.daapi.view.battle.shared.component_marker.markers_components import ComponentBitMask, MinimapMarkerComponent
    from Vehicle import Vehicle
    from lunar_possession.gui.battle_control.lunar_battle_constants import VehicleViewState
    from lunar_possession.gui.lunar_possession_gui_constants import POINT_ZONE_ALLY_ICON, POINT_ZONE_OPPONENT_ICON, BATTLE_CTRL_ID
    from gui.battle_control.battle_constants import DestroyTimerViewState, TIMER_VIEW_STATE
if typing.TYPE_CHECKING:
    if IS_EDITOR or IS_CGF_DUMP:

        class Avatar(object):
            pass


    else:
        from typing import Optional, Callable
        from Avatar import Avatar

@registerComponent
class LunarMinimapMarker(object):
    category = 'Lunar'
    editorTitle = 'Lunar Minimap Marker'
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
        super(LunarMinimapMarker, self).__init__()
        self.marker = None
        self.markerID = None
        return


@registerComponent
class _LunarZoneMinimapMarker(LunarMinimapMarker):

    def __init__(self, symbol, container):
        super(_LunarZoneMinimapMarker, self).__init__()
        self.symbol = symbol
        self.container = container


class StaticMinimapMarkerComponent(MinimapMarkerComponent):

    def _setupMarker(self, gui, **kwargs):
        super(StaticMinimapMarkerComponent, self)._setupMarker(gui)

    def setPointZoneState(self, state):
        gui = self._gui()
        if gui is not None and self._isMarkerExists:
            gui.invoke(self._componentID, 'setPointZoneState', state)
        return


class StaticAreaMarker(AreaMarker):
    COMPONENT_CLASS = {2: StaticMinimapMarkerComponent}

    def setPointZoneState(self, state):
        for component in self._components.itervalues():
            if hasattr(component, 'setPointZoneState'):
                component.setPointZoneState(state)
                return


@autoregister(presentInAllWorlds=True, domain=CGF.DomainOption.DomainClient)
class LunarHudMinimapManager(CGF.ComponentManager):
    __guiSessionProvider = dependency.descriptor(IBattleSessionProvider)
    __pointZoneMarkers = {}

    def activate(self):
        g_eventBus.addListener(PointZoneAnimationEvents.VEHICLE_DELIVERED_SPIRIT, self.__deliveredZoneMarker, EVENT_BUS_SCOPE.BATTLE)
        g_eventBus.addListener(PointZoneAnimationEvents.VEHICLE_DESTROYED_WITH_SPIRIT, self.__destroyedZoneMarker, EVENT_BUS_SCOPE.BATTLE)

    def destroy(self):
        g_eventBus.removeListener(PointZoneAnimationEvents.VEHICLE_DELIVERED_SPIRIT, self.__deliveredZoneMarker, EVENT_BUS_SCOPE.BATTLE)
        g_eventBus.removeListener(PointZoneAnimationEvents.VEHICLE_DESTROYED_WITH_SPIRIT, self.__destroyedZoneMarker, EVENT_BUS_SCOPE.BATTLE)

    @onAddedQuery(LunarMinimapMarker, GenericComponents.TransformComponent)
    def onAddedMinimapMarker(self, marker, transform):
        self.addMinimapMarker(marker, transform)

    @onRemovedQuery(LunarMinimapMarker)
    def onRemovedMinimapMarker(self, marker):
        self.removeMinimapMarker(marker)

    @onAddedQuery(_LunarZoneMinimapMarker, GenericComponents.TransformComponent)
    def onAddedZoneMinimapMarker(self, marker, transform):
        self.addMinimapMarker(marker, transform)

    @onRemovedQuery(_LunarZoneMinimapMarker)
    def onRemoveZonedMinimapMarker(self, marker):
        self.removeMinimapMarker(marker)

    @onAddedQuery(TeamIDComponent, CGF.GameObject)
    def onPointZoneAdded(self, teamIDComponent, go):
        player = BigWorld.player()
        symbol = POINT_ZONE_ALLY_ICON if player.followTeamID == teamIDComponent.teamID else POINT_ZONE_OPPONENT_ICON
        pointZoneMarker = go.createComponent(_LunarZoneMinimapMarker, symbol, 'flags')
        self.__pointZoneMarkers[teamIDComponent.teamID] = pointZoneMarker

    def addMinimapMarker(self, marker, transform):
        transform = transform.worldTransform
        matrixProduct = math_utils.MatrixProviders.product(transform, math_utils.createTranslationMatrix(marker.offset))
        data = {'visible': True, 
           'areaRadius': marker.areaRadius, 
           'disappearingRadius': marker.disappearanceRadius, 
           'reverseDisappearing': marker.reverseDisappearing, 
           ComponentBitMask.MINIMAP_MARKER: [
                                           {'symbol': marker.symbol, 
                                              'icon': marker.symbol, 
                                              'container': marker.container, 
                                              'onlyTranslation': marker.onlyTranslation}], 
           'matrixProduct': matrixProduct, 
           'bitMask': ComponentBitMask.MINIMAP_MARKER}
        marker.marker = StaticAreaMarker(data)
        marker.markerID = self.__guiSessionProvider.shared.areaMarker.addMarker(marker.marker)

    def removeMinimapMarker(self, marker):
        areaMarkerCtrl = self.__guiSessionProvider.shared.areaMarker
        if areaMarkerCtrl:
            areaMarkerCtrl.removeMarker(marker.markerID)

    @onAddedQuery(CGF.GameObject, LunarSpiritBuffComponent)
    def onVehicleGetsSpiritBuff(self, go, buffComponent):
        self.__vehicleBuffEvent(go, buffComponent, BuffEvents.VEHICLE_GET_BUFF)
        vehicle = go.findComponentByType(Vehicle) if go.isValid() else None
        if vehicle is None:
            LOG_WARNING('[Lunar] onVehicleGetsSpiritBuff - Could not find the vehicle')
            return
        else:
            self.__updateSpiritCarrierPointZoneState(vehicle.id, 'pulse')
            return

    @onRemovedQuery(CGF.GameObject, LunarSpiritBuffComponent)
    def onVehicleLosesSpiritBuff(self, go, buffComponent):
        self.__vehicleBuffEvent(go, buffComponent, BuffEvents.VEHICLE_LOSE_BUFF)

    def __vehicleBuffEvent(self, go, buffComponent, buffEventType):
        vehicle = go.findComponentByType(Vehicle) if go.isValid() else None
        if vehicle is None:
            LOG_WARNING('[Lunar] __vehicleBuffEvent - Could not find the vehicle')
            return
        else:
            g_eventBus.handleEvent(BuffEvents(buffEventType, vehicleID=vehicle.id), scope=EVENT_BUS_SCOPE.BATTLE)
            return

    def __deliveredZoneMarker(self, event):
        self.__updatePointZoneState(event.vehicleID, event.animationType)

    def __destroyedZoneMarker(self, event):
        self.__updateSpiritCarrierPointZoneState(event.vehicleID, event.animationType)

    def __updateSpiritCarrierPointZoneState(self, vehicleID, zoneState):
        arena = avatar_getter.getArena()
        if not arena:
            return
        else:
            vehicleInfo = arena.vehicles.get(vehicleID)
            if not vehicleInfo:
                return
            teamID = vehicleInfo.get('team')
            if teamID is not None:
                self.__setTeamPointZoneState(teamID, zoneState)
            return

    def __updatePointZoneState(self, vehicleID, zoneState):
        arena = avatar_getter.getArena()
        if not arena:
            return
        else:
            vehicleInfo = arena.vehicles.get(vehicleID)
            if not vehicleInfo:
                return
            teamID = vehicleInfo.get('team')
            if teamID is not None:
                self.__setTeamPointZoneState(teamID, zoneState)
            return

    def __setTeamPointZoneState(self, teamID, zoneState):
        pointZoneMarker = self.__pointZoneMarkers.get(teamID, None)
        if pointZoneMarker is not None and pointZoneMarker.marker is not None:
            pointZoneMarker.marker.setPointZoneState(zoneState)
        return


@registerComponent
class LunarPickupMarker(object):
    category = 'Lunar'
    editorTitle = 'Lunar Pickup Marker'
    domain = CGF.DomainOption.DomainClient
    symbol = ComponentProperty(type=CGFMetaTypes.STRING, value='EnemyTeamBaseEntry', editorName='Symbol')
    container = ComponentProperty(type=CGFMetaTypes.STRING, value='', editorName='Container')
    onlyTranslation = ComponentProperty(type=CGFMetaTypes.BOOL, value=False, editorName='Only Translation')
    offset = ComponentProperty(type=CGFMetaTypes.VECTOR3, value=Math.Vector3(0, 0, 0), editorName='offset')
    areaRadius = ComponentProperty(type=CGFMetaTypes.FLOAT, value=0.0, editorName='areaRadius')
    disappearanceRadius = ComponentProperty(type=CGFMetaTypes.FLOAT, value=1.0, editorName='Disappearance Radius')
    reverseDisappearing = ComponentProperty(type=CGFMetaTypes.BOOL, value=False, editorName='Reverse disappearing')

    def __init__(self):
        super(LunarPickupMarker, self).__init__()
        self.marker = None
        self.markerID = None
        return


@autoregister(presentInAllWorlds=True, domain=CGF.DomainOption.DomainClient)
class LunarPickupMarkerManager(CGF.ComponentManager):
    __guiSessionProvider = dependency.descriptor(IBattleSessionProvider)

    @onAddedQuery(LunarPickupMarker, GenericComponents.TransformComponent)
    def onAddedPickupMarker(self, marker, transform):
        transform = transform.worldTransform
        matrixProduct = math_utils.MatrixProviders.product(transform, math_utils.createTranslationMatrix(marker.offset))
        data = {'visible': True, 
           'areaRadius': marker.areaRadius, 
           'disappearingRadius': marker.disappearanceRadius, 
           'reverseDisappearing': marker.reverseDisappearing, 
           ComponentBitMask.MINIMAP_MARKER: [
                                           {'symbol': marker.symbol, 
                                              'icon': marker.symbol, 
                                              'container': marker.container, 
                                              'onlyTranslation': marker.onlyTranslation}], 
           'matrixProduct': matrixProduct, 
           'bitMask': ComponentBitMask.MINIMAP_MARKER}
        marker.marker = AreaMarker(data)
        marker.markerID = self.__guiSessionProvider.shared.areaMarker.addMarker(marker.marker)

    @onRemovedQuery(LunarPickupMarker)
    def onRemovedPickupMarker(self, marker):
        areaMarkerCtrl = self.__guiSessionProvider.shared.areaMarker
        if areaMarkerCtrl and marker.markerID:
            areaMarkerCtrl.removeMarker(marker.markerID)


@bonusCapsManager(ARENA_BONUS_TYPE_CAPS.LUNAR_POSSESSION, CGF.DomainOption.DomainClient)
class LunarSpiritPossessionStatusManager(CGF.ComponentManager):
    _guiSessionProvider = dependency.descriptor(IBattleSessionProvider)
    _VIEW_STATE_ID = VehicleViewState.SPIRIT_INDICATOR

    @onAddedQuery(Vehicle, LunarSpiritBuffComponent)
    def onSpiritPickedUp(self, vehicle, _):
        self._updateSpiritPossessionStatusComponents(vehicle, True)

    @onRemovedQuery(Vehicle, LunarSpiritBuffComponent)
    def onSpiritRemoved(self, vehicle, _):
        self._updateSpiritPossessionStatusComponents(vehicle, False)

    def _showEffect(self):
        self._guiSessionProvider.invalidateVehicleState(self._VIEW_STATE_ID, DestroyTimerViewState(self._VIEW_STATE_ID, 0.0, TIMER_VIEW_STATE.WARNING, startTime=0.0))

    def _hideEffect(self):
        self._guiSessionProvider.invalidateVehicleState(self._VIEW_STATE_ID, DestroyTimerViewState(self._VIEW_STATE_ID, 0.0, None))
        return

    def _updateStatusEffect(self, vehicle, updateFunc):
        if self._isMyVehicle(vehicle):
            updateFunc()

    def _updateSpiritPossessionStatusComponents(self, vehicle, hasSpirit):
        if not vehicle:
            return
        else:
            controller = self._guiSessionProvider.dynamic.getControllerByID(BATTLE_CTRL_ID.LUNAR_POSSESSION_BATTLE_CTRL)
            if not controller:
                return
            vehicleTeam = None
            if hasattr(vehicle, 'publicInfo') and vehicle.publicInfo:
                vehicleTeam = vehicle.publicInfo.team
            if vehicleTeam is None:
                arena = avatar_getter.getArena()
                if arena:
                    vehicleInfo = arena.vehicles.get(vehicle.id)
                    if vehicleInfo:
                        vehicleTeam = vehicleInfo.get('team')
            if vehicleTeam is None:
                return
            playerTeam = avatar_getter.getPlayerTeam()
            if playerTeam is None:
                arena = avatar_getter.getArena()
                playerVehicleID = avatar_getter.getPlayerVehicleID()
                if arena and playerVehicleID:
                    playerVehicleInfo = arena.vehicles.get(playerVehicleID)
                    if playerVehicleInfo:
                        playerTeam = playerVehicleInfo.get('team')
            if playerTeam is None:
                return
            isEnemy = vehicleTeam != playerTeam
            controller.updateSpiritPossession(vehicle.id, isEnemy, hasSpirit)
            return

    def _isMyVehicle(self, vehicle):
        if vehicle:
            return vehicle.id == avatar_getter.getPlayerVehicleID()
        return False