from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class TabScreenMeta(BaseDAAPIComponent):

    def onSelectQuest(self, questID):
        self._printOverrideError('onSelectQuest')

    def onStatsTableVisibiltyToggled(self, isVisible):
        self._printOverrideError('onStatsTableVisibiltyToggled')

    def as_questProgressPerformS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_questProgressPerform(data)

    def as_updateProgressTrackingS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateProgressTracking(data)

    def as_setActiveTabS(self, tabIndex):
        if self._isDAAPIInited():
            return self.flashObject.as_setActiveTab(tabIndex)

    def as_resetActiveTabS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_resetActiveTab()

    def as_updateTabsS(self, dataProvider):
        if self._isDAAPIInited():
            return self.flashObject.as_updateTabs(dataProvider)