from gui.Scaleform.daapi.view.lobby.prime_time_view_base import PrimeTimeViewBase

class EpicPrimeTimeMeta(PrimeTimeViewBase):

    def as_setHeaderTextS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setHeaderText(value)

    def as_setBackgroundSourceS(self, source):
        if self._isDAAPIInited():
            return self.flashObject.as_setBackgroundSource(source)

    def as_setFullscreenModeSupportedS(self, isSupported):
        if self._isDAAPIInited():
            return self.flashObject.as_setFullscreenModeSupported(isSupported)

    def as_setCloseBtnVisibilityS(self, isVisible):
        if self._isDAAPIInited():
            return self.flashObject.as_setCloseBtnVisibility(isVisible)

    def as_setShadowVisibilityS(self, isVisible):
        if self._isDAAPIInited():
            return self.flashObject.as_setShadowVisibility(isVisible)