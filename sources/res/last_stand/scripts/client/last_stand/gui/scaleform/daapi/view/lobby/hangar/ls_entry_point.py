from frameworks.wulf import ViewFlags
from last_stand.gui.impl.lobby.feature.ls_entry_point_view import LSEntryPointView
from last_stand.gui.scaleform.daapi.view.meta.LSEntryPointMeta import LSEntryPointMeta

class LSEntryPoint(LSEntryPointMeta):

    def _makeInjectView(self):
        return LSEntryPointView(ViewFlags.VIEW)