from frameworks.wulf import ViewFlags, ViewSettings, WindowFlags
from lunar_possession.gui.impl.gen.view_models.views.battle.lunar_help_view_model import LunarHelpViewModel
from gui.impl.gen import R
from gui.impl.pub import ViewImpl, WindowImpl

class LunarHelpView(ViewImpl):
    __slots__ = ()

    def __init__(self, layoutID):
        settings = ViewSettings(layoutID)
        settings.flags = ViewFlags.VIEW
        settings.model = LunarHelpViewModel()
        super(LunarHelpView, self).__init__(settings)

    @property
    def viewModel(self):
        return super(LunarHelpView, self).getViewModel()


class LunarHelpWindow(WindowImpl):
    __slots__ = ()

    def __init__(self):
        super(LunarHelpWindow, self).__init__(wndFlags=WindowFlags.WINDOW | WindowFlags.WINDOW_FULLSCREEN, content=LunarHelpView(R.views.lunar_possession.battle.LunarHelpView()))