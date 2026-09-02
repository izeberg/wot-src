from frameworks.wulf import ViewSettings, ViewModel
from gui.impl.gen import R
from gui.impl.pub import ViewImpl

class ModeInfoTooltip(ViewImpl):
    __slots__ = ()

    def __init__(self):
        settings = ViewSettings(R.views.mono.winback.tooltips.mode_info_tooltip())
        settings.model = ViewModel()
        super(ModeInfoTooltip, self).__init__(settings)