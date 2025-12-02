import BigWorld
from typing import TYPE_CHECKING, Optional, Tuple, Callable, List
import logging
from gui.battle_control import avatar_getter
from gui.shared import g_eventBus
from helpers import dependency
from helpers.events_handler import EventsHandler
from grinch_common.grinch_constants import CaptureStates
from skeletons.gui.battle_session import IBattleSessionProvider
from grinch_common.grinch_constants import CapturablePointNames
from grinch.gui.impl.gen.view_models.views.battle.grinch_base_capture_model import GrinchBaseCaptureModel, TeamColorEnum, BaseNameEnum
from grinch.gui.shared.events import CapturablePointEvent
from grinch_common.grinch_constants import Teams, GRINCH_INVADER_COMPONENT
from gui.shared.event_bus import EVENT_BUS_SCOPE, EventPriority
from grinch.cgf.capturable_point import getCapturablePointTransform
if TYPE_CHECKING:
    from grinch.gui.impl.battle.grinch_hud_view import GrinchHudView
    from frameworks.wulf import Array
logger = logging.getLogger(__name__)
TEAM_TO_TEAM_COLOR_ENUM_MAP = {Teams.CYAN: TeamColorEnum.BLUE, 
   Teams.YELL: TeamColorEnum.YELLOW, 
   Teams.MGNT: TeamColorEnum.MAGENTA, 
   Teams.BOTS: TeamColorEnum.NEUTRAL, 
   Teams.NONE: TeamColorEnum.NEUTRAL}
CAPTURABLE_POINT_NAME_MAP = {CapturablePointNames.CAPTURABLE_POINT_A: BaseNameEnum.A, 
   CapturablePointNames.CAPTURABLE_POINT_B: BaseNameEnum.B, 
   CapturablePointNames.CAPTURABLE_POINT_C: BaseNameEnum.C}

class CapturablePointsCtrl(EventsHandler):
    _sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self, hudRef):
        super(CapturablePointsCtrl, self).__init__()
        self.__hudRef = hudRef
        self.fillCapturablePointsArray()
        self._subscribe()
        self._initCapturablePointMarker()
        g_eventBus.handleEvent(CapturablePointEvent(eventType=CapturablePointEvent.UPDATE_REQUEST), scope=EVENT_BUS_SCOPE.BATTLE)

    def initCapturablePoint(self, *args, **kwargs):
        self._initCapturablePointMarker()

    def dispose(self):
        self.__hudRef = None
        self._unsubscribe()
        return

    def _getListeners(self):
        listeners = [
         (
          CapturablePointEvent.CAPTURABLE_POINT_UPDATE,
          self.updateCapturablePointModel,
          EVENT_BUS_SCOPE.BATTLE,
          EventPriority.HIGH),
         (
          CapturablePointEvent.INIT_CAPTURABLE_POINT,
          self.initCapturablePoint,
          EVENT_BUS_SCOPE.BATTLE,
          EventPriority.HIGH)]
        return listeners

    def getCapturablePointModel(self, capturablePointName):
        for model in self.capturablePointsArray:
            if model.getName() == CAPTURABLE_POINT_NAME_MAP[capturablePointName]:
                return model

        return

    @property
    def capturablePointsArray(self):
        return self.__hudRef.viewModel.getBasesCapturing()

    def updateMarkersCounter(self):
        self.__hudRef.viewModel.updateMarkersCounter.setValue(self.__hudRef.viewModel.updateMarkersCounter.getValue() + 1)

    def fillCapturablePointsArray(self):
        for name in CapturablePointNames.ALL:
            model = GrinchBaseCaptureModel()
            model.setName(CAPTURABLE_POINT_NAME_MAP[name])
            self.capturablePointsArray.addViewModel(model)

        self.capturablePointsArray.invalidate()
        self.updateMarkersCounter()

    def updateCapturablePointModel(self, event):
        with self.__hudRef.viewModel.transaction():
            model = self.getCapturablePointModel(event.capturablePointName)
            if not model:
                logger.warning('Capturable Point %s not found', event.capturablePointName)
                return
            isContestedByEnemy = event.isContested
            isContestedByTurret = event.captureState == CaptureStates.CAPTURED
            if avatar_getter.getPlayerTeam() == event.ownersTeam:
                isContestedByEnemy = False
                isContestedByTurret = False
            model.setCapturingTeamColor(TEAM_TO_TEAM_COLOR_ENUM_MAP[event.invadersTeam])
            model.setActivePlayers(event.invadersCount)
            model.setCapturePercentage(event.captureProgressPercent)
            model.setIsContestedByEnemy(isContestedByEnemy)
            model.setIsContestedByTurret(isContestedByTurret)
            model.setEstSecondsLeft(event.estTimeLeft)
            model.setOwnerTeamColor(TEAM_TO_TEAM_COLOR_ENUM_MAP[event.ownersTeam])
            self.updateProgressBar()
            self.updateMarkersCounter()

    def updateProgressBar(self):
        playerVehicle = BigWorld.player().vehicle
        if playerVehicle is None:
            self.__hudRef.viewModel.setShowCapturingBaseIndex(-1)
            return
        else:
            invasionComponent = playerVehicle.dynamicComponents.get(GRINCH_INVADER_COMPONENT)
            if invasionComponent is None:
                self.__hudRef.viewModel.setShowCapturingBaseIndex(-1)
                return
            for index, model in enumerate(self.capturablePointsArray):
                if CAPTURABLE_POINT_NAME_MAP[invasionComponent.capturablePointName] == model.getName():
                    self.__hudRef.viewModel.setShowCapturingBaseIndex(index)
                    return

            return

    def _initCapturablePointMarker(self):
        bases = self.capturablePointsArray
        for base in bases:
            with base.marker.transaction():
                self.__hudRef._markersCtrl.remove(base.marker.proxy)
                self.__hudRef._markersCtrl.add(base.marker.proxy, getCapturablePointTransform(base.getName().value))

        self.updateMarkersCounter()