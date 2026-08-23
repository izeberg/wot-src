from __future__ import absolute_import
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.pub import ViewImpl
from journey_marathon.gui.impl.gen.view_models.views.lobby.src.views.tooltips.lore_tooltip_model import LoreTooltipModel

class JmLoreTooltipView(ViewImpl):
    LAYOUT_ID = R.views.journey_marathon.mono.lobby.tooltips.lore_tooltip()
    __slots__ = ('__node', )

    def __init__(self, node):
        super(JmLoreTooltipView, self).__init__(settings=ViewSettings(layoutID=self.LAYOUT_ID, model=LoreTooltipModel()))
        self.__node = node

    def _onLoading(self, *args, **kwargs):
        super(JmLoreTooltipView, self)._onLoading(*args, **kwargs)
        with self.getViewModel().transaction() as (tx):
            tx.setIsUnlocked(self.__node.isExplored)