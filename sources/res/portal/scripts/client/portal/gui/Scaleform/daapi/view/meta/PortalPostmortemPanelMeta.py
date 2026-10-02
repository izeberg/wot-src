from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class PortalPostmortemPanelMeta(BaseDAAPIComponent):

    def as_setTimerS(self, time):
        if self._isDAAPIInited():
            return self.flashObject.as_setTimer(time)