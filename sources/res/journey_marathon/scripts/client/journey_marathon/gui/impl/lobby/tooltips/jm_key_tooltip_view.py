from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.pub import ViewImpl
from journey_marathon.gui.impl.gen.view_models.views.lobby.src.views.tooltips.key_tooltip_model import KeyTooltipModel

class JmKeyTooltipView(ViewImpl):
    LAYOUT_ID = R.views.journey_marathon.mono.lobby.tooltips.key_tooltip()
    __slots__ = ('__keyName', )

    def __init__(self, keyName):
        settings = ViewSettings(layoutID=self.LAYOUT_ID, model=KeyTooltipModel())
        super(JmKeyTooltipView, self).__init__(settings)
        self.__keyName = keyName

    def _onLoading(self, *args, **kwargs):
        super(JmKeyTooltipView, self)._onLoading(*args, **kwargs)
        with self.getViewModel().transaction() as (tx):
            tx.setKeyName(self.__keyName)