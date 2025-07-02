from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.pub import ViewImpl
from mt_birthday.gui.impl.gen.view_models.views.lobby.tooltips.gold_ticket_tooltip_model import GoldTicketTooltipModel

class GoldTicketTooltip(ViewImpl):

    def __init__(self):
        settings = ViewSettings(layoutID=R.views.mt_birthday.lobby.tooltips.GoldTicketTooltip(), model=GoldTicketTooltipModel())
        super(GoldTicketTooltip, self).__init__(settings)