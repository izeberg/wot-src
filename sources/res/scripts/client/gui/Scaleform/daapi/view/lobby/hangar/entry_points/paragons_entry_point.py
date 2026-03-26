from gui.Scaleform.daapi.view.meta.ResizableEntryPointMeta import ResizableEntryPointMeta
from gui.impl.lobby.paragons.banner.banner_view import ParagonsBannerView

class ParagonsBannerEntryPoint(ResizableEntryPointMeta):

    def isSingle(self, value):
        pass

    def _makeInjectView(self):
        self.__view = ParagonsBannerView()
        return self.__view