from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor

class TabContentMeta(InjectComponentAdaptor):

    def onTabChanged(self, tabAlias):
        self._printOverrideError('onTabChanged')