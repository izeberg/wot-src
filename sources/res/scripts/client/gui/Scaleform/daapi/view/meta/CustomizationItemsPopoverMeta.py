from gui.Scaleform.daapi.view.lobby.popover.SmartPopOverView import SmartPopOverView

class CustomizationItemsPopoverMeta(SmartPopOverView):

    def remove(self, id, itemsList):
        self._printOverrideError('remove')

    def removeAll(self):
        self._printOverrideError('removeAll')

    def onFilterChanged(self, showHistoric, showNonHistoric, showFantastic):
        self._printOverrideError('onFilterChanged')

    def as_setHeaderDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setHeaderData(data)

    def as_getDPS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getDP()

    def as_showClearMessageS(self, isClear, message):
        if self._isDAAPIInited():
            return self.flashObject.as_showClearMessage(isClear, message)