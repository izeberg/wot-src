import logging, BigWorld
from PlayerEvents import g_playerEvents
_logger = logging.getLogger(__name__)

class AccountNewbieChatLockComponent(BigWorld.StaticScriptComponent):

    def setChatLockingState(self, chatLocked):
        _logger.debug('AccountNewbieChatLockComponent.setChatLockingState %s', chatLocked)
        self.chatLocked = chatLocked

    def chatLockingStateChanged(self, chatLocked):
        _logger.debug('AccountNewbieChatLockComponent.chatLockingStateChanged %s', chatLocked)
        self.chatLocked = chatLocked
        g_playerEvents.onNewbieChatLockingStateChanged()