from gui.Scaleform.framework.entities.View import View

class PersonalMissionOperationsMeta(View):

    def closeView(self):
        self._printOverrideError('closeView')

    def onTabSelected(self, tabIdx):
        self._printOverrideError('onTabSelected')

    def as_setSelectedTabS(self, tabIdx):
        if self._isDAAPIInited():
            return self.flashObject.as_setSelectedTab(tabIdx)