from gui.Scaleform.daapi.view.meta.EpicMinimapMeta import EpicMinimapMeta

class HBMinimapMeta(EpicMinimapMeta):

    def as_setTabModeS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setTabMode(value)