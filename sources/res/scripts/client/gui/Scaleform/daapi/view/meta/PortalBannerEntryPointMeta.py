from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor

class PortalBannerEntryPointMeta(InjectComponentAdaptor):

    def setIsNewS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.setIsNew(value)