from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor

class PrebattleCarouselViewMeta(InjectComponentAdaptor):

    def setFilter(self, id):
        self._printOverrideError('setFilter')

    def onViewIsHidden(self):
        self._printOverrideError('onViewIsHidden')

    def as_showS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_show()

    def as_hideS(self, useAnim):
        if self._isDAAPIInited():
            return self.flashObject.as_hide(useAnim)