from grinch.gui.battle_control import grinch_battle_constants
from gui.Scaleform.daapi.view.battle.shared.timers_panel import TimersPanel, _TIMERS_PRIORITY
from gui.Scaleform.genConsts.BATTLE_NOTIFICATIONS_TIMER_COLORS import BATTLE_NOTIFICATIONS_TIMER_COLORS
from gui.Scaleform.genConsts.BATTLE_NOTIFICATIONS_TIMER_LINKAGES import BATTLE_NOTIFICATIONS_TIMER_LINKAGES
from gui.Scaleform.genConsts.BATTLE_NOTIFICATIONS_TIMER_TYPES import BATTLE_NOTIFICATIONS_TIMER_TYPES as _TIMER_STATES
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE, TIMER_VIEW_STATE
from gui.impl import backport
from gui.impl.gen import R
_CHASED_BY_MISSILE = 'chasedByMissile'
_FREEZING_ZONE_UI_TIMER = 'freezingZone'
_FLARE_MARK_UI_TIMER = 'flareMark'
_DART_STUN_UI_TIMER = 'dartStun'
_HEALING_INTERRUPTED = 'healingInterrupted'

class GrinchTimersPanel(TimersPanel):

    def __init__(self, mapping=None):
        super(GrinchTimersPanel, self).__init__(mapping)
        _TIMERS_PRIORITY[(_CHASED_BY_MISSILE, _TIMER_STATES.WARNING_VIEW)] = 1
        _TIMERS_PRIORITY[(_FREEZING_ZONE_UI_TIMER, _TIMER_STATES.WARNING_VIEW)] = 2
        _TIMERS_PRIORITY[(_FLARE_MARK_UI_TIMER, _TIMER_STATES.CRITICAL_VIEW)] = 9
        _TIMERS_PRIORITY[(_DART_STUN_UI_TIMER, _TIMER_STATES.CRITICAL_VIEW)] = 9
        _TIMERS_PRIORITY[(_HEALING_INTERRUPTED, _TIMER_STATES.CRITICAL_VIEW)] = 10

    def _generateMainTimersData(self):
        tData = super(GrinchTimersPanel, self)._generateMainTimersData()
        linkage = BATTLE_NOTIFICATIONS_TIMER_LINKAGES.DESTROY_TIMER_UI
        replaced = {_TIMER_STATES.WARNING_ZONE: self._getNotificationTimerData(_TIMER_STATES.WARNING_ZONE, BATTLE_NOTIFICATIONS_TIMER_LINKAGES.GRINCH_WARNING_ICON, linkage=linkage, color=BATTLE_NOTIFICATIONS_TIMER_COLORS.LIGHT_BLUE, text=backport.text(R.strings.ingame_gui.grinchBattle.warning_zone.indicator())), 
           _TIMER_STATES.DANGER_ZONE: self._getNotificationTimerData(_TIMER_STATES.DANGER_ZONE, BATTLE_NOTIFICATIONS_TIMER_LINKAGES.GRINCH_DANGER_ICON, linkage=linkage, color=BATTLE_NOTIFICATIONS_TIMER_COLORS.LIGHT_BLUE, iconOffsetY=-10), 
           _CHASED_BY_MISSILE: self._getNotificationTimerData(_CHASED_BY_MISSILE, BATTLE_NOTIFICATIONS_TIMER_LINKAGES.GRINCH_MISSILE_ICON, linkage=linkage, color=BATTLE_NOTIFICATIONS_TIMER_COLORS.RED, text=backport.text(R.strings.ingame_gui.grinchBattle.chased_by_missile.indicator())), 
           _FREEZING_ZONE_UI_TIMER: self._getNotificationTimerData(_FREEZING_ZONE_UI_TIMER, BATTLE_NOTIFICATIONS_TIMER_LINKAGES.GRINCH_DANGER_ICON, linkage=linkage, color=BATTLE_NOTIFICATIONS_TIMER_COLORS.LIGHT_BLUE, text=backport.text(R.strings.ingame_gui.grinchBattle.death_zone.indicator())), 
           _FLARE_MARK_UI_TIMER: self._getNotificationTimerData(_FLARE_MARK_UI_TIMER, BATTLE_NOTIFICATIONS_TIMER_LINKAGES.GRINCH_FLARE_MARK_ICON, linkage=linkage, color=BATTLE_NOTIFICATIONS_TIMER_COLORS.ORANGE, text=backport.text(R.strings.ingame_gui.grinchBattle.flare_mark.indicator()), iconOffsetY=-10), 
           _DART_STUN_UI_TIMER: self._getNotificationTimerData(_DART_STUN_UI_TIMER, BATTLE_NOTIFICATIONS_TIMER_LINKAGES.GRINCH_DART_STUN_MARK_ICON, linkage=linkage, color=BATTLE_NOTIFICATIONS_TIMER_COLORS.ORANGE, text=backport.text(R.strings.ingame_gui.grinchBattle.dart_stun_mark.indicator()), iconOffsetY=-10), 
           _HEALING_INTERRUPTED: self._getNotificationTimerData(_HEALING_INTERRUPTED, BATTLE_NOTIFICATIONS_TIMER_LINKAGES.GRINCH_INTERRUPTED_HEALING_ICON, linkage=linkage, color=BATTLE_NOTIFICATIONS_TIMER_COLORS.RED, text=backport.text(R.strings.ingame_gui.grinchBattle.healing_interrupted.indicator()), iconOffsetY=-10)}
        for i, tdV in enumerate(tData):
            typeID = tdV['typeId']
            if typeID in replaced:
                tData[i] = replaced[typeID]
                del replaced[typeID]

        for v in replaced.itervalues():
            tData.append(v)

        return tData

    def _onVehicleStateUpdated(self, state, value):
        if state == VEHICLE_VIEW_STATE.MAP_DEATH_ZONE:
            if value.needToCloseTimer():
                self._hideTimer(_FREEZING_ZONE_UI_TIMER)
            else:
                self._showTimer(_FREEZING_ZONE_UI_TIMER, 0.0, TIMER_VIEW_STATE.WARNING, 0.0)
        elif state == grinch_battle_constants.VEHICLE_VIEW_STATE.SONAR:
            if value.needToCloseTimer():
                self._hideTimer(_FLARE_MARK_UI_TIMER)
            else:
                self._showTimer(_FLARE_MARK_UI_TIMER, value.totalTime, value.level, value.totalTime + value.startTime)
        elif state == grinch_battle_constants.VEHICLE_VIEW_STATE.DART_STUN:
            if value.needToCloseTimer():
                self._hideTimer(_DART_STUN_UI_TIMER)
            else:
                self._showTimer(_DART_STUN_UI_TIMER, value.totalTime, value.level, value.totalTime + value.startTime)
        elif state == grinch_battle_constants.VEHICLE_VIEW_STATE.HEALING_INTERRUPTED:
            if value.needToCloseTimer():
                self._hideTimer(_HEALING_INTERRUPTED)
            else:
                self._showTimer(_HEALING_INTERRUPTED, value.totalTime, value.level, value.totalTime + value.startTime)
        if state == grinch_battle_constants.VEHICLE_VIEW_STATE.BEING_CHASED_BY_MISSILE:
            if value.needToCloseTimer():
                self._hideTimer(_CHASED_BY_MISSILE)
            else:
                self._showTimer(_CHASED_BY_MISSILE, 0.0, TIMER_VIEW_STATE.WARNING, 0.0)
        else:
            super(GrinchTimersPanel, self)._onVehicleStateUpdated(state, value)