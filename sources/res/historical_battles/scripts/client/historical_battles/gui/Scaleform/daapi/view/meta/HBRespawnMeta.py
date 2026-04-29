from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class HBRespawnMeta(BaseDAAPIComponent):

    def onPickVehicle(self, id):
        self._printOverrideError('onPickVehicle')

    def onSelectVehicle(self):
        self._printOverrideError('onSelectVehicle')

    def as_updateGoalTimeS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_updateGoalTime(value)

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_setTimerDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setTimerData(data)

    def as_setVisibilityS(self, isVisible, isRespawn=False):
        if self._isDAAPIInited():
            return self.flashObject.as_setVisibility(isVisible, isRespawn)