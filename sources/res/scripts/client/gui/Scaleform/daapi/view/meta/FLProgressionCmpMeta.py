from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor

class FLProgressionCmpMeta(InjectComponentAdaptor):

    def as_updateVisibilityS(self, isVisible):
        if self._isDAAPIInited():
            return self.flashObject.as_updateVisibility(isVisible)