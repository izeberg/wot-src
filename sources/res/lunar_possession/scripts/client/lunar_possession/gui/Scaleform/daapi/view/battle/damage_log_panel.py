import logging
from account_helpers.settings_core.options import DamageLogDetailsSetting
from gui.battle_control.battle_constants import PERSONAL_EFFICIENCY_TYPE as _PET
from gui.shared import EVENT_BUS_SCOPE
from lunar_possession.gui.Scaleform.daapi.view.meta.LunarBattleDamageLogPanelMeta import LunarBattleDamageLogPanelMeta
from lunar_possession.gui.shared.events import PlayerScoreUpdatedEvents
_logger = logging.getLogger(__name__)
_LUNAR_TOTAL_DAMAGE_CONTENT_MASK = _PET.DAMAGE

class LunarDamageLogPanel(LunarBattleDamageLogPanelMeta):

    def _populate(self):
        super(LunarDamageLogPanel, self)._populate()
        self.addListener(PlayerScoreUpdatedEvents.PLAYER_SCORE_UPDATED, self._handleTotalLunarScoreUpdateEvent, scope=EVENT_BUS_SCOPE.BATTLE)

    def _dispose(self):
        self.removeListener(PlayerScoreUpdatedEvents.PLAYER_SCORE_UPDATED, self._handleTotalLunarScoreUpdateEvent, scope=EVENT_BUS_SCOPE.BATTLE)
        super(LunarDamageLogPanel, self)._dispose()

    def _handleTotalLunarScoreUpdateEvent(self, event):
        self.as_updateSummaryLunarValueS(event.score)

    def _invalidateLogs(self):
        self._topLog.updateLog(0, DamageLogDetailsSetting.HIDE, 0)
        self._bottomLog.updateLog(0, DamageLogDetailsSetting.HIDE, 0)

    def _invalidateTotalDamageContentMask(self):
        return _LUNAR_TOTAL_DAMAGE_CONTENT_MASK