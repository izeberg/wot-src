import random, typing, AnimationSequence, SoundGroups, Windowing
from PlayerEvents import g_playerEvents
from debug_utils import LOG_DEBUG, LOG_ERROR
from gui.hangar_cameras.hangar_camera_common import CameraRelatedEvents
from gui.shared import EVENT_BUS_SCOPE
from helpers import dependency
from helpers.CallbackDelayer import CallbackDelayer
from helpers.events_handler import EventsHandler
from new_year.interactive_state_machine.constants import PersonaTypes, INACTIVITY_THRESHOLD_RANGE
from new_year.interactive_state_machine.sm_handler import StateMachineHandler
from new_year.interactive_state_machine.sm_handler_man import ManStateMachineHandler
from new_year.interactive_state_machine.sm_handler_old_man import OldManStateMachineHandler
from new_year.interactive_state_machine.sm_handler_woman import WomanStateMachineHandler
from new_year.skeletons.i_sm_queue import IStateMachineQueue
from new_year.skeletons.i_sm_queue_context import IQueueContext
from shared_utils import nextTick
from skeletons.gui.impl import IGuiLoader
_HANGAR_ENTER_TIMEOUT = 15
_ORDER = (PersonaTypes.OLD_MAN, PersonaTypes.CELEB_MAN)
_VO_SEQ_PAUSE = 'ny_vo_seq_pause'
_VO_SEQ_RESUME = 'ny_vo_seq_resume'

class StateMachineQueue(IStateMachineQueue, EventsHandler):
    __slots__ = ('__items', '__inactiveQueue', '__callbackDelayer', '__isWindowMinimized')
    __guiLoader = dependency.descriptor(IGuiLoader)
    __context = dependency.descriptor(IQueueContext)

    def __init__(self):
        super(StateMachineQueue, self).__init__()
        self.__items = {}
        self.__inactiveQueue = []
        self.__isWindowMinimized = False
        self.__callbackDelayer = CallbackDelayer()

    @nextTick
    def init(self):
        self._subscribe()
        Windowing.addWindowAccessibilitynHandler(self.__onWindowAccessibilityChanged)

    def fini(self):
        Windowing.removeWindowAccessibilityHandler(self.__onWindowAccessibilityChanged)
        self._unsubscribe()
        self.__callbackDelayer.clearCallbacks()

    @property
    def items(self):
        return self.__items

    @property
    def handlersDict(self):
        return {PersonaTypes.CELEB_MAN: ManStateMachineHandler, 
           PersonaTypes.CELEB_WOMAN: WomanStateMachineHandler, 
           PersonaTypes.OLD_MAN: OldManStateMachineHandler}

    def lock(self):
        if self.__context.isLocked:
            return False
        self.__context.isLocked = True
        return True

    def release(self):
        self.__context.isLocked = False

    def bind(self, personaType, animatorComponent):
        self.unbind(personaType)
        item = self.handlersDict[personaType](animatorComponent)
        self.__items[personaType] = item
        item.init()

    def unbind(self, personaType):
        self.__inactiveQueue = []
        item = self.__items.pop(personaType, None)
        if item is not None:
            item.fini()
        return

    def handleCloseUp(self, personaType, state):
        return self._proxy('handleCloseUp', personaType, state)

    def handleRewards(self, personaType, rewards):
        return self._proxy('handleRewards', personaType, rewards)

    def handleLoaded(self):
        if not self.__callbackDelayer.hasDelayedCallback(self._loadedCallback):
            self.__callbackDelayer.delayCallback(_HANGAR_ENTER_TIMEOUT, self._loadedCallback)

    def _handleLoaded(self, personaType):
        return self._proxy('handleLoaded', personaType)

    def _proxy(self, name, personaType, *args, **kwargs):
        if self.__context.isLocked:
            LOG_DEBUG('[NY] SM global lock', name, personaType, args, kwargs)
            return
        else:
            if personaType not in self.__items:
                LOG_DEBUG('[NY] Failed to find SM for', name, personaType, args, kwargs)
                return
            attr = getattr(self.__items[personaType], name, None)
            if not attr:
                LOG_ERROR('[NY] Failed to find attr for', name, personaType, args, kwargs)
                return
            return attr(*args, **kwargs)

    def _loadedCallback(self):
        for pType in _ORDER:
            if self._handleLoaded(pType):
                return

    def _getListeners(self):
        return ((CameraRelatedEvents.IDLE_CAMERA, self.__handleIdleCameraActivation, EVENT_BUS_SCOPE.GLOBAL),)

    def _getEvents(self):
        return (
         (
          g_playerEvents.onAvatarBecomePlayer, self.__onAvatarBecomePlayer),
         (
          g_playerEvents.onDisconnected, self.__onDisconnected))

    def __onAvatarBecomePlayer(self):
        self.__context.wasInBattle = True

    def __onDisconnected(self):
        self.__context.reset()
        self.__callbackDelayer.clearCallbacks()

    def __handleIdleCameraActivation(self, event):
        isStarted = event.ctx['started']
        if not isStarted or not self.__items:
            self.__callbackDelayer.stopCallback(self.__handleInactivity)
            return
        self.__callbackDelayer.delayCallback(0, self.__handleInactivity)

    def __handleInactivity(self):
        if self.__isWindowMinimized or not AnimationSequence.getEnableAnimationSequenceUpdate():
            return 5.0
        if not self.__inactiveQueue:
            self.__inactiveQueue = self.__items.values()
            random.shuffle(self.__inactiveQueue)
        if not self.__inactiveQueue:
            return
        self.__inactiveQueue.pop().handleInactivity()
        return random.uniform(*INACTIVITY_THRESHOLD_RANGE)

    def __onWindowAccessibilityChanged(self, _):
        isMinimized = Windowing.isWindowMinimized()
        if isMinimized == self.__isWindowMinimized:
            return
        self.__isWindowMinimized = isMinimized
        if not self.__items:
            return
        eventName = _VO_SEQ_PAUSE if isMinimized else _VO_SEQ_RESUME
        SoundGroups.g_instance.playSound2D(eventName)