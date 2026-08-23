from __future__ import absolute_import
from functools import partial
import typing, BigWorld
from helpers.dependency import descriptor
from helpers.time_utils import getServerUTCTime, getDayTimeLeft, ONE_DAY
from journey_marathon.jm_constants import JmTimeState, JM_RUNNING_OUT_THRESHOLD, JmTokensUpdType, JmTimeUpdType
from journey_marathon.jm_helpers import jmCtrl
from skeletons.gui.lobby_context import ILobbyContext
if typing.TYPE_CHECKING:
    from typing import Tuple, Union, Optional
    from helpers.server_settings import ServerSettings
    from journey_marathon.jm_constants import JmTokensUpdTypes, JmTimeUpdTypes
    Num = Union[(float, int, long)]

class JmTime(object):
    __lobbyCtx = descriptor(ILobbyContext)

    def __init__(self):
        self.__stamps = (0, 0)
        self.__timeState = JmTimeState.UNDEFINED
        self.__timeStateCBID = None
        self.__serverSettings = None
        return

    def init(self):
        jmCtrl().onJmTokensChange += _onNewQuestsUpdTime
        self.__lobbyCtx.onServerSettingsChanged += self.__onServerSettingsReset

    def fini(self):
        jmCtrl().onJmTokensChange -= _onNewQuestsUpdTime
        self.__lobbyCtx.onServerSettingsChanged -= self.__onServerSettingsReset
        self.__cancelTimeStateCB()
        self.__serverSettings = None
        return

    def getJmTimeState(self):
        return self.__timeState

    def getJmTimeStamps(self):
        return self.__stamps

    def getJmTimeLeft(self):
        state = self.__timeState
        start, finish = self.__stamps
        now = getServerUTCTime()
        if state == JmTimeState.PRE:
            return start - now
        if state in (JmTimeState.DURING, JmTimeState.RUNNING_OUT):
            return finish - now
        return 0

    def getJmTimeTillNewQuests(self):
        if self.__serverSettings is not None:
            return getDayTimeLeft()
        else:
            return ONE_DAY

    def invalidateJmDatesConfig(self, newStamps):
        if self.__stamps == newStamps:
            return
        self.__stamps = newStamps
        updType = {JmTimeUpdType.STAMPS}
        updType |= self.__invalidateTimeState()
        self.__startTimeStateCB()
        jmCtrl().onJmTimeChange(updType)

    def hasMoreJmQuestRerolls(self):
        offset = self.__getGameDayOffset()
        now = getServerUTCTime()
        _, finish = self.__stamps
        currAbsDay = _getAbsoluteGameDay(now, offset)
        nextGameDayStart = (currAbsDay + 1) * ONE_DAY + offset
        return nextGameDayStart < finish

    def getAbsoluteGameDay(self):
        now = getServerUTCTime()
        offset = self.__getGameDayOffset()
        return _getAbsoluteGameDay(now, offset)

    def __getGameDayOffset(self):
        if self.__serverSettings is None:
            return 0
        else:
            return self.__serverSettings.regionals.getGameDayStartingTime()

    def __invalidateTimeState(self, nextState=None):
        now = getServerUTCTime()
        start, finish = self.__stamps
        if nextState is not None:
            timeState = nextState
        elif now <= start:
            timeState = JmTimeState.PRE
        elif now >= finish:
            timeState = JmTimeState.POST
        elif finish - now <= JM_RUNNING_OUT_THRESHOLD:
            timeState = JmTimeState.RUNNING_OUT
        else:
            timeState = JmTimeState.DURING
        if timeState != self.__timeState:
            self.__timeState = timeState
            return {
             JmTimeUpdType.STATE}
        else:
            return set()

    def __timeStateCB(self, nextState):
        self.__timeStateCBID = None
        updType = self.__invalidateTimeState(nextState)
        jmCtrl().onJmTimeChange(updType)
        return

    def __startTimeStateCB(self):
        self.__cancelTimeStateCB()
        state = self.__timeState
        start, finish = self.__stamps
        if state == JmTimeState.PRE:
            endTime = start
            nextState = JmTimeState.DURING
        elif state == JmTimeState.RUNNING_OUT:
            endTime = finish
            nextState = JmTimeState.POST
        elif state == JmTimeState.DURING:
            endTime = finish - JM_RUNNING_OUT_THRESHOLD
            nextState = JmTimeState.RUNNING_OUT
        else:
            return
        timeLeft = endTime - getServerUTCTime()
        self.__timeStateCBID = BigWorld.callback(timeLeft, partial(self.__timeStateCB, nextState))

    def __cancelTimeStateCB(self):
        if self.__timeStateCBID is not None:
            BigWorld.cancelCallback(self.__timeStateCBID)
            self.__timeStateCBID = None
        return

    def __onServerSettingsReset(self, serverSettings):
        self.__serverSettings = serverSettings


def _onNewQuestsUpdTime(updTypes, _):
    if JmTokensUpdType.QUEST in updTypes:
        jmCtrl().onJmTimeChange({JmTimeUpdType.QUESTS_REROLL})


def _getAbsoluteGameDay(stampUTC, offset):
    return int((stampUTC - offset) // ONE_DAY)