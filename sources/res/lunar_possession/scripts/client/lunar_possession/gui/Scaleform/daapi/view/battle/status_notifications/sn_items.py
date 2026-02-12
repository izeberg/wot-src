from gui.Scaleform.daapi.view.battle.shared.status_notifications import sn_items
from gui.impl import backport
from gui.impl.gen import R
from lunar_possession.cgf.ui import TIMER_VIEW_STATE
from lunar_possession.gui.Scaleform.genConsts.LUNAR_BATTLE_NOTIFICATIONS_TIMER_TYPES import LUNAR_BATTLE_NOTIFICATIONS_TIMER_TYPES
from lunar_possession.gui.battle_control.lunar_battle_constants import VehicleViewState

class LunarSpiritIndicatorSN(sn_items.DestroyMiscTimerSN):

    def start(self):
        super(LunarSpiritIndicatorSN, self).start()
        self._subscribeOnVehControlling()

    def getItemID(self):
        return VehicleViewState.SPIRIT_INDICATOR

    def getViewTypeID(self):
        return LUNAR_BATTLE_NOTIFICATIONS_TIMER_TYPES.LUNAR_SPIRIT_INDICATOR

    def _getDescription(self, value=None):
        return backport.text(R.strings.lunar_battle.statusNotificationTimers.lunarSpiritIndicator())

    def _getSupportedLevel(self):
        return TIMER_VIEW_STATE.WARNING

    def _update(self, state):
        self._setVisible(self._getSupportedLevel() == state.level)