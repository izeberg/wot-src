from gui.Scaleform.daapi.view.lobby.popover.SmartPopOverView import SmartPopOverView

class CrewOperationsPopOverMeta(SmartPopOverView):

    def invokeOperation(self, operationName):
        self._printOverrideError('invokeOperation')

    def onToggleClick(self, operationName):
        self._printOverrideError('onToggleClick')

    def as_updateS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_update(data)