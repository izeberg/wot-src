import WWISE, BigWorld
from constants import ARENA_PERIOD
from gui.shared import g_eventBus, EVENT_BUS_SCOPE
from helpers import dependency
from lunar_possession.gui.shared.events import MatchRoundsEvents
from gui.impl import backport
from gui.impl.gen import R
from gui.Scaleform.daapi.view.battle.shared.battle_timers import PreBattleTimer, BattleTimer
from gui.battle_control.battle_constants import COUNTDOWN_STATE
from skeletons.gui.battle_session import IBattleSessionProvider

class ROUND_STATE(object):
    UNDEFINED = 0
    ROUND_START = 1


_ROUND_MESSAGE = {ROUND_STATE.ROUND_START: R.strings.lunar_battle.hints.roundStart()}

class LunarPossessionPreBattleTimer(PreBattleTimer):
    _RTPC = 'RTPC_ext_battle_countdown_timer'

    def __init__(self):
        super(LunarPossessionPreBattleTimer, self).__init__()
        self.__soundID = dependency.instance(IBattleSessionProvider).arenaVisitor.type.getCountdownTimerSound()
        self.__roundStatus = ROUND_STATE.UNDEFINED
        self.__timeLeft = None
        return

    def _onHideAll(self, speed):
        super(LunarPossessionPreBattleTimer, self)._onHideAll(speed)
        self.as_setWinConditionTextS('')
        self.as_setMessageS('')

    def _populate(self):
        super(LunarPossessionPreBattleTimer, self)._populate()
        g_eventBus.addListener(MatchRoundsEvents.ROUND_START, self.__onRoundStart, EVENT_BUS_SCOPE.BATTLE)

    def _dispose(self):
        g_eventBus.removeListener(MatchRoundsEvents.ROUND_START, self.__onRoundStart, EVENT_BUS_SCOPE.BATTLE)
        super(LunarPossessionPreBattleTimer, self)._dispose()

    def __onRoundStart(self, event):
        self.__roundStatus = ROUND_STATE.ROUND_START
        self.as_setMessageS(self._getMessage())
        self.setCountdown(COUNTDOWN_STATE.START, event.timer)

    def _getMessage(self):
        if self.__roundStatus != ROUND_STATE.UNDEFINED:
            msg = backport.text(_ROUND_MESSAGE[self.__roundStatus])
            return msg
        return super(LunarPossessionPreBattleTimer, self)._getMessage()

    def setCountdown(self, state, timeLeft):
        if self.__roundStatus != ROUND_STATE.UNDEFINED:
            self.__timeLeft = timeLeft
            self.__updateRoundTimer()
        else:
            super(LunarPossessionPreBattleTimer, self).setCountdown(state, timeLeft)

    def __updateRoundTimer(self):
        self.__callbackID = None
        if self.__timeLeft > 0:
            self.__timeLeft -= 1
            self.as_setTimerS(self.__timeLeft)
            if self.__roundStatus == ROUND_STATE.ROUND_START:
                BigWorld.callback(0.5, self.__playSound)
            self.__callbackID = BigWorld.callback(1, self.__updateRoundTimer)
        else:
            self.__roundStatus = ROUND_STATE.UNDEFINED
            self.hideCountdown(COUNTDOWN_STATE.STOP, 0)
        return

    def __playSound(self):
        if self.__soundID:
            WWISE.WW_setRTCPGlobal(self._RTPC, self.__timeLeft)
            WWISE.WW_eventGlobal(self.__soundID)


class LunarPossessionBattleTimer(BattleTimer):

    def __init__(self):
        super(LunarPossessionBattleTimer, self).__init__()
        self.__period = ARENA_PERIOD.IDLE

    def setPeriod(self, period):
        self.__period = period

    def hideTotalTime(self):
        pass