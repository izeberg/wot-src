import Event
from items.utils import isclose
from script_component.DynamicScriptComponent import DynamicScriptComponent
from portal_common_cgf.camp.components import CampReplicableComponent as CampReplicableComponentBase

class CampReplicableComponent(DynamicScriptComponent, CampReplicableComponentBase):
    onCanBeCaptured = Event.Event()
    onCaptured = Event.Event()
    onCapturing = Event.Event()
    onStopCapturing = Event.Event()

    @property
    def gameObject(self):
        return self.entity.entityGameObject

    def set_canBeCaptured(self, prev):
        if not prev and self.canBeCaptured:
            self.onCanBeCaptured(self.gameObject)

    def set_isCaptured(self, prev):
        if not prev and self.isCaptured:
            self.onCaptured(self.gameObject)

    def set_captureProgress(self, _):
        if isclose(self.captureProgress, 0.0):
            return
        info = self.__getCapturableInfo()
        self.onCapturing(info)

    def set_captureCurrentSpeed(self, prev):
        if isclose(self.captureCurrentSpeed, 0.0):
            self.onStopCapturing(self.gameObject)
            return
        info = self.__getCapturableInfo()
        self.onCapturing(info)

    def __getCapturableInfo(self):
        progress = self.captureProgress
        maxProgress = self.captureTotal
        captureSpeed = self.captureCurrentSpeed
        timeLeft = (isclose(captureSpeed, 0.0) or maxProgress - progress) / captureSpeed if 1 else 0
        MAX_PROGRESS_IN_PERCENT = 100
        progressInPercent = (isclose(maxProgress, 0.0) or progress * MAX_PROGRESS_IN_PERCENT) / maxProgress if 1 else 0
        return {'invaderCount': self.invaderCount, 
           'progress': int(progressInPercent), 
           'timeLeft': int(timeLeft), 
           'index': self.index, 
           'name': self.gameObject.name}