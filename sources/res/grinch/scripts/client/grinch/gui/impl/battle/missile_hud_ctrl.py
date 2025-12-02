import typing, logging, BigWorld
from Math import Matrix
from constants import EQUIPMENT_STAGES, NULL_ENTITY_ID
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE
from grinch.gui.impl.gen.view_models.views.battle.grinch_missile_target_marker_model import TargetingStatus
from grinch_common.cgf.missiles import TRACKING_COMPONENT_NAME
from grinch_common.grinch_constants import GrinchAbilities, TARGET_LOST_MARKER_DISABLE_ANIMATION_DELAY
from helpers import dependency
from helpers.CallbackDelayer import CallbackDelayer
from helpers.events_handler import EventsHandler
from skeletons.gui.battle_session import IBattleSessionProvider
if typing.TYPE_CHECKING:
    from grinch.gui.impl.gen.view_models.views.battle.grinch_hud.missile_hud_model import MissileHudModel
    from gui.battle_control.controllers.vehicle_state_ctrl import VehicleStateController
    from typing import Generator
_logger = logging.getLogger(__name__)

def lostMarkerToggler():
    step = 0
    while True:
        yield step % 2
        step += 1


class MissileHudCtrl(EventsHandler):
    _sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self, hudRef):
        super(MissileHudCtrl, self).__init__()
        self.__hudRef = hudRef
        self._delayer = CallbackDelayer()
        self._lockingComponent = BigWorld.player().vehicle.dynamicComponents.get(TRACKING_COMPONENT_NAME)
        self._lockingVisualComponent = BigWorld.player().vehicle.dynamicComponents.get(GrinchAbilities.GRINCH_MISSILES)
        self._lostMarkerStep = lostMarkerToggler()
        self._initMissileModel()
        self._initEvents()
        self._subscribe()

    def _getEvents(self):
        events = []
        vehicleCtrl = self._sessionProvider.shared.vehicleState
        if vehicleCtrl is not None:
            events.append((vehicleCtrl.onVehicleStateUpdated, self._onVehicleStateUpdated))
        return events

    @property
    def viewModel(self):
        return self.__hudRef.viewModel.missileHud

    def dispose(self):
        self.__hudRef = None
        self._delayer.destroy()
        self._delayer = None
        if self._lockingVisualComponent is not None:
            self._lockingVisualComponent.onStateUpdated -= self._onEquipmentUpdated
        self._lockingVisualComponent = None
        if self._lockingComponent is not None:
            self._lockingComponent.onTargetAcquiring -= self._onTargetAcquiring
            self._lockingComponent.onTargetAcquired -= self._onTargetAcquired
            self._lockingComponent.onTargetLost -= self._onTargetLost
        self._lockingComponent = None
        self._unsubscribe()
        self._lostMarkerStep = None
        return

    def _initEvents(self):
        if self._lockingVisualComponent is not None:
            self._lockingVisualComponent.onStateUpdated += self._onEquipmentUpdated
        if self._lockingComponent is not None:
            self._lockingComponent.onTargetAcquiring += self._onTargetAcquiring
            self._lockingComponent.onTargetAcquired += self._onTargetAcquired
            self._lockingComponent.onTargetLost += self._onTargetLost
        return

    def _onEquipmentUpdated(self, stage, prevStage):
        if EQUIPMENT_STAGES.PREPARING not in (stage, prevStage):
            return
        with self.viewModel.transaction() as (model):
            model.setIsTargeting(stage == EQUIPMENT_STAGES.PREPARING)
            self._resetModels()

    def _onVehicleStateUpdated(self, state, _):
        if self._lockingComponent and state in (VEHICLE_VIEW_STATE.DESTROYED, VEHICLE_VIEW_STATE.CREW_DEACTIVATED):
            self._lockingComponent.setTargetVehicleID(NULL_ENTITY_ID)
            self.viewModel.setIsTargeting(False)
            self._resetModels()
        elif state == VEHICLE_VIEW_STATE.SWITCHING:
            if BigWorld.player().vehicle and BigWorld.player().vehicle.isAlive():
                self._lockingComponent = BigWorld.player().vehicle.dynamicComponents.get(TRACKING_COMPONENT_NAME)
                self._lockingVisualComponent = BigWorld.player().vehicle.dynamicComponents.get(GrinchAbilities.GRINCH_MISSILES)
                self._initEvents()

    def _onTargetAcquiring(self, targetVehicleID, lockTime):
        if not targetVehicleID:
            return
        else:
            with self.viewModel.transaction() as (model):
                if model.currentTargetMarker.getIsEnabled():
                    model.currentTargetMarker.setRemainingLockTime(lockTime)
                    return
                targetVehicle = BigWorld.entities.get(targetVehicleID, None)
                if not targetVehicle:
                    _logger.warning("Couldn't retrieve target vehicle with id %i", targetVehicleID)
                    return
                model.currentTargetMarker.setTargetID(targetVehicleID)
                model.currentTargetMarker.setTargetingStatus(TargetingStatus.TARGETING)
                model.currentTargetMarker.setRemainingLockTime(lockTime)
                model.currentTargetMarker.setIsEnabled(True)
                self.__hudRef._markersCtrl.add(model.currentTargetMarker.proxy, targetVehicle.matrix)
            return

    def _onTargetLost(self, targetVehicleID):
        self._disableLostMarker()
        with self.viewModel.transaction() as (model):
            model.currentTargetMarker.setIsEnabled(False)
            self.__hudRef._markersCtrl.remove(model.currentTargetMarker.proxy)
            targetVehicle = BigWorld.entities.get(targetVehicleID, None)
            if not targetVehicle:
                _logger.info("Couldn't retrieve lost target vehicle with id %i", targetVehicleID)
                return
            step = next(self._lostMarkerStep)
            targetMatrix = Matrix(targetVehicle.matrix)
            if step:
                model.lostTargetMarkerOdd.setIsEnabled(True)
                self.__hudRef._markersCtrl.add(model.lostTargetMarkerOdd.proxy, targetMatrix)
            else:
                model.lostTargetMarkerEven.setIsEnabled(True)
                self.__hudRef._markersCtrl.add(model.lostTargetMarkerEven.proxy, targetMatrix)
            self._delayer.delayCallback(TARGET_LOST_MARKER_DISABLE_ANIMATION_DELAY, self._disableLostMarker)
        return

    def _onTargetAcquired(self, targetVehicleID):
        with self.viewModel.transaction() as (model):
            if not model.currentTargetMarker.getIsEnabled():
                _logger.warning('You are trying to lock on vehicle ID %i when reticle was disabled', targetVehicleID)
                return
            model.currentTargetMarker.setTargetingStatus(TargetingStatus.LOCKED)
            model.currentTargetMarker.setRemainingLockTime(0)

    def _disableLostMarker(self):
        with self.viewModel.transaction() as (model):
            model.lostTargetMarkerEven.setIsEnabled(False)
            model.lostTargetMarkerOdd.setIsEnabled(False)
            self.__hudRef._markersCtrl.remove(model.lostTargetMarkerEven.proxy)
            self.__hudRef._markersCtrl.remove(model.lostTargetMarkerOdd.proxy)

    def _resetModels(self):
        with self.viewModel.transaction() as (model):
            model.currentTargetMarker.setIsEnabled(False)
            model.currentTargetMarker.setTargetingStatus(TargetingStatus.TARGETING)
            model.currentTargetMarker.setRemainingLockTime(self._lockingComponent.timeToLock)
            model.lostTargetMarkerEven.setIsEnabled(False)
            model.lostTargetMarkerOdd.setIsEnabled(False)
            self._delayer.clearCallbacks()

    def _initMissileModel(self):
        if not self._lockingComponent:
            return
        with self.viewModel.transaction() as (model):
            model.setPercentageX(self._lockingComponent.screenFactorX * 100)
            model.setPercentageY(self._lockingComponent.screenFactorY * 100)