from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class PortalEnemiesPanelMeta(BaseDAAPIComponent):

    def as_setCurrentPhaseS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setCurrentPhase(value)

    def as_setPhasesCountS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setPhasesCount(value)

    def as_setLaneVehicleInfoS(self, laneIndex, heavyCount, mediumCount, lightCount):
        if self._isDAAPIInited():
            return self.flashObject.as_setLaneVehicleInfo(laneIndex, heavyCount, mediumCount, lightCount)

    def as_setBuffStatusVisibleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setBuffStatusVisible(value)

    def as_resetStateS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_resetState()