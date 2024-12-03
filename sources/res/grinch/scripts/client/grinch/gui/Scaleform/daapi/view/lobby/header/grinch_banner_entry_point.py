from grinch.gui.impl.lobby.banner_entry_point.grinch_banner_entry_point import GrinchBannerEntryPoint as GrinchBannerEntryPointView
from grinch.gui.Scaleform.daapi.view.meta.GrinchBannerEntryPointMeta import GrinchBannerEntryPointMeta

class GrinchBannerEntryPoint(GrinchBannerEntryPointMeta):

    def isSingle(self, value):
        if self.__view:
            self.__view.setIsSingle(value)

    def _makeInjectView(self):
        self.__view = GrinchBannerEntryPointView()
        return self.__view