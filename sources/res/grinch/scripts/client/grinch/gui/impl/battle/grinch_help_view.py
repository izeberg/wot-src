from typing import TYPE_CHECKING
import ArenaType, BigWorld
from frameworks.wulf import ViewFlags, ViewSettings, WindowFlags
from grinch.gui.impl.gen.view_models.views.battle.grinch_help_view_model import GrinchHelpViewModel, MapTypeEnum
from gui.impl.gen import R
from gui.impl.pub import ViewImpl, WindowImpl
if TYPE_CHECKING:
    from typing import List, Any, Dict

class GrinchHelpView(ViewImpl):
    __slots__ = ()

    def __init__(self, layoutID):
        settings = ViewSettings(layoutID)
        settings.flags = ViewFlags.VIEW
        settings.model = GrinchHelpViewModel()
        super(GrinchHelpView, self).__init__(settings)

    @property
    def viewModel(self):
        return super(GrinchHelpView, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        super(GrinchHelpView, self)._onLoading(*args, **kwargs)
        with self.viewModel.transaction() as (model):
            model.setType(MapTypeEnum(ArenaType.g_cache[BigWorld.player().arenaTypeID].geometryName))


class GrinchHelpWindow(WindowImpl):
    __slots__ = ()

    def __init__(self):
        super(GrinchHelpWindow, self).__init__(wndFlags=WindowFlags.WINDOW | WindowFlags.WINDOW_FULLSCREEN, content=GrinchHelpView(R.views.grinch.battle.GrinchHelpView()))