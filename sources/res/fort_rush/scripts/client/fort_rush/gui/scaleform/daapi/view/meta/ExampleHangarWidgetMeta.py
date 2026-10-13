from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class ExampleHangarWidgetMeta(BaseDAAPIComponent):

    def as_showSomeDataS(self, message, iconSource):
        if self._isDAAPIInited():
            return self.flashObject.as_showSomeData(message, iconSource)

    def as_setVisibilityS(self, isVisible):
        if self._isDAAPIInited():
            return self.flashObject.as_setVisibility(isVisible)