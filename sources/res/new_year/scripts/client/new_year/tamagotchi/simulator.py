import math
from debug_utils import LOG_DEBUG
from helpers import dependency
from helpers.CallbackDelayer import CallbackDelayer
from helpers.events_handler import EventsHandler
from helpers.time_utils import ONE_MINUTE, getServerUTCTime
from new_year.ny_constants import TamagotchiState
from new_year.skeletons.new_year import ITamagotchiDataProvider
from wotdecorators import noexceptReturn
_TICK_TIME = float(ONE_MINUTE)

class TamagotchiSimulator(EventsHandler):
    __slots__ = ('__ticker', )
    _dataProvider = dependency.descriptor(ITamagotchiDataProvider)

    def __init__(self):
        super(TamagotchiSimulator, self).__init__()
        self.__ticker = CallbackDelayer()

    def init(self):
        self._subscribe()

    def fini(self):
        self._unsubscribe()
        self.__ticker.clearCallbacks()

    def setEnabled(self, state):
        self._updateCallbacks(state)

    @classmethod
    def getDelayTime(cls):
        timeDiff = math.floor(getServerUTCTime() - cls._dataProvider.initialPlayerInfo.lastUpdateTime)
        return _TICK_TIME - timeDiff % _TICK_TIME

    def _updateCallbacks(self, state):
        self.__ticker.clearCallbacks()
        if not state or not self._dataProvider.isValidConfig:
            return
        self.__ticker.delayCallback(0, self.__tick)

    @noexceptReturn(_TICK_TIME)
    def __tick(self):
        self.update()
        return self.getDelayTime()

    def update(self):
        timestamp = getServerUTCTime()
        self.__updateDebHistory(timestamp)
        oldIndicators = dict(self._dataProvider.playerInfo.indicators)
        self._dataProvider.getIndicatorStates().clear()
        for name, points in self._dataProvider.initialPlayerInfo.indicators.iteritems():
            if points < 0 or name not in self._dataProvider.config.indicators:
                continue
            self.__updateIndicator(name, points, timestamp)

        if self.__hasDecreasedIndicators(oldIndicators):
            self._dataProvider.onDecreasedIndicatorsPoints()
        self.__updateState()
        LOG_DEBUG('[TAMAGOTCHI tick] ', self._dataProvider.playerInfo.state, self._dataProvider.playerInfo.indicators, self._dataProvider.getDeb())
        self._dataProvider.setRaidReady()
        self._dataProvider.onSimulationEnd()

    def __updateIndicator(self, name, points, timestamp):
        sInfo = self._dataProvider.playerInfo
        states = self._dataProvider.getIndicatorStates()
        decayConfig = self._dataProvider.config.indicators[name]
        timeDiff = max(0, timestamp - self._dataProvider.initialPlayerInfo.lastUpdateTime)
        minutesDiff = math.floor(timeDiff / _TICK_TIME)
        state = 0
        for level in reversed(decayConfig.levels):
            if points < level.points:
                continue
            minutesToDecay = (points - level.points) / level.degradation
            if minutesToDecay >= minutesDiff:
                points = points - level.degradation * minutesDiff
                state = level.state
                break
            points = level.points
            minutesDiff -= minutesToDecay

        sInfo.indicators[name] = points
        states[name] = state

    def __hasDecreasedIndicators(self, oldIndicators):
        return any(self._dataProvider.playerInfo.indicators.get(name, 0) < points for name, points in oldIndicators.iteritems())

    def __updateState(self):
        score = maxScore = 0
        for name, value in self._dataProvider.getIndicatorStates().iteritems():
            score += value
            maxScore += self._dataProvider.config.indicators[name].levels[(-1)].state

        if score == 0:
            self._dataProvider.playerInfo.state = TamagotchiState.SAD.value
            return
        if score == maxScore:
            self._dataProvider.playerInfo.state = TamagotchiState.FUN.value
            return
        self._dataProvider.playerInfo.state = TamagotchiState.NORMAL.value

    def __updateDebHistory(self, timestamp):
        history = self._dataProvider.playerInfo.debHistory
        while history:
            top = history[0]
            if top.expirationTime > timestamp:
                break
            history.popleft()

        for bonus in history:
            if bonus.expirationTime >= timestamp:
                self._dataProvider.debValue = bonus.value
                break
        else:
            self._dataProvider.debValue = 0

        self._dataProvider.onBonusUpdated()