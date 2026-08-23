from __future__ import absolute_import
from frameworks.wulf import ViewSettings
from gui.impl.backport import text
from gui.impl.gen import R
from gui.impl.pub import ViewImpl
from journey_marathon.gui.impl.gen.view_models.views.lobby.src.views.tooltips.locked_tooltip_model import LockedTooltipModel
from journey_marathon_common.journey_marathon_constants import parseUnlockTokenKey
from shared_utils import first

class JmLockedTooltipView(ViewImpl):
    LAYOUT_ID = R.views.journey_marathon.mono.lobby.tooltips.locked_tooltip()
    __slots__ = ('__node', )

    def __init__(self, node):
        super(JmLockedTooltipView, self).__init__(settings=ViewSettings(layoutID=self.LAYOUT_ID, model=LockedTooltipModel()))
        self.__node = node

    def _onLoading(self, *args, **kwargs):
        super(JmLockedTooltipView, self)._onLoading(*args, **kwargs)
        with self.getViewModel().transaction() as (tx):
            keyName = parseUnlockTokenKey(first(self.__node.lockedBy))
            res = R.strings.journey_marathon.lockToken.dyn(keyName)
            tx.setKeyName(text(res.name()) if res.isValid() else keyName)
            tx.setIsUnlocked(self.__node.isExplored)