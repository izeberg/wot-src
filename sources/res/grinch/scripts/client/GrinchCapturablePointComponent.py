from functools import wraps
from typing import TYPE_CHECKING
from cgf_script.component_meta_class import registerReplicableComponent
from grinch.gui.shared.events import CapturablePointEvent
from grinch_common.cgf.capturable_point import GrinchCapturablePointComponentDescr as CapturablePointCommonDescr
from gui.shared import g_eventBus
from gui.shared.event_bus import EVENT_BUS_SCOPE, EventPriority
from script_component.DynamicScriptComponent import DynamicScriptComponent
from shared_utils import nextTick
from vehicle_systems.stricted_loading import makeCallbackWeak
if TYPE_CHECKING:
    from typing import Any

class GrinchCapturablePointComponentDescr(CapturablePointCommonDescr):
    pass


def capturablePointEventWrapper(func):

    @wraps(func)
    def wrapper(self, *args, **kwargs):
        nextTick(makeCallbackWeak(self._sendEvent))()
        return func(self, *args, **kwargs)

    return wrapper


@registerReplicableComponent
class GrinchCapturablePointComponent(DynamicScriptComponent, GrinchCapturablePointComponentDescr):

    def __init__(self):
        super(GrinchCapturablePointComponent, self).__init__()
        g_eventBus.addListener(CapturablePointEvent.UPDATE_REQUEST, self._onUpdateRequested, EVENT_BUS_SCOPE.BATTLE, EventPriority.HIGH)

    def onDestroy(self):
        g_eventBus.removeListener(CapturablePointEvent.UPDATE_REQUEST, self._onUpdateRequested, EVENT_BUS_SCOPE.BATTLE)

    @capturablePointEventWrapper
    def set_invadersCount(self, _):
        pass

    @capturablePointEventWrapper
    def set_capturablePointOwnerTeam(self, _):
        pass

    @capturablePointEventWrapper
    def set_invadingTeam(self, _):
        pass

    @capturablePointEventWrapper
    def set_currentPoints(self, _):
        pass

    @capturablePointEventWrapper
    def set_isContested(self, _):
        pass

    @capturablePointEventWrapper
    def set_captureState(self, _):
        pass

    def calculatePercentage(self):
        return float(self.currentPoints) / self.maxPoints * 100

    def calculatePointsPerSecond(self):
        return self.pointsForInvader * (self.invadersCount or 1)

    def calculateEstTimeLeft(self):
        return (self.maxPoints - self.currentPoints) / self.calculatePointsPerSecond()

    def _sendEvent(self):
        g_eventBus.handleEvent(CapturablePointEvent(eventType=CapturablePointEvent.CAPTURABLE_POINT_UPDATE, capturablePointName=self.capturablePointName, invadersTeam=self.invadingTeam, invadersCount=self.invadersCount, ownersTeam=self.capturablePointOwnerTeam, isContested=self.isContested, captureProgressPercent=self.calculatePercentage(), estTimeLeft=self.calculateEstTimeLeft(), captureState=self.captureState), scope=EVENT_BUS_SCOPE.BATTLE)

    def _onUpdateRequested(self, _):
        self._sendEvent()