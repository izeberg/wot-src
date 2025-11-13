from frameworks.wulf import ViewSettings, ViewModel
from gui.impl.pub import ViewImpl
from gui.impl.gen import R

class StatisticButtonTooltip(ViewImpl):
    __slots__ = ()

    def __init__(self):
        settings = ViewSettings(R.views.gui_lootboxes.lobby.gui_lootboxes.tooltips.StatisticButtonTooltip())
        settings.model = ViewModel()
        super(StatisticButtonTooltip, self).__init__(settings)