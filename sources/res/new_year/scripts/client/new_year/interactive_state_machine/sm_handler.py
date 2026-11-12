from datetime import datetime
import typing
from debug_utils import LOG_DEBUG
from gui.Scaleform.framework.entities.View import ViewKey
from gui.app_loader.settings import APP_NAME_SPACE
from helpers import dependency
from helpers.events_handler import EventsHandler
from helpers.time_utils import getCurrentTimestamp, getDateTimeInUTC, ONE_MINUTE
from new_year.gui.constants import VIEW_ALIAS
from new_year.gui.impl.lobby.new_year.quests.ny_quest_helper import getWeekFromStart
from new_year.interactive_state_machine.config import getSMSetting, setSMSetting
from new_year.interactive_state_machine.constants import NEW_ENTER_COOLDOWN
from new_year.ny_constants import GREETINGS_TIMESTAMP, FIRST_ENTRANCE, WEEKLY_GREETINGS_COUNT
from new_year.skeletons.i_sm_queue_context import IQueueContext
from skeletons.gui.app_loader import IAppLoader
if typing.TYPE_CHECKING:
    from GenericComponents import AnimatorComponent

class StateMachineHandler(EventsHandler):
    __slots__ = ('__animator', '__state')
    _TYPE = None
    _IDLE_S = 'idle'
    _CLOSE_UP_IDLE_S = 'idle_close_up'
    _INACTIVITY_S = 'inactivity'
    _GREETING_S = 'greeting'
    _GREETING_WEEKLY_S = 'greeting_weekly'
    _FIRST_ENTER_S = 'first_enter'
    _INTERRUPT_GROUP = (
     _IDLE_S, _CLOSE_UP_IDLE_S, _INACTIVITY_S)
    _CLOSE_UP_IDLE_V = 'isCloseUp'
    __context = dependency.descriptor(IQueueContext)
    __appLoader = dependency.descriptor(IAppLoader)

    def __init__(self, animator):
        super(StateMachineHandler, self).__init__()
        self.__animator = animator
        self.__state = self._IDLE_S
        self.__animator.setOnStateNodeChanged(self._onAnimatorNodeChanged)

    def init(self):
        self._subscribe()

    def fini(self):
        self._unsubscribe()

    @property
    def isEnabled(self):
        return True

    @property
    def animator(self):
        return self.__animator

    @property
    def state(self):
        return self.__state

    @property
    def isHangarViewLoaded(self):
        app = self.__appLoader.getApp(APP_NAME_SPACE.SF_LOBBY)
        if app and app.containerManager:
            return app.containerManager.getViewByKey(ViewKey(VIEW_ALIAS.LOBBY_HANGAR)) is not None
        else:
            return False

    def setTrigger(self, name):
        return self.__animator.setTrigger(name)

    def handleInactivity(self):
        if self.__state == self._IDLE_S and not self.__context.isLocked:
            self.setTrigger(self._INACTIVITY_S)

    def handleLoaded(self):
        pass

    def handleCloseUp(self, isCloseUp):
        self.__animator.setBoolParam(self._CLOSE_UP_IDLE_V, isCloseUp)
        if self.__state not in self._INTERRUPT_GROUP:
            return
        if isCloseUp and self.isEnabled and self._handleGreeting():
            return
        self.setTrigger(self._CLOSE_UP_IDLE_S if isCloseUp else self._IDLE_S)

    def _handleGreeting(self):
        return self._handleFirstEnter() or self._handleNewWeek() or self._handleNewEnter() or self._handleNewDay()

    def _handleFirstEnter(self):
        if not getSMSetting(FIRST_ENTRANCE, self._TYPE) or not self.isEnabled:
            return False
        setSMSetting(FIRST_ENTRANCE, self._TYPE, False)
        setSMSetting(GREETINGS_TIMESTAMP, self._TYPE, getCurrentTimestamp())
        self.setTrigger(self._FIRST_ENTER_S)
        return True

    def _handleNewDay(self):
        if not self.isEnabled:
            return False
        prevTimestamp = getSMSetting(GREETINGS_TIMESTAMP, self._TYPE)
        isNewDay = datetime.utcnow().date() != getDateTimeInUTC(prevTimestamp).date()
        if not isNewDay:
            return False
        setSMSetting(GREETINGS_TIMESTAMP, self._TYPE, getCurrentTimestamp())
        self.setTrigger(self._GREETING_S)
        return True

    def _handleNewEnter(self):
        if not self.isEnabled:
            return False
        prevTimestamp = getSMSetting(GREETINGS_TIMESTAMP, self._TYPE)
        currentTimestamp = getCurrentTimestamp()
        minutesElapsed = (currentTimestamp - prevTimestamp) / float(ONE_MINUTE)
        if minutesElapsed < NEW_ENTER_COOLDOWN:
            return False
        setSMSetting(GREETINGS_TIMESTAMP, self._TYPE, currentTimestamp)
        self.setTrigger(self._GREETING_S)
        return True

    def _handleNewWeek(self):
        if not self.isEnabled:
            return False
        currWeek = getWeekFromStart()
        if getSMSetting(WEEKLY_GREETINGS_COUNT, self._TYPE) == currWeek:
            return False
        setSMSetting(WEEKLY_GREETINGS_COUNT, self._TYPE, currWeek)
        self.setTrigger(self._GREETING_WEEKLY_S)
        return True

    def _onAnimatorNodeChanged(self, _):
        self.__state = self.__animator.getStateNodeName()
        LOG_DEBUG('NY SM animator node changed', self._TYPE, self.__state)