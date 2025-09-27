from gui.Scaleform.daapi.view.meta.ResizableEntryPointMeta import ResizableEntryPointMeta
from gui.impl.lobby.black_market.black_market_entry_point_view import BlackMarketEntryPointView

class BlackMarketEntryPoint(ResizableEntryPointMeta):

    def isSingle(self, value):
        if self.__view:
            self.__view.setIsSingle(value)

    def _makeInjectView(self):
        self.__view = BlackMarketEntryPointView()
        return self.__view