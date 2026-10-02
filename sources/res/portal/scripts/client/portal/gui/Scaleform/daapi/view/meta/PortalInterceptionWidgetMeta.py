from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class PortalInterceptionWidgetMeta(BaseDAAPIComponent):

    def as_updateTimeS(self, seconds):
        if self._isDAAPIInited():
            return self.flashObject.as_updateTime(seconds)