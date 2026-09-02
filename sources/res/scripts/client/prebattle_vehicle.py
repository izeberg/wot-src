import logging, CGF
from ClientSelectableCameraObject import ClientSelectableCameraObject
from Event import Event
from account_helpers import AccountSettings
from gui.hangar_cameras.hangar_camera_common import CameraMovementStates
from gui.shared import events, EVENT_BUS_SCOPE, g_eventBus
from account_helpers.AccountSettings import EVENT_VEHICLE
from EventVehicle import EventVehicle
from HangarVehicle import HangarVehicle
from gui.vehicle_view_states import createState4CurrentVehicle
from gui.wt_event.wt_event_helpers import g_execute_after_all_event_vehicles_loaded
from helpers import dependency
from constants import PREBATTLE_TYPE
from shared_utils import first, nextTick
from skeletons.prebattle_vehicle import IPrebattleVehicle
from skeletons.gui.shared import IItemsCache
from skeletons.gui.shared.utils import IHangarSpace
from gui.prb_control import prbDispatcherProperty
from skeletons.gui.game_control import IWhiteTigerController
from wt_settings import g_wt_config
_logger = logging.getLogger(__name__)

class PrebattleVehicle(IPrebattleVehicle):
    itemsCache = dependency.descriptor(IItemsCache)
    hangarSpace = dependency.descriptor(IHangarSpace)
    __wtController = dependency.descriptor(IWhiteTigerController)

    def __init__(self):
        super(PrebattleVehicle, self).__init__()
        self.onChanged = Event()

    def fini(self):
        self.onChanged.clear()

    @g_execute_after_all_event_vehicles_loaded
    def switchCamera(self, vehicle):
        ClientSelectableCameraObject.switchCamera(vehicle)

    def select(self, vehicle):
        isEvent = self.__wtController.isEventPrbActive()
        if vehicle is None or vehicle == self.item or not isEvent:
            return
        if vehicle.intCD not in g_wt_config.getAllVehiclesData():
            _logger.error('This service is only suitable for event vehicles')
            return
        else:
            vehicleData = g_wt_config.getVehicleData(vehicle.intCD)
            query = CGF.Query(self.hangarSpace.spaceID, EventVehicle)
            if not query.empty():
                for ev in query.values():
                    if ev.eventType == vehicleData.subType:
                        ev.select(vehicle.descriptor)

                nextTick(self.onChanged)()
            else:
                self.__selectDefer(vehicleData.subType, vehicle)
            self.__wtController.saveSelectVehicleCD(vehicle.intCD)
            return

    @g_execute_after_all_event_vehicles_loaded
    def __selectDefer(self, eventType, vehicle):

        def select():
            query = CGF.Query(self.hangarSpace.spaceID, EventVehicle)
            for ev in query.values():
                if ev.eventType == eventType:
                    ev.select(vehicle.descriptor)

            nextTick(self.onChanged)()

        nextTick(select)()

    def selectAny(self):
        g_eventBus.handleEvent(events.LobbySimpleEvent(events.HangarSimpleEvent.UPDATE_CAROUSEL_VEHICLE_STATES), scope=EVENT_BUS_SCOPE.LOBBY)
        vehicle = self.__wtController.getCurrentVehicle()
        if vehicle:
            self.select(vehicle)

    def selectNone(self):
        query = CGF.Query(self.hangarSpace.spaceID, HangarVehicle)
        if not query.empty():
            vehicle = first(query.values())
            self.switchCamera(vehicle)

    def getViewState(self):
        return createState4CurrentVehicle(self)

    def isPresent(self):
        return self.item is not None

    def isPremiumIGR(self):
        return self.isPresent() and self.item.isPremiumIGR

    def isInHangar(self):
        return self.isPresent() and not self.item.isInBattle

    def isDisabled(self):
        return self.isPresent() and self.item.isDisabled

    def isBroken(self):
        return self.isPresent() and self.item.isBroken

    def isDisabledInRent(self):
        return self.isPresent() and self.item.rentalIsOver

    def isOnlyForEventBattles(self):
        return self.isPresent() and self.item.isOnlyForEventBattles

    def isOutfitLocked(self):
        return self.isPresent() and self.item.isOutfitLocked

    def isCustomizationEnabled(self):
        return not self.isPresent() or self.item.isCustomizationEnabled()

    def isSquad(self):
        if self.prbDispatcher:
            state = self.prbDispatcher.getFunctionalState()
            isSquad = state.isInUnit(PREBATTLE_TYPE.SQUAD) or state.isInUnit(PREBATTLE_TYPE.WHITE_TIGER) or state.isInUnit(PREBATTLE_TYPE.EPIC)
            return isSquad
        return False

    @prbDispatcherProperty
    def prbDispatcher(self):
        return

    @property
    def item(self):
        query = CGF.Query(self.hangarSpace.spaceID, EventVehicle)
        if query.empty() or not query.values():
            return
        for ev in query.values():
            if ev.state == CameraMovementStates.ON_OBJECT:
                return self.itemsCache.items.getItemByCD(ev.typeDescriptor.type.compactDescr)

        return

    @property
    def invID(self):
        if self.item is None:
            return 0
        else:
            return self.item.invID

    @property
    def lastInvID(self):
        return AccountSettings.getFavorites(EVENT_VEHICLE)

    @property
    def intCD(self):
        if self.item is None:
            return 0
        else:
            return self.item.invID

    @property
    def lastIntCD(self):
        return self.__wtController.accountSettings.savedVehicleCD