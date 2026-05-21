from gui.Scaleform.daapi.view.meta.ResizableEntryPointMeta import ResizableEntryPointMeta
from gui.impl.lobby.summer_sale.summer_sale_entry_point_view import SummerSaleEntryPointView

class SummerSaleEntryPoint(ResizableEntryPointMeta):

    def isSingle(self, value):
        if self.__view:
            self.__view.setIsSingle(value)

    def _makeInjectView(self):
        self.__view = SummerSaleEntryPointView()
        return self.__view