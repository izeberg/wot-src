from frameworks.wulf import ViewSettings, ViewFlags, ViewModel
from gui.impl.gen import R
from gui.impl.pub import ViewImpl

class SkillOrderTooltip(ViewImpl):

    def __init__(self):
        settings = ViewSettings(R.views.frontline.mono.lobby.tooltips.skill_order_tooltip(), ViewFlags.VIEW, ViewModel())
        super(SkillOrderTooltip, self).__init__(settings)