from frameworks.wulf import ViewSettings, ViewModel
from gui.impl.gen import R
from gui.impl.pub import ViewImpl

class CrewBookMouseTooltip(ViewImpl):

    def __init__(self):
        settings = ViewSettings(R.views.lobby.crew.tooltips.CrewBookMouseTooltip(), model=ViewModel())
        super(CrewBookMouseTooltip, self).__init__(settings)