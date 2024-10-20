from frameworks.wulf import ViewFlags
from gui.Scaleform.daapi.view.meta.StrongholdEntryPointMeta import StrongholdEntryPointMeta
from gui.impl.lobby.stronghold.stronghold_entry_point_view import StrongholdEntryPointView

class StrongholdEntryPoint(StrongholdEntryPointMeta):

    def _makeInjectView(self):
        self.__view = StrongholdEntryPointView(ViewFlags.VIEW)
        return self.__view

    def isSingle(self, value):
        if self.__view:
            self.__view.setIsSingle(value)