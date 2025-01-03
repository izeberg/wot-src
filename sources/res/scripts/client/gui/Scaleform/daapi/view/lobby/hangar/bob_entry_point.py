from frameworks.wulf import ViewFlags
from gui.Scaleform.daapi.view.meta.BOBEventEntryPointMeta import BOBEventEntryPointMeta
from gui.impl.lobby.bob.bob_entry_point_view import BobEntryPointView

class BobEntryPoint(BOBEventEntryPointMeta):

    def _makeInjectView(self):
        self.__view = BobEntryPointView(ViewFlags.VIEW)
        return self.__view