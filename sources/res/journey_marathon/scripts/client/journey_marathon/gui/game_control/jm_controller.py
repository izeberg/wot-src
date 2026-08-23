from __future__ import absolute_import
import logging
from Event import EventManager, Event
from PlayerEvents import g_playerEvents
from constants import IS_DEVELOPMENT
from gui.prb_control.entities.listener import IGlobalListener
from journey_marathon.gui.game_control.jm_components import JmConfig, JmNodesCtrl, JmTime, JmQuests, JmTokens, JmSwitcher, JmSysMessages, JmBonuses
from journey_marathon.jm_helpers import initJmAccountSettings
from journey_marathon.skeletons.game_control import IJourneyMarathonController
_logger = logging.getLogger(__name__)

class JourneyMarathonController(IJourneyMarathonController, IGlobalListener):

    def __init__(self):
        self.__em = em = EventManager()
        self.onJmFeatureStateChange = Event(em)
        self.onJmTimeChange = Event(em)
        self.onJmNodesChange = Event(em)
        self.onJmQuestsChange = Event(em)
        self.onJmTokensChange = Event(em)
        self.onJmConfigChange = Event(em)
        self.onJmConfigErrors = Event(em)
        self.__logEvents()
        self.jmConfig = JmConfig()
        self.jmSwitcher = JmSwitcher()
        self.jmTokens = JmTokens()
        self.jmNodes = JmNodesCtrl()
        self.jmTime = JmTime()
        self.jmQuests = JmQuests()
        self.jmSysMessages = JmSysMessages()
        self.jmBonuses = JmBonuses()

    def init(self):
        initJmAccountSettings()
        self.jmBonuses.init()

    def fini(self):
        self.jmBonuses.fini()
        self.__em.clear()

    def onConnected(self):
        self.jmConfig.init()
        self.jmTokens.init()
        self.jmNodes.init()
        self.jmTime.init()
        self.jmQuests.init()
        self.jmSysMessages.init()
        g_playerEvents.onPrbDispatcherCreated += self.__onPrbDispatcherCreated

    def onDisconnected(self):
        g_playerEvents.onPrbDispatcherCreated -= self.__onPrbDispatcherCreated
        self.stopGlobalListening()
        self.jmSysMessages.fini()
        self.jmQuests.fini()
        self.jmTime.fini()
        self.jmNodes.fini()
        self.jmTokens.fini()
        self.jmConfig.fini()

    def onPrbEntitySwitched(self):
        self.jmSwitcher.invalidateJmFeatureState()

    def onLobbyInited(self, _):
        self.jmSysMessages.onLobbyInited()

    def __onPrbDispatcherCreated(self):
        self.startGlobalListening()

    def __logEvents(self):
        if IS_DEVELOPMENT:
            for name, event in self.__dict__.items():
                if isinstance(event, Event):
                    event += _makeEventLogger(name, event)


def _makeEventLogger(eventName, event):

    def _logEvent(*args, **kwargs):
        strArgs = []
        if args:
            strArgs.append('args=' + str(args))
        if kwargs:
            strArgs.append('kwargs=' + str(kwargs))
        subs = [ sub for sub in event if sub is not _logEvent ]
        msg = 'JmEvent(%s).__call__(%s) -> %s' % (eventName, (', ').join(strArgs), subs)
        _logger.info(msg)

    return _logEvent