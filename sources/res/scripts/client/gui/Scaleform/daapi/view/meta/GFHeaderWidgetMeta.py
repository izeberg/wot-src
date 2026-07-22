from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor

class GFHeaderWidgetMeta(InjectComponentAdaptor):

    def as_updateMarginsS(self, top, right, left):
        if self._isDAAPIInited():
            return self.flashObject.as_updateMargins(top, right, left)