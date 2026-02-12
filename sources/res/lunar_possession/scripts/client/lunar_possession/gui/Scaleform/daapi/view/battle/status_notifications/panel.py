import logging
from lunar_possession.gui.Scaleform.daapi.view.battle.status_notifications import sn_items as lunar_sn_items
from gui.Scaleform.daapi.view.battle.shared.status_notifications import components
from gui.Scaleform.daapi.view.battle.shared.status_notifications import sn_items
from gui.Scaleform.daapi.view.battle.shared.status_notifications.panel import StatusNotificationTimerPanel
from gui.Scaleform.genConsts.BATTLE_NOTIFICATIONS_TIMER_COLORS import BATTLE_NOTIFICATIONS_TIMER_COLORS as COLORS
from gui.Scaleform.genConsts.BATTLE_NOTIFICATIONS_TIMER_LINKAGES import BATTLE_NOTIFICATIONS_TIMER_LINKAGES as LINKS
from gui.Scaleform.genConsts.BATTLE_NOTIFICATIONS_TIMER_TYPES import BATTLE_NOTIFICATIONS_TIMER_TYPES as TYPES
from lunar_possession.gui.Scaleform.genConsts.LUNAR_BATTLE_NOTIFICATIONS_TIMER_LINKAGES import LUNAR_BATTLE_NOTIFICATIONS_TIMER_LINKAGES as LUNAR_LINKS
from lunar_possession.gui.Scaleform.genConsts.LUNAR_BATTLE_NOTIFICATIONS_TIMER_TYPES import LUNAR_BATTLE_NOTIFICATIONS_TIMER_TYPES as LUNAR_TYPES
_logger = logging.getLogger(__name__)

class _LunarHighPriorityGroup(components.StatusNotificationsGroup):

    def __init__(self, updateCallback):
        super(_LunarHighPriorityGroup, self).__init__((
         sn_items.FireSN,
         sn_items.DrownSN,
         sn_items.HalfOverturnedSN,
         lunar_sn_items.LunarSpiritIndicatorSN), updateCallback)


class LunarStatusNotificationTimerPanel(StatusNotificationTimerPanel):

    def _generateItems(self):
        items = [
         _LunarHighPriorityGroup,
         sn_items.PersonalDeathZoneSN,
         sn_items.StunSN]
        return items

    def _generateNotificationTimerSettings(self):
        data = super(LunarStatusNotificationTimerPanel, self)._generateNotificationTimerSettings()
        link = LINKS.DESTROY_TIMER_UI
        self._addNotificationTimerSetting(data, TYPES.DROWN, LINKS.DROWN_ICON, link)
        self._addNotificationTimerSetting(data, TYPES.FIRE, LINKS.FIRE_ICON, link)
        self._addNotificationTimerSetting(data, TYPES.OVERTURNED, LINKS.OVERTURNED_ICON, link, COLORS.GREEN)
        self._addNotificationTimerSetting(data, TYPES.HALF_OVERTURNED, LINKS.HALF_OVERTURNED_ICON, link, COLORS.GREEN)
        self._addNotificationTimerSetting(data, LUNAR_TYPES.LUNAR_SPIRIT_INDICATOR, LUNAR_LINKS.LUNAR_SPIRIT_INDICATOR_ICON, link, COLORS.ORANGE, countdownVisible=False)
        return data