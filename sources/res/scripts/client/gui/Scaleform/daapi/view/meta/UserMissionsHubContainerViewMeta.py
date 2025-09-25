from gui.Scaleform.framework.entities.View import View

class UserMissionsHubContainerViewMeta(View):

    def resetFilters(self):
        self._printOverrideError('resetFilters')

    def onClose(self):
        self._printOverrideError('onClose')

    def as_showFilterCounterS(self, countText, isFilterApplied):
        if self._isDAAPIInited():
            return self.flashObject.as_showFilterCounter(countText, isFilterApplied)

    def as_blinkFilterCounterS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_blinkFilterCounter()

    def as_updateCommonMissionsTabVisibilityS(self, isVisible):
        if self._isDAAPIInited():
            return self.flashObject.as_updateCommonMissionsTabVisibility(isVisible)

    def as_updateCommonMissionsTabPositionS(self, posY, maxHeight):
        if self._isDAAPIInited():
            return self.flashObject.as_updateCommonMissionsTabPosition(posY, maxHeight)

    def as_setBackgroundS(self, source):
        if self._isDAAPIInited():
            return self.flashObject.as_setBackground(source)