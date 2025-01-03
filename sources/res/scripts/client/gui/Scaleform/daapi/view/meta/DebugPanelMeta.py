from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class DebugPanelMeta(BaseDAAPIComponent):

    def as_initReplayS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_initReplay()

    def as_updatePingS(self, ping):
        if self._isDAAPIInited():
            return self.flashObject.as_updatePing(ping)

    def as_updateFpsS(self, fps):
        if self._isDAAPIInited():
            return self.flashObject.as_updateFps(fps)

    def as_updatePingFPSS(self, ping, fps):
        if self._isDAAPIInited():
            return self.flashObject.as_updatePingFPS(ping, fps)

    def as_updateAllS(self, ping, fps, isLagging):
        if self._isDAAPIInited():
            return self.flashObject.as_updateAll(ping, fps, isLagging)

    def as_updateReplayS(self, ping, fps, isLagging, replayFps):
        if self._isDAAPIInited():
            return self.flashObject.as_updateReplay(ping, fps, isLagging, replayFps)